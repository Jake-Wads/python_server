#!/usr/bin/env python3

import yaml
import os
import logging

def to_markdown(chapter, level=0):
    logging.debug('level {} -- {}'.format(level, chapter))
    for title, v in chapter.items():
        if type(v) is str:
            logging.debug('type(v) is str')
            url = v.replace('index.md', '').replace('.md', '/')
            print('%s- [%s](/%s)' % ('    ' * (level - 1), title, url))
        else:
            logging.debug('type(v) is not str')
            if level == 0:
                print('\n## %s\n' % title)
            else:
                print('%s- %s' % ('    ' * (level - 1), title))
            for chapter in v:
                to_markdown(chapter, level + 1)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.description = 'Generate a single markdown file table of contents for the curriculum based on the table of contents in the mkdocs.yml file'
    parser.add_argument('-v', '--verbose',
                        help='increase output verbosity', action='count')
    args = parser.parse_args()

    if args.verbose is None:
        loglevel = logging.WARN
    elif args.verbose == 1:
        loglevel = logging.INFO
    elif args.verbose >= 2:
        loglevel = logging.DEBUG
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S', level=loglevel)

    print()
    with open('./build/mkdocs.yml') as f:
        for chapter in yaml.load(f.read(), Loader=yaml.BaseLoader)['nav']:
            to_markdown(chapter)

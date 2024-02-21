'''
Script to remove student's personally identifying information from the
curriculum access logs.
'''

import pandas as pd
from pandas import DataFrame
from os import system
import logging
import csv
from fileinput import FileInput


def download_log_file(dest: str):
    cmd = f'scp ryan@java.codeup.com:/srv/www/codeup.com/storage/logs/curriculum-access.txt {dest}'
    logging.info('using scp to download the log file')
    logging.debug(cmd)
    system(cmd)
    logging.info('log file downloaded')


def get_df(path) -> DataFrame:
    logging.info('reading log file into a data frame')
    df: DataFrame = pd.read_csv(
        './data/curriculum-access.txt', sep='\t', header=None)

    df.columns = ['timestamp', 'path', 'user', 'cohort_id', 'ip']

    unique_users = list(df.user.unique())
    lookup_user = {name: (i + 1) for i, name in enumerate(unique_users)}

    df.user = df.user.apply(lambda user: lookup_user[user])
    df.rename(columns={'user': 'user_id'}, inplace=True)
    df.cohort_id = df.cohort_id.astype('str').str.replace('.0', '')
    return df


def write_txt_file(df: DataFrame, path):
    logging.info(f'Writing out to {path}')
    df.to_csv(path, sep=' ', header=None, index=False,
              quoting=csv.QUOTE_NONE, escapechar='\\')
    # pandas leaves an escape character in the timestamp field, we want to
    # remove this, so we'll have to re-read and write the file
    with FileInput(path, inplace=True) as f:
        for line in f:
            print(line.replace('\\', ''), end='')
    logging.info('Compressing...')
    system(f'rm -f {path}.gz')
    system(f'gzip -q {path}')


def main(download: bool, infile: str, outfile: str, repl: bool):
    if download:
        download_log_file(infile)
    df = get_df(infile)
    write_txt_file(df, outfile)
    if repl:
        from IPython import embed
        embed()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.description = 'optionally download the access log, and anonymize student names'
    parser.add_argument('-v', '--verbose',
                        help='increase output verbosity', action='count')
    parser.add_argument('--download', action='store_true',
                        help='Download the log file from the curriculum server')
    parser.add_argument('--infile', default='./data/curriculum-access.txt',
                        help='Where the original log file lives (default: %(default)s)')
    parser.add_argument('--outfile', default='./data/anonymized-curriculum-access.txt',
                        help='Where the anonymized data should be written to (default: %(default)s)',)
    parser.add_argument('--repl', action='store_true',
                        help='Start a repl with the curriculum access data frame as "df"')
    args = parser.parse_args()

    if args.verbose is None:
        loglevel = logging.WARN
    elif args.verbose == 1:
        loglevel = logging.INFO
    elif args.verbose >= 2:
        loglevel = logging.DEBUG
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S', level=loglevel)

    logging.info(f'Starting up, download = {args.download}')
    main(args.download, args.infile, args.outfile, args.repl)
    logging.info('All Done')

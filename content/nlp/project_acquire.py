'''
This script contains functionality to do the data acquisition for the Codeup NLP
module project[1]. It acquires the data through GitHub's API, as opposed to
scraping it from their website, which was causing us to get rate-limited to
github.

This script can be shared with students if they are running short on time, or
presented as part of the project "solution".

In order to use this script, you must:

- Make a github personal access token and put it in an env.py file. To generate
  a personal access token, go here [2]. Note that the token does not need any
  permissions, it just needs to exist.
- Replace YOUR_GITHUB_USERNAME in this script with your github username.
- Populate the repos list defined towards the end of this file with a list of
  repos you want to scrape.

[1]: https://ds.codeup.com/10-nlp/project/
[2]: https://github.com/settings/tokens
'''

import os
import json
from typing import Dict, List
import requests

from env import github_token

headers = {
    'Authorization': f'token {github_token}',
    'User-Agent': 'YOUR_GITHUB_USERNAME'
}

def github_api_request(url: str) -> requests.Response:
    return requests.get(url, headers=headers)

def get_repo_language(repo: str) -> str:
    url = f'https://api.github.com/repos/{repo}'
    return github_api_request(url).json()['language']

def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f'https://api.github.com/repos/{repo}/contents/'
    return github_api_request(url).json()

def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    '''
    Takes in a response from the github api that lists
    the files in a repo and returns the url that can be
    used to download the repo's README file.
    '''
    for file in files:
        if file['name'].lower().startswith('readme'):
            return file['download_url']

def process_repo(repo: str) -> Dict[str, str]:
    '''
    Takes a repo name like "gocodeup/codeup-setup-script" and returns
    a dictionary with the language of the repo and the readme contents.
    '''
    contents = get_repo_contents(repo)
    return {
        'repo': repo,
        'language': get_repo_language(repo),
        'readme_contents': requests.get(get_readme_download_url(contents)).text
    }

def scrape_github_data(repos: List[str], fp='data.json'):
    data = [process_repo(repo) for repo in repos]
    json.dump(data, open(fp, 'w'))

# TODO: put a lot of repos here (or generate the list progromatically)
repos = [
    'gocodeup/codeup-setup-script',
    'gocodeup/movies-application'
]

if __name__ == '__main__':
    scrape_github_data(repos)

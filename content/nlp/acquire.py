from requests import get
from bs4 import BeautifulSoup
from os import path

def get_article_text():
    # if we already have the data, read it locally
    if path.exists('article.txt'):
        with open('article.txt') as f:
            return f.read()

    # otherwise go fetch the data
    url = 'https://codeup.com/data-science/math-in-data-science/'
    headers = {'User-Agent': 'Codeup Data Science'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text)
    article = soup.find('div', id='main-content')

    # save it for next time
    with open('article.txt', 'w') as f:
        f.write(article.text)

    return article.text

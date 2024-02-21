import unicodedata
import re
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords


def basic_clean(text):
    text = unicodedata.normalize('NFKD', text.lower())\
        .encode('ascii', 'ignore')\
        .decode('utf-8', 'ignore')
    return re.sub(r"[^a-z0-9'\s]", '', text)

def stem(text):
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in text.split()]
    return ' '.join(stems)

def lemmatize(text):
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in text.split()]
    return ' '.join(lemmas)

def remove_stopwords(text):
    tokenizer = ToktokTokenizer()
    stopword_list = stopwords.words('english')
    stopword_list.remove('no')
    stopword_list.remove('not')
    tokens = tokenizer.tokenize(text)
    filtered_tokens = [t for t in tokens if t not in stopword_list]
    return ' '.join(filtered_tokens)

def prep_article_data(text):
    return {
        'original': text,
        'stemmed': stem(basic_clean(text)),
        'lemmatized': lemmatize(basic_clean(text)),
        'clean': remove_stopwords(basic_clean(text))
    }

if __name__ == '__main__':
    import acquire
    data = prep_article_data(acquire.get_article_text())

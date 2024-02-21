# NLP

- LDA?
    - latent dirichlet allocation
    - technique for topic modeling
    - [whitepaper](http://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf)
    - **not** linear discriminant analysis
    - classify text in documents to topics
    - document -> topic
    - topic -> words
    - `sklearn.decomposition.LatentDirichletAllocation` takes in a bag of words
- Wordnet?
    - existing database from the cognitive science lab at princeton
    - dictionary + thesaurus
    - abstract vs specific nouns
    - heirarchy of information (e.g. dog -> canine -> carnivore -> mammal -> animal)
- POS meaning?
    - [table with definitions](https://www.guru99.com/pos-tagging-chunking-nltk.html)
- topic modeling
    - basically just LDA?
    - [Probabilistic Topic Models](https://cacm.acm.org/magazines/2012/4/147361-probabilistic-topic-models/fulltext) ACM whitepaper
- LSA (TF-IDF?)
- word embedding
    - words or phrases to vector of real numbers
    - words with similar meanings have similar representations
    - word2vec
- levenstein distance: how many edits (insertion, deletion, or change) to get
  from one word to another

## Libraries

| Library                                                                   | Description                                                                        |
| :------                                                                   | :----------                                                                        |
| [`nltk`](https://www.nltk.org/)                                           | Natural Language Toolkit; de-facto standard, most common library for nlp in python |
| [textblob](https://textblob.readthedocs.io/en/dev/)                       | Built on top of `nltk`, makes common operations easier                             |
| [spacy](https://spacy.io/)                                                | NLP from the ground up. Very fast, but less common. Gaining popularity             |
| [textacy](https://chartbeat-labs.github.io/textacy/build/html/index.html) | Built on top of spacy, makes common use cases easier                               |

## Prep

- general cleaning: probably always do this
    - unicode normalize
    - lowercase
- handle punctuation
- stopwords
- contractions
- tokenization
- stemming / lemmatizing

## EDA

How can we put a number on a document?

- unigrams, bigrams, trigrams frequency (+categorical (target?))
    - overall or by document
    - proportion by category/target
- domain-driven features
    - built-in to the data: likes, retweets, upvotes, downvotes, stars
    - domain-knowledge:
        - number of @mentions, #hashtags
        - is the product name metioned in the review?
        - time to respond in customer support chat
- common measures
    - text length
    - word count
    - sentence count
    - stopword count
    - non-stopwords count
    - unique word count
    - punctuation count
    - avg (or other aggregate) words per sentence
    - avg (or other aggregate) word length
    - stopword / non-stopword ratio
- sentiment analysis
    - knowledge-based + statistical approach
    - relies on human-labelled data
        - valence scored wordlists
        - overall labels, measure is how well it compares to human judgement
    - different models for diff domains (e.g. social media vs news)
    - for social media
        - Afinn ([github](https://github.com/fnielsen/afinn) + [whitepaper](http://www2.imm.dtu.dk/pubdb/edoc/imm6006.pdf))
        - Vader ([whitepaper](http://comp.social.gatech.edu/papers/icwsm14.vader.hutto.pdf) `nltk.sentiment.vader.SentimentIntensityAnalyzer`)
- word clouds

## Modeling

How do we represent a document?

- Bag of words (`sklearn.feature_extraction.text.CountVectorizer`)
- Bag of bigrams (ngram_range=(2, 2))
- TF-IDF (`sklearn.feature_extraction.text.TfidfVectorizer`)
- scikit-learn objects give back sparse matrices here

Find the most useful of the above (RFE) and combine with other features from
exploration.

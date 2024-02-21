# NLP Project

For this project, you will be using data from GitHub repository README files.
The goal is to build a model that can predict the main programming language
of a repository, given the text of the README file.

## Deliverables

- A new GitHub repository
    - a well-documented jupyter notebook that contains your analysis
    - a README file that contains a description of your project, as well as
      instructions on how to run it
- Slides (with presentation) 
    - suitable for a general audience
    - summarize findings in exploration and results of modeling 
    - well-labeled visualizations
    - link slides in README of your repository

## Guidance

### Acquisition + Preparation

- For this project, you will have to build a dataset yourself. Decide on a list
  of GitHub repositories to scrape, and use the provided script to acquire the README data for each repository. The repositories you use
  are up to you, but you should include at least 100 repositories in your data
  set.
- As an example of which repositories to use, here [is a link to GitHub's
  trending repositories][trending], the [most forked repositories][most-forked],
  and [the most starred repositories][most-starred].
- The list of repositories could be generated programatically using web scraping
  techniques.
- Make sure to document where your data comes from. All of the pages linked
  above change over time, so it would be wise to say something like: "Our data
  comes from the top 100 trending repositories on GitHub as of $DATE".

[acquire-script]: https://gist.github.com/zgulde/62dc5487475b182bfcfedfef16777476
[trending]: https://github.com/trending
[most-forked]: https://github.com/search?o=desc&q=stars:%3E1&s=forks&type=Repositories
[most-starred]: https://github.com/search?q=stars%3A%3E0&s=stars&type=Repositories

### Exploration

Explore and visualize the natural language data that you have acquired. Here are
some ideas for exploration:

- What are the most common words in READMEs?
- Does the length of the README vary by programming language?
- Do different programming languages use a different number of unique words?
- Are there any words that uniquely identify a programming language?

### Modeling

- Transform your documents into a form that can be used in a machine learning
  model. You should use the programming language of the repository as the label
  to predict.
- Try fitting several different models and using several different
  representations of the text (e.g. a simple bag of words, then also the TF-IDF
  values for each).
- Build a function that will take in the text of a README file and try to
  predict the programming language.
- If you have many different unique values in your target variable, consider
  narrowing down this list. For example, use the top 3 languages and then label
  everything else as "Other" so that you have fewer unique values to predict.

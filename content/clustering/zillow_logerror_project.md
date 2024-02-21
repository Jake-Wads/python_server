# Zillow: What is driving the errors in the Zestimates?

For this project you will continue working with the zillow dataset. Your target 
variable is now logerror.Continue to use the 2017 properties and predictions 
data for single unit / single family homes.

In addition to continuing work on your previous project, you should incorporate
clustering methodologies on this project.

Your audience for this project is a data science team. The presentation will
consist of a notebook demo of the discoveries you made and work you have done
related to uncovering what the drivers of the error in the zestimate are.

## Specification

You are expected to deliver a github repository with the following contents:

- A clearly named final notebook. This notebook will be what you present and
  should contain plenty of markdown documentation and cleaned up code.
- A README that explains what the project is, how to reproduce you work, and
  your notes from project planning.
- A Python module or modules that automate the data acquisistion and preparation
  process. These modules should be imported and used in your final notebook.

Further project requirements:

- Data Acquisition: Data is collected from the codeup cloud database with an
  appropriate SQL query
- Data Prep: Column data types are appropriate for the data they contain
- Data Prep: Missing values are investigated and handled
- Data Prep: Outliers are investigated and handled
- Exploration: the interaction between independent variables and the target
  variable is explored using visualization and statistical testing
- Exploration: Clustering is used to explore the data. A conclusion, supported
  by statistical testing and visualization, is drawn on whether or not the
  clusters are helpful/useful. At least 3 combinations of features for
  clustering should be tried.
- Modeling: At least 4 different models are created and their performance is
  compared. One model is the distinct combination of algorithm, hyperparameters,
  and features.
- Best practices on data splitting are followed
- The final notebook has a good title and the documentation within is
  sufficiently explanatory and of high quality
- Decisions and judment calls are made and explained/documented
- All python code is of high quality

## Guidance

- The data acquisition here can take some time. You should probably build out
  caching in your python scripts to store the data locally as a csv in order to
  speed up future data acquisition.
- Create sections indicated with markdown headings in your final notebook the
  same way you would create seperate slides for a presentation.
- For your MVP, do the easiest thing at each stage to move forward. Remember
  your MVP won't fulfill every detail of the project spec and it isn't a good
  use of your time to do this at first.
    - For example, for your mvp, decide not to deal with outliers and to simply
      drop all the null values
- Model on scaled data, explore on unscaled
- Clustering could be useful in several ways on this project:
    - Do clusters produce an interesting insight, takeaway, or visualization
      that can be shared and communicated?
    - With a small number of clusters, clusters could be one-hot encoded and
      used as a feature for modeling.
    - Different models can be created for different clusters (while conceptually
      simple, this involves a much more complicated python implementation, so
      you should probably treat this idea as a bonus)
- Sometimes your conclusion is that there is no effect or no significant
  difference. This is a valid conclusion in and of itself.
- You might wish to start working in a notebook or to split your work up into
  multiple notebooks. This is totally fine and makes sense so long as eventually
  you clean up and transfer the work to a final notebook and/or python scripts.



## Reminders

For the avoidance of doubt, the major goal for this project is to:

- Use clusters to help your exploration, understanding, and modeling of the data.

- The target variable you are trying to predict is logerror (b/c this is a regression problem since logerror is continuous)

- BUT if you use a cluster number as a feature, that cluster should _not_ have the target variable of logerror in it.

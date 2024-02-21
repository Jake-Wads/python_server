# Quit Your Wine-ing: What makes a high quality wine?

## Goal

Predict the quality of wine while incorporating unsupervised learning techniques.  


## Scenario

You are a data science consultant and have been tasked to **find drivers of wine quality** for the California Wine Institute. Your audience will be the **data science team** in charge of data driven consultation for winery supply chain marketing. They are most interested in seeing how **utilizing clusters** will affect a machine learning model. You will be delivering a **slide deck presentation** to share your findings. 


## Deliverables

1. New github repository
    - README.md
        - Project goal and description
        - Data dictionary
        - Project plan
        - Initial questions
        - Conclusion
        - How to reproduce your work
    - final_notebook.ipynb 
        - Notebook that runs from top to bottom
        - Clearly shows the pipeline process
            - Acquire
            - Prepare
            - Explore
            - Model
    - Python modules
        - wrangle.py OR acquire.py & prepare.py
2. Presentation
    - Slides
        - Introduction
        - Executive Summary
        - Findings
        - Conclusion
    - 5 minutes time limit




## Specification

**Overall**

- The final notebook has ample documentation that explains your process  
- Notebook and modules contain code comments
- Best practices on data splitting are followed

**Acquire**

- Data is collected from [Data.World Wine Quality Dataset](https://data.world/food/wine-quality)

**Prepare**

- The red and white csv's should be combined into a single column thats states if the wine is red or white
- Column data types are appropriate 
- Missing values are investigated and handled
- Outliers are investigated and handled

**Exploration**

- The interaction between independent variables and the target variable is explored using visualization and statistical testing
- Clustering is used to explore the data
    - Statistical testing and visualization is utilized to determine if the cluster is useful
    - A clear conclusion is drawn from the interactions 
    - At least 3 combinations of features for clustering should be tried
        - The clusters should also be compared to the target variable 
    
**Modeling** 

- At least 4 different models are created and their performance is compared
    - One model is the distinct combination of algorithm, hyperparameters, and features


## Guidance

- The data acquisition here can take some time. You should probably build out
  caching in your python scripts to store the data locally as a csv in order to
  speed up future data acquisition.
  
- For your MVP, do the easiest thing at each stage to move forward. 
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

- The target variable you are trying to predict is wine quality (you may decide whether you want to solve this with classification or regression)

- If you use a cluster number as a feature, that cluster should _NOT_ have the target variable of wine quality in it.

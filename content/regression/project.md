# Regression Project: Estimating Home Value

## Scenario

You are a junior data scientist on the Zillow data science team and receive the following email in your inbox:

> We want to be able to predict the property tax assessed values ('taxvaluedollarcnt') of **Single Family Properties** that had a transaction during 2017. 

> We have a model already, but we are hoping your insights can help us improve it. I need recommendations on a way to make a better model. Maybe you will create a new feature out of existing ones that works better, try a non-linear regression algorithm, or try to create a different model for each county. Whatever you find that works (or doesn't work) will be useful. Given you have just joined our team, we are excited to see your outside perspective. 

> One last thing, Maggie lost the email that told us where these properties were located. Ugh, Maggie :-/. Because property taxes are assessed at the county level, we would like to know what states and counties these are located in.

-- The Zillow Data Science Team

_____


## Business Goals

- Construct an ML Regression model that predicts propery tax assessed values ('taxvaluedollarcnt') of **Single Family Properties** using attributes of the properties. 

- Find the key drivers of property value for single family properties. Some questions that come to mind are: 
    - Why do some properties have a much higher value than others when they are located so close to each other? 
    - Why are some properties valued so differently from others when they have nearly the same physical attributes but only differ in location? 
    - Is having 1 bathroom worse for property value than having 2 bedrooms? 

- Deliver a report that the data science team can read through and replicate, understand what steps were taken, why and what the outcome was. 

- Make recommendations on what works or doesn't work in predicting these homes' values. 

___


## Project Objectives

- Document code, process (*data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation*), findings, and key takeaways in a jupyter notebook final report.

- Create modules (acquire.py, prepare.py) that make your process repeateable and your report (notebook) easier to read and follow. 

- Ask exploratory questions of your data that will help you understand more about the attributes and drivers of home value. Answer questions through charts and statistical tests.

- Construct a model to predict assessed home value for single family properties using regression techniques. 

- Make recommendations to a data science team about how to improve predictions. 

- Refine your work into a report, in the form of a jupyter notebook, that you will walk through in a 5 minute presentation to a group of collegues and managers. Communicate your goals, the work you did and why, what you found, your methodologies, and your conclusions. 

- Be prepared to answer panel questions about your code, process, findings, key takeaways, and model.

___


## Audience

Your customer/end user is the **Zillow Data Science Team**. In your deliverables, be sure to re-state your goals, as if you were delivering this to Zillow. They have asked for something from you, and you are basically communicating in a more concise way, and very clearly, the goals as you understand them and how you have acted upon them through your research.

____

## Deliverables

A. Github repo with:

 - a complete readme.md
 - acquire module (.py)
 - prepare module (.py)
 - a final report (.ipynb)
 - other supplemental artifacts created while working on the project (e.g. exploratory/modeling notebook(s)). 

B. Live 5 minute (max) presentation of your final notebook


### A. Github repo with the following:

1. **Readme (.md)**

    - Project goals
    
    - Project description
    
    - Project planning (lay out your process through the data science pipeline)

    - Initial hypotheses and/or questions you have of the data, ideas

    - Data dictionary

    - Instructions or an explanation of how someone else can reproduce your project and findings (What would someone need to be able to recreate your project on their own?)

    - Key findings, recommendations, and takeaways from your project. 
    
2. **Acquire & Prepare Modules (.py)**

    - Contains functions to acquire, prepare and split your data. You can have other .py files if you desire to abstract other code away from your final report. 
    
    - Each of your functions are accompanied by descriptive docstrings. If they are functions you borrowed from instructors, put those docstrings in your own words. 
    
    - Functions to acquire and prepare your data should be imported and used in your final report. 
    
    - Your work must be reproducible by someone with their own `env.py` file. 

3. **Final Report (.ipynb)** 

    - A **Report** that has filtered out all the extraneous elements not necessary to include in the report. 
    
    - Use markdown throughout the notebook to guide the audience. Assume the reader will not read your code blocks as you think about how much markdown guidance do you need. 

    - Then, assume another reader will read ALL of your code, so make sure it is clearly commented. All cells with code need comments. 

    - Your notebook should begin with a project overview and goals

    - Exploration should be refined in the report because now you know which visualizations and tests led to valuable outcomes. 

    - Include at least 4 visualizations in the form of: 

        1. Question *in markdown* that you want to answer 

        2. Visualization 

        3. Statistical test (in at least 2 of your 4) 

        4. Provide your clear answer or takeaway *in markdown and natural language* to the question based on your exploration.  

    - Provide the context of the target variable through a visualization (distribution of the values, e.g.)

    - Include your 3 best models in the final notebook to review. Show the steps and code you went through to fit the models, evaluate, and select. 

    - On your best model, a chart visualizing how it performed on test would be valuable. 
    
    - End with a conclusion that talks about your original goals and how you reached those (or didn't), the key findings, recommendations and next steps ("If I had more time, I would...")
    
4. Additional non-final notebooks (.ipynb) may be created while working on the project, containing exploration, other work, or  modeling work, but they will not be graded. All required elements must be in the final report notebook. 
     

### B. Live Presentation

- A **live presentation** where you deliver the **final report** (.ipynb) and walk through it with the audience. 

- You have a time limit of 5 minutes to present. 

- *If have content that you intend to skip in your presentation, it should not be included in your report, like scrolls and scrolls of visualizations.* Remember, this is a different artifact from the notebook you worked on that contains all your work. This serves a purpose of conveying information to others. And you will use it to give an overview of your project by walking through the main steps - what cleaning did you do and why, what insights did you find in exploration, what are 3 models you developed, how did the differ, and how did they compare in terms of performance? What was the best model and how do you expect it to perform in production on data it's never seen? And finally, wrap it all up in a conclusion. (5 minutes max)

- You should be prepared to answer follow-up questions about your code, process, tests, model, and findings.

- You will have created multiple notebooks in your work. Do not be concerned about not showing all your work in your report. That is not intended. We can look back to see the work that led to your final notebook. But we want you to feel comfortable creating a report from your work that gives brief insight into the findings and how you got those findings. This is the first step in learning to deliver a report that is abstracted away from all the details. It takes practice to feel comfortable not showing everything. It will get easier the more you practice. 

    
<hr style="border-top: 10px groove dodgerblue; margin-top: 1px; margin-bottom: 1px"></hr>

## Project Guidance

- Read the rubric for the project before beginning. 

- Reread your feedback/rubric from the classification project and any notes you took from feedback. 

- You are asked to use **properties that had a transaction** in 2017! You must figure out how to determine which properties those are and filter your data IN SQL before bringing it into your Python environment.
    - You will need to use the **properties_2017**, **predictions_2017**, and **propertylandusetype** tables. 

- For the first iteration of your model, use only square feet of the home, number of bedrooms, and number of bathrooms to estimate the property's assessed value, `taxvaluedollarcnt`. You can expand this to other fields after you have completed an MVP (minimally viable product).

- Be sure and remove the fields that leak information about `taxvaluedollarcnt`. These are fields we would not know until we knew the assessed value, so using them would be "cheating". These fields are `landtaxvaluedollarcnt`, `structuretaxvaluedollarcnt`, and `taxamount`. 

- You will want to do some data validation or QA (quality assurance) to be sure the data you gather is what you think it is.

- You will want to make sure you are using the best fields to represent square feet of home, number of bedrooms, and number of bathrooms. "Best" meaning the most accurate and available information. Here you will need to do some data investigation in the database and use your domain expertise to make some judgement calls.

- You will want to read and re-read the requirements given by your stakeholders to be sure you are meeting all of their needs and representing it in your data, report, and model.

___

## Data Science Pipeline Guidance

We highly recommend you re-read the data science pipeline lesson to refresh your memory on the purpose of each stage in the pipeline and how to get there. 

[https://ds.codeup.com/fundamentals/data-science-pipeline/](https://ds.codeup.com/fundamentals/data-science-pipeline/)


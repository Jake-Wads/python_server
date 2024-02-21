# Classification Project

<hr style="border-top: 10px groove limegreen; margin-top: 1px; margin-bottom: 1px"></hr>


## Business Goals

- Find drivers for customer churn at Telco. Why are customers churning?

- Construct a ML classification model that accurately predicts customer churn

- Present your process and findings to the lead data scientist

___



## Project Objectives

- Refine your work into a final report, in the form of a jupyter notebook, that shows the work you did, why, goals, what you found, your methodologies, and your conclusions

- Document code, process (*data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation*), findings, and key takeaways in your report (notebook)

- Create modules (acquire.py, prepare.py) that make your process repeateable and your report (notebook) easy to read and follow

- Ask exploratory questions of your data that will help you understand more about the attributes and drivers of customers churning (answer questions through charts and statistical tests)

- Construct a model to predict customer churn using classification techniques, and make predictions for a group of customers 

- Walk through your report (notebook) in a 5 minute presentation with the lead data scientist

- Be prepared to answer panel questions about your code, process, findings and key takeaways, and model

___


## Audience

- Your target audience for your notebook walkthrough is your lead data scientist. This should guide your language and level of explanations in your walkthrough.

___


## Deliverables


### Github repo with the following:

1. **Readme (.md)**

    - project description with goals

    - initial hypotheses and/or questions you have of the data, ideas

    - data dictionary

    - project planning (lay out your process through the data science pipeline)

    - instructions or an explanation of how someone else can reproduce your project and findings (What would someone need to be able to recreate your project on their own?)

    - key findings, recommendations, and takeaways from your project 

2. **Final Report (.ipynb)**

    - A **Report** that has filtered out all the extraneous elements not necessary to include in the report. 

    - Use markdown throughout the notebook to guide the audience. Assume the reader will not read your code blocks as you think about how much markdown guidance do you need. 

    - Then, assume another reader will read ALL of your code, so make sure it is very very clearly commented. All cells with code need comments. 

    - Your notebook should begin with a project overview and goals
    
    - Preparation should specifically call out any ways you changed the data (like handling nulls)

    - Provide the context of the target variable through a visualization (distribution of the values, e.g.)

    - Exploration should be refined in the report because now you know which visualizations and tests led to valuable outcomes. 

    - Include at least 4 visualizations in the form of: 

        1. Question *in markdown* that you want to answer 

        2. Visualization 

        3. Statistical test (in at least 2 of your 4) 

        4. Provide your clear answer or takeaway *in markdown and natural language* to the question based on your exploration  

    - Include your 3 best models in the final notebook to review. Show the steps and code you went through to fit the models, evaluate, and select. 

    - On your best model, a chart visualizing how it performed on test would be valuable. 
    
    - End with a conclusion that talks about your original goals and how you reached those (or didn't), the key findings, recommendations and next steps ("If I had more time, I would...")

3. **Acquire & Prepare Modules (.py)**

    - contains functions to acquire, prepare and split your data. You can have other .py files if you desire to abstract other code away from your final report. 
    
    - Your work must be reproducible by someone with their own `env.py` file. 
    
    - Each of your functions are complimented with docstrings. If they are functions you borrowed from instructors, put those docstrings in your own words. 
    
    - Functions to acquire and prepare your data should be imported and used in your final report. 

4. **Predictions (.csv)**. 

    - 3 columns: customer_id, probability of churn, and prediction of churn. (1=churn, 0=not_churn). 
    
    - These predictions should be from your best performing model ran on `X_test`. 
    
    - Note that the order of the `y_pred` and `y_proba` are numpy arrays coming from running the model on `X_test`. The order of those values will match the order of the rows in `X_test`, so you can obtain the customer_id from `X_test` and concatenate these values together into a dataframe to write to CSV.

5. **non-final Notebook(s) (.ipynb)** 

     - there should be at least 1 non-final notebook
     
     - these were created while working on the project, containing exploration & modeling work (and other work), not shown in the final report
          
___


### Live Presentation

- A **live presentation** where you deliver the **final report** (.ipynb) (your jupyter notebook) and walk through it with the audience. 

- *If have content that you intend to skip in your presentation, it should not be included in your report, like scrolls and scrolls of visualizations.* Remember, this is a different artifact from the notebook you worked on that contains all your work. This serves a purpose of conveying information to others. And you will use it to give an overview of your project by walking through the main steps (what cleaning did you do and why, what insights did you find in exploration, what are 3 models you developed, how did the differ, and how did they compare in terms of performance? What was the best model and how do you expect it to perform in production on data it's never seen? And finally, wrap it all up in a conclusion. (5 minutes max). *You should be prepared to answer follow-up questions about your code, process, tests, model, and findings.*

- You will have created multiple notebooks in your work. Do not be concerned about not showing all your work in your report. That is not intended. We can look back to see the work that let to your final notebook. But we want you to feel comfortable creating a report from your work that gives brief insight into the findings and how you got those findings. This is the first step of you practicing delivering a report that is abstracted away from all the details. It takes practice to feel comfortable not showing everything. It will get easier the more you practice. 

___

## Tips

**Sample questions**

- Are customers with DSL more or less likely to churn? 
- What month are customers most likely to churn and does that depend on their contract type? 
- Is there a service that is associated with more churn than expected? 
- Do customers who churn have a higher average monthly spend than those who don't? 

**Making recommendations**

Recommendations should be feasible. If you find that month-to-month customers churn more, we won't be surprised, but Telco is not getting rid of that plan. The fact that customers churn is not because they can; it's because they can *and* they are motivated to do so. We want your insights into *why* they are motivated to do so. We realize you will not be able to do a full causal experiment, but we would like to see some solid evidence of your conclusions.

**The pipeline**

To step through each step in the pipeline, refer to the lessons in classification. This project is intended to pull together what you have done in this module. So use those resources. If you need a refresher on the pipeline and the goals in each stage, refer to the lesson in fundamentals: [Data Science Pipeline](https://ds.codeup.com/fundamentals/data-science-pipeline/). 

**Data Prep**

Prepare your data within the notebook first. Line by line, testing the functionality. Then define the function (with docstrings, of course), in the notebook. Run the function, in the notebook. Make sure it works as expected before sending it to the prepare.py module. If you run into errors later, bring it back into the notebook and work backwards...take it out of the function, then run it. Still issues, take out line by line to find where the error is. Don't put it back into the prepare.py until you know it is working! And remember, restart your kernel before trying again!

**Time management**

The hardest part of this first DS project is time management. *Don't skip planning*. And in planning, write the questions you intend to answer in exploration. This is where you can fall down the rabbit hole (exploration + coming up with new features). Complete an MVP before diving deeper. So write questions to answer before you even touch code. When you get to exploration, answer only those questions first, limit the time you allow yourself to create new features. Answer the minimum of 4 questions, create viz's, run tests, then move on. Fit 3 models with train, predict and evaluate with train. Evaluate with validate, select the best, and then evaluate on test. Make a copy of the notebook. 

One will become your report. Add the markdown at the top of the report (intro, project overview, goals, etc.), add the markdown of what you are doing to prepare the data, make sure the exploration is well documented where you can walk through each question, viz/test, and answer individually. Add a summary of your exploration findings to the end of your explore section. Enhance the markdown around your modeling stage. Which eval metric did you use and why? Which performed the best and why? Add a visual of your best model showing how it performed. Add a solid conclusion with how you achieved the goals, key takeaways, next steps, how you expect the predictions you made on the customers (in the csv) to perform, and recommendations to help reduct churn and improve customer retention. 

Once you have finished all that and made sure your code is commented and all deliverables are ready to go, then you can go back (in your original working notebook...NOT your report), and do more exploration or modeling! If you find something you want to add before you deliver it, cool. If you don't, no problem because you already have an MVP, Minimally Viable Product! 

___

## Templates

A sample project with full repo and analysis report:

[Chess Upsets Example Project](https://github.com/Johndsalas/chess_upsets_example_project)

For a basic template to follow in your final report:

[Analysis Report Template](https://github.com/Johndsalas/lesson_prep/blob/main/project_template.ipynb)
# Individual Projects

* What? Codeup students will work on individual data science projects that touch the full DS pipeline.
* Why? Based on instructor's judgement and employer feedback from Codeup's annual technical advisory board. This time is meant to address feedback that Codeup alumni's portfolios tend to look similar and re-enforce skills in time management and completing end to end data science projects.

## Deliverables

* Github Repo w/ Final Notebook and README
* Project summary and writeup for your resume or other professional portfolio pieces

## Timeline

| Day | Goal                                                 |
| --- | ---                                                  |
| 1   | Project Planning, Data Wrangling, Exploration        |
| 2   | Exploration Wrap up, Modeling, Project Delivery Prep |
| 3   | MVP Iteration, Project Writeup                       |
| 4   | Peer Review                                          |

## Day 1

For day 1 you should spend your morning selecting a dataset, planning the
project, and starting to acquire and prepare your data. In the afternoon you
should wrap up your initial data prep and start exploration.

1. 1 Hour - Select a dataset / project to work on

    You might wish to explore several datasets and even start looking (briefly) at the data to see what kinds of questions you might be able to answer.

    Recommended sources are in the [Codeup appendix](https://ds.codeup.com/appendix/open_data/), Kaggle, or data.world.

    At this point you should have a rough idea of what the goal of the project will be.

2. 1 Hour - Project Planning

    - Define your target.
    - Outline your goals and define deliverables.
    - Document initial thoughts and hypotheses.
    - Create a Trello board where you document what those deliverables are and the steps you will take to get there.

3. 2 hours - Data Acquired and Prepped

    Get your data into a state such that it can be explored and modeled. You should try to make decisions that enable you to move forward rapidly. For example, right now, simply drop all the null values as opposed to trying to fill them in a fancy way. You can always revisit this stage later.

4. 2.5 hours - Initial EDA

    Explore variable interactions through visualizations. For your MVP you should visualize how the predictors interact with your target. Make sure to document your takeaways, insights, and further questions.


## Day 2

1. 1 hour - Summarize your findings, perform next steps indicated from exploration, and wrap up any work needed prior to modeling.

2. 2 hours - Modeling

    Here you should establish a baseline and try out several different models. Compare model performance, select your best model, and see how it performs on unseen data. Visualize the performance of your model where applicable.

3. 2.5 hours - Iteration 2

    What are changes, new features, or other questions you would like to address to increase your findings or improve your performance? Use this time go back through your pipeline adding a few of those ideas along the way.

4. 1 hour - Prepare to deliver

    - Clean up your work and organize the key details in a single notebook.
    - Make sure your helper files are available and being used.
    - Ensure your readme is akin to an "abstract" of a research paper.
    - Ensure you have all the necessary elements required from the project spec and the basics from any project (project planning, data dictionary, Trello, readme, how to reproduce, etc.).
    - Make sure you have a solid conclusion in your final notebook. Include next steps, learnings, and recommendations.

## Day 3

- Further MVP Iteration

    What this time looks like is going to vary depending on what you are working on individually.

    In general, you should revisit your MVP and improve the individual pipeline sections using what you learned the previous day. It is important to finish an end-to-end MVP before going back and iterating because going through the entire pipeline can inform you of where it will be valuable to spend more of your time.

- Project Summary/Write-up

    You should prepare a brief writeup of your own project that can be added to your resume / LinkedIn.

## Day 4

Peer Review

- Each person will review 2 other students' notebooks and work completed.
- As a reviewer, you will make comments on what you see that works, what doesn't work, and where you see room for improvement. These topics can vary from style of code to implementation, to discoveries or questions asked and answered in exploration.
- Did you find the student met the goal? Are the key drivers clearly stated?  Where would you make improvements?

## Additional Guidance

- At the start of day 2, consider any takeaways from Initial EDA that lead to action, for example, creating new variables.

    Make sure those takeaways are clearly documented; it should only take a few minutes to add the documentation. Go back to pre-processing and add that feature(s) (so that is it scaled, split, etc as all others).

- Before going into modeling, run through some data validation (QA/QC) of all of your final dataframes.

    Look at counts of rows/columns, are they what you would expect? Take a single observation and follow it from the initial import through the last stage. Any errors in numbers, values? Are all X variables numeric? Is the target, y-variable, of the datatype your problem calls for? For example, if you are running linear regression, is your datatype of a numeric type? Are all numeric independent variables of the dataframe you will be modeling scaled?

### Exploration

- **Univariate exploration**: Explore feature variable individually.

    For numeric variables, create a histogram and use `.describe()`. For categorical variables, use a frequency table and a bar plot of that frequency table.

- **Bivariate exploration**: Plot each variable against your target.

    For a categorical target variable, your target can be on the x-axis, and numeric variables on the y. For testing, you can compare your categorical target to numeric variables using comparison of means tests, such as t-test, anova or mann-whitney. You can compare your categorical target to categorical variables using a chi-square test.

    For a numeric target variable, your target can be on the y-axis, and independent variables on the x-axis. For independent variables that are numeric, scatterplots are useful. For independent variables that are categorical or discrete, bar plots, swarm plots or violin plots are useful.

- **Multivariate exploration**: Visualize multiple (3+) variables at once.

    With a categorical target, plot each categorical variable (x-axis) against each numeric variable (y-axis) and set color to your categorical target variable.  You could use a bar plot, swarm plot, violin plot, box plot.

    When plotting a numeric target against categorical independent variables, your y-axis is the target and your x-axis is categorical variables (bar, swarm, violin, box plots). You can set color to be another one of the categorical variables. One you are most interested in, for example.

- When plotting a numeric target against numeric independent variables, your y-axis should be your target and your x-axis should be a numeric independent variable. Color can be added from one of the categorical variables to add a dimension.

- Document any findings, insights, thoughts, takeaways from the charts and statistics you produced. In that, be sure and include any additional features you would like to develop if there is time, which features need to be removed, and which are free to move forward.

# Regression Project Rubric

## Overall

### Planning

1. Data dictionary included
2. Hypotheses stated
3. Project summary and goals stated
4. Project plan scoped 

### Acquire

1. acquire.py or wrangle.py exists
2. data acquisition can be replicated through function
3. data is acquired from mySQL database
4. env.py file is referenced
5. data is summarized after acquisition
6. Notebook contains text (code comments & markdown) that explains what is happening. 

### Prep

1. prep.py or wrangle.py exists
2. Notebook contains text (code comments & markdown) that explains what is happening. 
3. Missing values are handled
4. Support is given for why missing values are handled the way they are
5. Distributions are plotted
6. data prep is reproducible
7. Notebook contains text (code comments & markdown) that explains what is happening. 
8. Functions in .py files are commented

### Split

1. Function to split exists in either split_scale.py or prep.py or wrangle.py
2. Data is split into train and test set 
3. Reasonable proportions given to train/test (60-90%)/(10-40%)
4. Seed is set through random_state for reproducibility
5. Split is done prior to scaling and exploration
6. Notebook contains text (code comments & markdown) that explains what is happening. 
7. Functions in .py files are commented

### Scale

1. Function to scale exists in either split_scale.py or prep.py or wrangle.py
2. Numeric data is scaled
3. Scaler is fit on train, and transformed on train and test
4. Notebook contains text (code comments & markdown) that explains what is happening. 
5. Functions in .py files are commented

### Explore

1. hypotheses stated
2. statistical tests run (correlation, t-test, chi-sq, e.g.)
3. variable relationships visualized
4. takeaways/conclusions documented, drivers identified
5. Notebook contains text (code comments & markdown) that explains what is happening. 
6. Counties being studied are determined and communicated
7. distributions of tax rates are plotted

### Preprocessing

1. Features.py or preprocessing.py exists (bonus) (but min expectation is it's done in notebook). 
2. code for turning variables into features exists
3. turning variables into features is reproducible
4. random state is set where applicable
5. functions are commented and defined/notebook contains comments & text

### Modeling

1. Baseline performance of using no independent variables is measured
2. 2+ regression models fitted and predicted on train
3. random state set where applicable
4. all results are evaluated and compared, using training dataset!
5. clear communication why final model is the selected one
6. model.py exists
7. evaluation functions exist in model.py or evaluate.py module
8. regression: plot evaluation, residuals

### Presentation

1. chart content/types:	chart types appropriate (ideal setting (e.g. no tables/heatmaps), type is idea for data types (e.g. continuous x != barchart!), context included (multiple charts presented together when useful to compare, baseline numbers present of data used, etc.), no misleading viz/communication around causation/etc.,
2. slide & chart formatting: titles useful, of what the audience should take away from the chart or slide (not 'x by y', e.g.), axes are labeled, units are labeled ($, %, e.g.) and in correct unit (not scaled, e.g.) for presentations, numbers of in ideal precision level, use of color is ideal (not too many, only used to make a point/draw a distinction, gradient for continuous & distinct for categorical, e.g.), font and font size appropriate, no obvious spelling/grammar errors
3. slides included: title, intro, conclusion, executive summary, distribution of tax rate per county, the counties included, and key drivers
4. presentation: intro made with goals, overview / conclusion made with takeaways, next steps, recommendations, limitations / charts are talked through
5. presentation: volume, speed of talk, flow, professionalism, slides are not read, level of technicality appropriate for audience & setting
# Data Science Virtual Classroom & Grading

*Google Classroom will be abbreviated using **GC** in this document*

## Create a class

1. Be sure you are a member as an instructor of the [Template class in GC](https://classroom.google.com/u/0/c/NDI4OTA2OTk3Nzda), class code: 2bit2z.  
2. Go to the [GC home page](https://classroom.google.com) where you see the list of classes. You can also get there within the app by going to the menu in the top left and selecting "Classes".  
3. On the Template Class card, click on the menu dots in the top right, and select "copy".  The class name should be the name of the cohort.
4. Upload new syllabus, specific to the cohort.  
    - Update "Attendance" dates in the assignment depending on the grading period.  
5. Progress Report:   
    - Update "Progress Report" dates scheduled to "assign" at 8:00 AM on the last of the grading period, and the "due date" to be the the next class day (no due time).
5. Confirm all assignments delivered via google forms are accessible by students.
4. *insert things to do to adapt assignments, materials, etc. for the new class...I will walk through this once the template is completed*  


## Grading

### Attendance 

Update the attendance grades referencing the [Codeup Master DataScience Attendance](https://docs.google.com/spreadsheets/d/1uD5n69jjdqISvasJvmoH5SLZKsCXdrBybB4S76BZxag/edit?usp=sharing)  

### Progress Report

- This is the grade averaged under "Grades" tab for each student across all the assignments.    
- It is weighted in class settings based on the type of assignment (exercises, quizzes, assignments/projects, attendance)    

### Pre-work

- Python pre-work was graded by Ryan for Bayes. *need details as to how it was graded*.  The grades were manually entered into the GC assignment. 

### Fundamentals

- Exercises: graded based on completion.    
    - Each assignment will be submitted through GC; therefore, 100 for each student with the assignment "turned in".     
    - Add the form responses to "Skills in Demand" assignments (will be one google sheet document) and "Data Science Community" assignment (another google sheet) as "material" under the "Class Materials" topic header.   
- Quiz: taken through a quiz form and will be graded based on the quiz template upon completion.   
    - Verify the grading of the 2 questions that require short answers (acronym for NLP and HDFS).  
    - If they are correct but weren't captured as correct, add the answer as another option in the quiz grading template.     
- Assessment (Project):  The Path Toward Data Science
    - Students will submit the link to a Google Slides document.   
    - This is graded using fundamentals-project-rubric.md  
    - Grade is manually entered into GC.  
    
### Excel & Storytelling  

- Exercises: Grade based on completion.  
    - Excel:  When the "Excel Exercises" assignment is posted/assigned with the excel workbook template attached (the one the students will work off of), GC will create a new directory with the name of the assignment and in the directory will be a workbook named for each student. The students are unaware this is happening, but they will see the document renamed (with their name appended to the original name) when they download it to work on it. The key is for them to keep that name...do NOT rename the document! When they submit the document it will replace the one that originally appeared in that directory with their name appended to the document name.   
    - Storytelling: Google slides submitted through assignment in GC.  
- Assessment (Project): storytelling-project-rubric.md *update rubric with info from Bayes Grades workbook*


### SQL  

- Exercises: graded through the grading/check_exercises.py script:  
    ```python check_exercises.py -p database-exercises -c *cohort_name* --format csv
    ```  

- Quiz:  grading/assessments/sql.md *create in google forms* will be taken through a quiz form. Quiz will be grade upon completion. Verify the short answers


### Python 

- Exercises: graded through the check_exercises.py script:  
    ```python
    python check_exercises.py -p python-exercises -c *cohort_name* --format csv
    ```    

- Project (Quiz Grade): link to github submitted into GC assignment.  *how graded?*  

- Assessment: grading/assessments/python.txt 
    - solutions.py will be submitted to the GC assignment.   

### Stats

- Exercises  
    - Probability Distributions
    - Hypothesis testing-overview
    - Hypothesis testing-t-test
    - Hypothesis testing-correlation
    - Hypothesis testing-chi-squared
    - Hypothesis testing-more statistical testing
    - Power analysis

- Quiz

- Assessment: grading/assessments/statistics.md


### Regression

- Assessment (Project): grading/regression-project-rubric.md  


### Classification

- Assessment (Project): grading/classification-project-rubric.md

### Clustering

- Assessment (Project): grading/clustering-project-rubric.md

### Time Series Analysis

- Assessment (Project): grading/time-series-project-rubric.md

### Anomaly Detection

### NLP

- Assessment (Project): grading/nlp-project-rubric.md


### Spark

### 

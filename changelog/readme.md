#### Changelog:
 - This tool will capture commits to the data-science-curriculum repository.
 - [The changelog sheet lives here.](https://docs.google.com/spreadsheets/d/1Z7JfIgb498rZlC7a8VSNGQZhMkyhJJ6-Qk1MwvDZcII/edit?usp=sharing)
 - In order to optimize the value of the commits and make the content searchable and legible for instructors, please follow the following style guide* (*proposed suggestion, pending team agreement)

  - *[Change Type] - [Subject Area/Module] - [Comment]*
  - *Change Types*:
    - Content Change, Exercise Change, Tool Change, Copy Edit..
  - *Subject Area/Module*:
    - Regression:Modeling, Spark:API, Python:Intro, Handouts, Tools, etc.
  - *Comment*:
    - What was done: "changed exercise set, question #4," "changed subject of lesson paragraph to focus on matplotlib axes," "Updated exercise set entirely," etc.

 - Example: 
 ```
 git commit -m "Exercise Change - Regression:Modeling - changed subject of lesson paragraph to focus on matplotlib axes"
 ```

 ### To run:
  - Requirements: 
  ```
  **Gitpython**: pythonic interaction with Git: pip install GitPython
  ```
  ```
  **gspread**: interaction with google sheets API: pip install gspread
  ```
  ```
  **gspread_dataframe**: convert pandas to google sheets:  pip install gspread-dataframe
  ```
import pandas as pd
  1. Get google sheets credentials
```
    Create a project from google cloud dashboard
    Enable google sheets and google drive APIs
    Generate oauth credentials
```
  1. Run gsheets_init.py, sign in with your @codeup account and authorize.
  1. Move the downloaded file to ~/.config/gspread/credentials.json.
 
 In the appropriate folder (here):
 ```
 python changelog.py
 ```
# requirements outside of regular specs:
# Gitpython: pythonic interaction with Git: pip install GitPython
# gspread: interaction with google sheets API: pip install gspread
# gspread_dataframe: convert pandas to google sheets:  pip install gspread-dataframe
import pandas as pd
import gspread
import git
from gspread_dataframe import set_with_dataframe

# Utilize GitPython to grab the current repo
# this presumes locational structure within the current repo if you
# have this pulled down appropriately.
repo = git.Repo('..')

# iter_commits grabs the current list of commits
commit_list = list(repo.iter_commits())

# initialize an empty list, grab the commits,
# pull out the metadata desired from them, 
# plop that biz into a dataframe.
log_deets = []
for commit in commit_list:
    commit_info = {
        'author': str(commit.author),
        'author_email': str(commit.author.email),
        'commit_time': str(commit.committed_datetime),
        'commit_message': commit.message
    }
    log_deets.append(commit_info)

log_deets = pd.DataFrame(log_deets)

# establish an authorized connection to google sheets
# **see stipulations on obtaining cretentials from the wiki!!**
gc = gspread.oauth()

# open the appropriate workbook
sh = gc.open('curriculum_changelog')
# establish the appropriate worksheet
worksheet = sh.worksheet('changelog')
# put that dataframe up into that sheet
set_with_dataframe(worksheet, log_deets, include_index=True)
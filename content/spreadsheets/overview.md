# Introduction to Spreadsheets

## Use Cases

- You need to deliver a dataset and/or report specifically in spreadsheet format (Excel, Google Sheets, e.g.).
- Someone wants to see your analysis and be able to explore the data themselves, and they need to use Excel or Google Sheets to do so.
- You are working on a report that is going to be done in Powerpoint/Google Slides and the data that creates the charts and tables need to accompany it.
- You are working on a collaborative presentation or report and the others are using Excel or Google Sheets to create the charts and reference the data.
- You receive a workbook in Excel or Google Sheets and need to take a look at it, make changes, and deliver back to original author.
- You have a small dataset and need to answer a quick, one-time question.

## Limitations of Spreadsheets

- Limitations in amount of data, e.g. Excel is limited to 16,384 Columns & 1,048,576 million rows.
- Excel use a lot of RAM!
- Time Consuming: manually entering data, not simple to automate basic tasks.
- Security issues, e.g. viruses are often attached to Excel files that can be executed through macros.
- Limited types of charts and data must fit into the existing frameworks and formats of the charts available.
- Analyzing data: As the data grows and emerge over time the analysis must be re-run.
- Analyzing data: The data and the formulas are not consistently updated often leading to bad results and decisions.
- Achieving reproducibility is almost impossible.
- Excel & Google Sheets mix the data with the code, leading to duplicate effort in running same code on different data.
- There is no way to modularize the code.
- It is difficult to see what's going on the background, hard to see which cells are formula vs. raw data.
- Hard to debug: no error messages, or a few with no specifics.
- Easy to mess up your data permanently without realizing it.
- Version control and collaboration is difficult

## Benefits of Spreadsheets

- Small learning curve
- Good for organizing point in time data to deliver to others to explore who don't have experience with programming or SQL
- Faster for some applications where you know the maximal scope of the project is going to be small. You have a well defined upper bound on the complexity of the problem. Although that is rarely the case... even when it is claimed to be in the beginning.

## Skills Covered in Prework

- Entering data
- Worksheet structure
- Entering a formula
- Copy and paste: CTRL-C/CTRL-V, fill handle
- Relative reference in functions
- Formatting: cells, font, alignment, data formats, borders, copy and paste formats with format painter.
- Filtering and sorting data
- Insert/delete rows and columns
- Auto-sum, average, count...
- Functions: `SUM(), *, +, IF(), VLOOKUP()`
- Insert Table, name the table, add totals
- Remove duplicates
- Pivot Table
- Create a chart

## Exercises

1. Read through [Data Organization in Spreadsheets](https://www.tandfonline.com/doi/full/10.1080/00031305.2017.1375989) for spreadsheet best practices.
1. Create a copy of the google sheet provided in the google classroom.
1. Create a new worksheet and copy the tips dataset into it. The code sample below will put the dataset on your clipboard so that you can paste it into google sheets.

    ```python
    import seaborn as sns

    df = sns.load_dataset('tips')
    df.to_clipboard()
    ```

1. Add a `tip_percentage` column to the tips worksheet. Tip percentage is the tip amount divided by the total bill.
1. Add a cost per person column to the tips worksheet. This is the total bill divided by the party size.

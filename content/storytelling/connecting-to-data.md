# Connecting to Data

Tableau can connect to a broad range of data storage systems, softwares and file types. Tableau Public limits the connections, but the most common are available and should satisfy most of what you want to do. The first step in building a visualization in tableau is connecting to the data. Tableau offers flexibility in how you connect (maintain a live connection vs. create a data extract), in the data types that can be read, as well as in the merging of multiple data sources and datasets. Upon opening the Tableau app (and not a workbook), you will start on the connection page. We will spend this lesson here and on the *Data Source* tab, which you will see after completing a connection.


**Lesson Goals**

- Know where to get help
- Connect to a data source
- Filter your data
- Prepare your data

_______________________________________________

## Primary Types of Data Sources

**Local Files**

- Excel: .xls, .xlsx
- Text: .csv, .txt, .tsv, .tab
- JSON Files: .json
- PDF Files: .pdf
- Spatial Files: Esri File Geodatabases (gdb*.zip), Esri Shapefiles (.shp), MapInfo Tables (.tab), MapInfo Interchange Format (.mif), GeoJSON (.geojson), TopoJSON (.json, .topojson), KML (.kml)
- Statistical Files: SAS (.sas7bdat), SPSS (.sav), R (.rda, .rdata)

**Servers**

- Google Sheets
- OData: mysql database server, e.g.
- Web data connector

**Other data connectors** (not available in Tableau Public)

- [Other Data Sources](https://www.tableau.com/products/desktop?_ga=2.168784937.943005315.1582736711-305547270.1582736711&_fsi=g1y4KoAD#data-sources)

_______________________________________________

## Connection Method: Live vs. Data Extract

> "Tableau Data Extracts are snapshots of data optimized for aggregation and loaded into system memory to be quickly recalled for visualization. Extracts tend to be much faster than live connections, especially in more complex visualizations with large data sets, filters, calculations, etc."
(Medrano, 2016). If data is being updated regularly, refreshing the extract is necessary in order to stay up to date with the most recent data.On the other hand, live connections will provide real-time updates and those changes will be reflected in your visualizations, with any changes in the data source reflected in Tableau. While extracts are always optimized for performance, the databases you may access may not be.  That is to say that With live connections, your queries will only perform as well as the database can. Generally, you will be using extracts. When you publish a dashboard that needs real-time updates (which is the small minority of the time), you may decide to use a live connection. However, even in those cases, when building the visualizations on your desktop, you will likely use an extract. All of that said, with Tableau Public, you do not have the option to create a data extract.

_______________________________________________

## Connect to a File

- When connecting to a file, select the file type, navigate to the file you wish to connect to in your directory, and *open*.
- On the left side, you will see Connections, Files & New Union. Also, listed under *Files*, you will also see any other files in your current working directory that can be read by tableau.
- In the main section, you will see a sample (1,000 rows default) of the file you have connected to. Think about this sample size like running a SQL query that limits your results to 1,000. You can increase that number, and it will also increase the time required to load the data into view. You really just want a sample large enough to understand the data that is contained in each field.
For this lesson, we will connect to cc_institution_details.csv.

_______________________________________________

## Join Files

**Join Columns**
You can connect and merge multiple data sources, such as multiple files or spreadsheets. Tableau joins are similar to joining tables in a mySQL database. You can do an inner, left, right, or full outer join. A box will display asking for the field(s) to join on.
For this lesson, we will add a new connection to the file, merged_2013_PP.csv.

**Union Rows**
You can append rows from 2 sources if your columns map to each other.

_______________________________________________

## Filter Data

In this section, we will be focused on the filter option box. You can get there by looking in the top right of the *Data Source* page. There you can add a filter.

Let's work through an example. Say we want to add a new filter to keep only 4 year universities.

1. To do this, we will add a filter to the *Level* field.
2. Filter (in top right) -> Add -> Add... -> Select field *Level* -> ...
3. Set the criteria.

**General & Wildcard Filters**

There are many ways to identify the criteria for your filters. Under the **General** tab, you have ways to set criteria for exact matches to values in the *Level* field. Under the **Wildcard** tab, you can set criteria for wildcard string matching. We will look at the Condition tab in our next example. For now, let's filter to include only 4-year institutions.

**Conditional Filters**

For the next example, we will filter states. Add a new filter, and select *State* as the field. Under the **Condition** tab, let's add a condition 'By field'. Let's say we want to only include states which have a median *Student Count* of less than 1,000. We will select 'By field' and fill in the parameters to say *Student Count* Median $<$ 1000. You should end with only Florida and Utah remaining. What you have done is filter out *States*. You have not filtered out schools that have a *Student Count* > 1000. To test this, complete your filter by selecting OK. You should have 206 rows remaining. Now, go back to your filters, edit the existing filter to not filter by a condition, but instead filter by name of state. Include only Florida and Utah. You will see you end up with the same number of observations.

**'Top' Filters**

Similar to Conditional filtering, you can filter the states by ranking in any of the columns. For example, say you want to explore colleges that are in the top 10 states in terms of *Median SAT Value*. You would filter *State* by going to the **Top** tab, and then filter Top 10 by *Median SAT Value* followed by your aggregate method, such as average. Note: Median SAT Value is the median SAT value for that school. When we are aggregating by average, we are taking the average of all of the colleges' *Median SAT Value* in that state. Then Tableau ranks those averages and returns the top 10 states.

_______________________________________________

## Prepare Data

In this section, we will be focused on the table containing a sample view of our data. Each column header has 3 groups of activities contained in that tiny little box. The first is the icon in the top left of the column header representing the type of data. Second is the drop down arrow in the top right of the column header. Finally is the sort option in the bottom right of the column header box. The drop down menu arrow and the sort icon on the right side will not appear until you hover over the column header.

### Data Types

For each column, there is an icon that represents the type of data it contains, or, more accurately, the type of data Tableau has concluded it contains. The options are: Number (decimal), Number (whole), Date & Time, Date, String, and Boolean. When you see a globe icon, this means the data type is a string or a number with a *Geographic Role* assigned to it. Possible geographic roles include airport, area code, city, country/region, county, state/province, zip code, latitude, and longitude. If the data type is a string, you will not see latitude or longitude as options under geographic role. To update the data type of a column, click the icon and select the new data type. The most common types that need correcting are ID columns that default to a number or a year that also defaults to a number. A good way to think about what data type a column should be is to consider how the column will be used in your visualization. If it might make sense to aggregate the field by summing or averaging, for example, then that field should be a number type. If the only way you would aggregate that column would be through a count, then it is likely that column should be in a string. If the column represents a date, such as year, then, obviously, change it to date format. What happens when you change a column *year* to a date data type?

### Other Column Options

The quick menu in the top right of each column provides the following options...

- **Rename**: Rename the column name

- **Reset Name**: Reset the name of the column to the name in the source data. Tableau renames the fields, upon import, to a more audience friendly name. Often, when building the visualizations, and especially calculated fields, it is easier to have names not separated by spaces. In these cases, it might be easier to revert back to the original names.

- **Copy Values**: By selecting the column and then 'copy values', you are copying the values in the column to the clipboard. It is the same as typing command-C.

- **Hide**: Hide will hide the column from view. You can still reference the column, such as in calculated fields.

- **Aliases** (strings only): Aliases are useful when you want a value in a field to be a more user-friendly value. For example, if *State* was in abbreviated form, but you want to make sure the entire state is spelled out on your visualizations, then aliasing would be useful. The alias does not change anything about the data in the background, only what is displayed.

- **Create Calculated Field...**:   Create a new field based on existing fields. As an example, we will create a new field, award_per_natl_delta, that is the difference between awards_per_natl_value and awards_per_value. In the column *Awards Per Natl Value*, select Create Calculated Field from the drop down menu in the top right corner of the column header. Add the new column name, Awards Per Natl Delta. In the formula box, enter the formula:  [Awards Per Value] - [Awards Per Natl Value] and click OK. You now have a new column where the data type icon, instead of '#' for number, it shows '=#' to represent a calculated number. You will also notice the lack of a blue bar bordering the top of the column header, indicating the column was not in the original data.

- **Create Group...**: Created Group is used for grouping categories into larger, higher hierarchical groups. For example, if I wanted to have a way to identify states by region, I could use the *State* column to create groups and then add each state to a group, such as south, northeast, southwest, northwest, and central. To do so, go to "Create Group" in the drop down menu for the *State* column. Begin selecting the states you wish to go in the first group. To select multiple states, hold the Command key down. Once your first group values are selected, click 'group'. You can then name the group. Move on to the next group. When you are done, title the new field and click ok. You can know a field is a result of grouping another field by the paperclip that has been added to the data type icon.

- **Split** (strings only): Split strings at a common delimiter into multiple columns. Let's take the field, *Counted Pct*, as an example. *Counted Pct* is defined as the "share entering undergraduate class who were first-time, full-time, degree-seeking students, meaning that they generally would be part of a tracked cohort of potential graduates. The entering class of 2007 is displayed for 4-year institutions; 2010 for 2-year institutions" (https://data.world/databeats/college-completion/workspace/data-dictionary). Currently, the data is in the format pct|yy, such at 54.8|10. 54.8% of those entering that 2-yr college's undergraduate class of 2010 were first-time, full-time, degree-seeking students. I would like to be able to use that percentage, so if I split the column into 2, then I can turn one into numeric and the other into date.  I can then hide the original column.

- **Custom Split** (strings only): With custom split, you can specify the delimiter to split on. You can also specify how many columns to split off.

- **Create Bins...** (numbers only): Bins are useful when you have a continuous variable and you want to reduce the noise and bin the values close to each other together. For example, if you wanted to create a field that bins the number of students into equally sized groups, you could use "Create Bins" to do that.

- **Pivot** (when selecting multiple fields): Use as you would when creating a pivot table in excel or Python.

- **Merge Mismatched Fields** (when selecting multiple fields): Does what you would think! Use this when you want to merge fields into a single field, such as *City* and *State* into *City State*.

- **Describe**: Describe is a useful resource for a quick view into the column. The domain is not loaded by default. To see the domain of the field, click 'Load' in the Describe window. If you look at the description for *Awards Per Natl Delta*, a calculated field, you will see the formula that is used to calculate that field.


### Column Sorting

Click the horizontal bar graph icon in the column header to sort that column. It will cycle through ascending, descending, and original sort as you click the icon. When you hover over the column header, you can tell if it is sorted by the way the horizontal bar graph image is sorted.

_______________________________________________

## Getting Help

- F1 or the Help menu header: you have options to get support, watch videos, see sample workbooks, sample gallery, as well as customizing settings & preferences.
- onlinehelp.tableau.com

_______________________________________________

## Exercises

1. In your mySQL client, query the database `telco_normalized`, joining all tables together into a single table which you will then export to a csv and save on your local drive. Do NOT use the telco_churn database. 

2. Connect to your csv through the tableau client that is installed on your laptop. Reminder: a csv is considered a text file. 

3. Hide any redundant columns (payment_type_id, contract_type_id, internet_service_type_id are all represented through the columns with their descriptive names). 

4. Dimensions are something you could group by to see aggregated measures, like average payment by gender, or total charges by customer_id. Measures are the fields you would perform calculations on. Ensure all possible measures are stored number datatype, and all dimensions are NOT stored as number data types. E.g. Senior Citizen will need to be changed to a string. 

5. Create aliases for values in the following fields. Follow the examples to make similar aliases. The goal is to make the values easily interpretable to the user. 

    - Senior Citizen: "Is Senior Citizen", "Not Senior Citizen"
    - Partner
    - Dependents
    - Paperless Billing
    - Phone Service
    - Multiple Lines: "No": "Single line", "Yes": "Multiple lines", "No phone service": "No Phone service"
    - Online Security: "No": "Internet without Online Security", "Yes": "Online Security", "No internet service": "No internet service"
    - Online Backup
    - Device Protection
    - Tech Support
    - Streaming TV
    - Streaming Movies
    
8. Create a new grouped field from payment type. Group the automatic payments by selecting both of those payment types, and name the group "Automatic Payment". Then group the non-auto payments and name the group "Manual Payment". You will then have a new field at the end of your table titled "Payment Type (group)". 

9. Once your table is ready, export it to a csv for a backup in case your tableau file gets deleted! (data -> export data to csv)

_______________________________________________

## Data Resources

- https://ds.codeup.com/appendix/open_data/
- https://public.tableau.com/en-us/s/resources

_______________________________________________

## References

Medrano, Diego (April 14, 2016), Tableau Online tips: Extracts, live connections, & cloud data,
https://www.tableau.com/about/blog/2016/4/tableau-online-tips-extracts-live-connections-cloud-data-53351

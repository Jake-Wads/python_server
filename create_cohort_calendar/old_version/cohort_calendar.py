from csv_ical import Convert
import pandas as pd
import numpy as np

# cohort_name = 'oneill'
def create_cohort_start_stop_df():
# source: https://docs.google.com/spreadsheets/d/1BZVS8D3Z0jkZxUeQNlGvwn88P9nH2ZM2j8WzdkEC4kc/edit?usp=sharing
    labels = ['cohort', 'start_date', 'end_date']
    easley = ['easley',  '12/07/2020', '06/11/2021']
    florence = ['florence', '03/15/2021', '09/03/2021']
    germain = ['germain', '06/14/2021', '12/07/2021']
    hopper = ['hopper', '09/07/2021', '03/14/2022']
    innis = ['innis', '12/13/2021', '06/16/2022']
    jemison = ['jemison', '03/21/2022', '08/19/2022']
    kalpana = ['kalpana', '05/09/2022', '10/07/2022']
    leavitt = ['leavitt', '06/20/2022', '11/18/2022']
    mirzakhani = ['mirzakhani', '08/29/2022', '02/10/2023']
    noether = ['noether', '10/17/2022', '03/31/2023']
    oneill = ['oneill', '01/17/2023', '06/16/2023']
    pagel = ['pagel', '02/28/2023', '07/31/2023']
    somerville = ['somerville', '06/13/2023', '11/13/2023']
    cohort_df = pd.DataFrame([easley, florence, germain, hopper, innis, jemison, kalpana, leavitt, mirzakhani, noether, oneill, pagel, somerville])
    cohort_df.columns = labels
    
    return cohort_df

def create_holiday_df(file_path='student_holidays.csv'):
    '''
    this function takes a file that contains all student holidays and reads it in to a dataframe
    with the date being the index, and student Holiday names returned for each date. 
    '''
    holiday_df = pd.read_csv(file_path)
    holiday_df['Date'] = pd.to_datetime(holiday_df.Date)
    holiday_df.index = pd.to_datetime(holiday_df.Date)
    return holiday_df

def create_sepd_days():
    '''
    this function creates a dataframe of student experience/prof development days
    based on dates provided by student experience. these dates are manually entered here reference
    in creating the cohort calendar. 
    a dataframe with the dates, cohort, event type (se/pd day 1 or 2). 
    '''
    labels = ['cohort', 'event_type', 'date']
    leavitt_d1 = ['leavitt', 'se/pd day 1', '07/12/2022']
    leavitt_d2 = ['leavitt', 'se/pd day 2', '09/08/2022']
    mirzakhani_d1 = ['mirzakhani', 'se/pd day 1', '09/22/2022']
    mirzakhani_d2 = ['mirzakhani', 'se/pd day 2', '11/14/2022']
    noether_d1 = ['noether', 'se/pd day 1', '11/07/2022']
    noether_d2 = ['noether', 'se/pd day 2', '01/04/2023']
    oneill_d1 = ['oneill', 'se/pd day 1', '02/07/2023']
    oneill_d2 = ['oneill', 'se/pd day 2', '04/18/2023']
    pagel_d1 = ['pagel', 'se/pd day 1', '07/29/2023']
    pagel_d2 = ['pagel', 'se/pd day 2', '07/30/2023']
    somerville_d1 = ['somerville', 'se/pd day 1', '11/11/2023']
    somerville_d2 = ['somerville', 'se/pd day 2', '11/12/2023']
    se_pd_days = pd.DataFrame([leavitt_d1, leavitt_d2, mirzakhani_d1, mirzakhani_d2, 
                               noether_d1, noether_d2, oneill_d1, oneill_d2, pagel_d1, pagel_d2,
                               somerville_d1, somerville_d2]
                             )
    se_pd_days.columns = labels
    se_pd_days['date'] = pd.to_datetime(se_pd_days['date'])
    se_pd_days = se_pd_days.set_index('date')
    se_pd_days.to_csv('se_pd_days.csv')
    return se_pd_days

# 
def get_lessons(generic_lessons_filepath='generic_lessons_days_full_wednesdays.csv'):
    '''
    this function reads in a csv that contains generic lessons by the class day number. 
    it returns a dataframe with the lesson description, delivery_day_number, and event_type (delivery_day)
    '''
    lesson_df = pd.read_csv(generic_lessons_filepath)
    lesson_df['event_type'] = 'delivery_day'
    return lesson_df

def get_cohort_days(cohort_name,
                    holidays_file_path = 'student_holidays.csv',
                    se_pd_days_path = 'se_pd_days.csv'):
    '''
    This function takes, as arguments, cohort_name, holidays.csv file path, and se_pd_days.csv file path 
    and returns a data frame, "cohort_days" that includes the dates, holidays, se-pd days
    '''
    # create a 2 row dataframe with the start and stop date for next cohort (we will then fill in the dates 
    # inbetween using asfreq)
    # cohort_calendar contains the start and stop dates of each cohort, filter to the next cohort
    next_cohort = pd.DataFrame(create_cohort_start_stop_df().set_index('cohort').loc[cohort_name])
    next_cohort.columns = ['Date']
    
    # create a dataframe with all dates in between the start and stop date of the next cohort. 
    next_cohort_dates = pd.DataFrame(pd.to_datetime(next_cohort.Date)).set_index(next_cohort.Date).asfreq('D')
    
    # read in the holidays and add those to the dataframe
    holiday_df = create_holiday_df(file_path=holidays_file_path)
    holiday_df.columns = ['date', 'student_holiday']

    # join on holidays dataframe
    cohort_days = next_cohort_dates.join(holiday_df, how='left').drop(columns=['Date', 'date'])
    
    # get weekday names
    cohort_days['weekday'] = cohort_days.index.day_name()

    # label weekends and classdays
    cohort_days.loc[cohort_days.weekday == 'Saturday', 'student_holiday'] = 'Weekend'
    cohort_days.loc[cohort_days.weekday == 'Sunday', 'student_holiday'] = 'Weekend'

    # label classdays
    cohort_days.loc[cohort_days.student_holiday.isna(), 'is_classday'] = 1
    cohort_days.is_classday = cohort_days.is_classday.fillna(0)

    # add hours per class day
    hours = pd.DataFrame({'weekday': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                    'is_classday': [1, 1, 1, 1, 1, 0, 0], 'class_hours': [6, 7, 7, 6.5, 7, 0, 0]})

    # merge with class hours per day on classdays
    cohort_days = cohort_days.merge(hours, how='left', 
                                    on=['weekday', 'is_classday']).set_index(cohort_days.index)

    # fill na's in class hours with 0 when holiday or weekend. 
    cohort_days.class_hours = cohort_days.class_hours.fillna(0)

    return cohort_days

def get_class_days(cohort_days):
    # get the dates for all non-holiday, non-weekend days. 
    class_days = cohort_days[cohort_days.is_classday == 1].reset_index()
    # using those days, add a classday_num that is the day number of the cohort. 
    class_days['classday_num'] = class_days.index + 1

    # reset the index back to the date
    class_days = class_days.set_index('Date')

    return class_days

def get_delivery_days(class_days, se_pd_days, cohort_name):
    '''
    merge the class_days dataframe (with date, day of week, is_classday, and hours) with se_pd_days to 
    add prof development days into the df
    '''
    delivery_days = pd.merge(class_days, se_pd_days[se_pd_days.cohort==cohort_name][['event_type']],
                             how='left', left_index=True, right_index=True)

    # add 'event_type' to be delivery day when null. otherwise it is 'se/pd day'
    delivery_days.loc[delivery_days['event_type'].isna(), 'event_type'] = 'delivery_day'

    # separate the delivery days into 3 sections...before the first PD day, between the first and the second, and 
    # after the second. this way we can shift the classday_num by one to have a delivery_day_num. That way we leave 
    # a blank day for each PD day in the lessons in order to insert the PD days. 
    delivery_days1 = delivery_days[delivery_days.index < 
                                   se_pd_days[se_pd_days.cohort == cohort_name].index[0]].classday_num
    delivery_days2 = delivery_days[delivery_days.index >= 
                                   se_pd_days[se_pd_days.cohort == cohort_name].index[0]].classday_num.shift()
    delivery_days3 = delivery_days2[delivery_days2.index >= se_pd_days[se_pd_days.cohort == cohort_name].index[1]].shift()
    
    # concatenate all delivery_days series 
    delivery_day_num = pd.concat([delivery_days1, 
                                  delivery_days2[delivery_days2.index < 
                                                 se_pd_days[se_pd_days.cohort == cohort_name].index[1]], 
                                  delivery_days3])
    return delivery_day_num

def get_lesson_dates(class_days, delivery_day_num, lesson_df):
    '''
    merge the delivery_day_num series with the classdays so that the daynum is associated withthe correct date. 
    And there should not be a delivery_day_num for the 2 PD days now. Doing this will allow lessons to line up 
    correctly.
    '''
    class_days = pd.merge(class_days, delivery_day_num, how='left', left_index=True, right_index=True)
    class_days = class_days.rename({'classday_num_x': 'classday_num', 'classday_num_y': 'delivery_day_num'}, axis=1)
    lesson_dates = pd.merge(class_days.reset_index(), lesson_df, on=['delivery_day_num'], how='left')
    lesson_dates.loc[lesson_dates.event_type != 'delivery_day','generic_event_name'] = 'SE/PD Day'

    # shift capstons 
    # get the number of days at the end of our dataframe with no event name. 
    # This means that this cohort has more days than the generic lesson list does
    # and shift so that capstones take up with last 15 days of the cohort. 
    # lesson_dates = cohort_calendar.shift_capstones(lesson_dates)

    return lesson_dates

def get_full_calendar(cohort_days, lesson_dates):
    full_calendar = cohort_days.reset_index().merge(lesson_dates.drop(columns=['student_holiday', 
                                                                                'weekday', 
                                                                                'is_classday', 
                                                                                'class_hours']), on='Date', how='left')
    # for google calendar, we need a csv with the column names "Subject" and "Start Date"
    # I will remove weekends but keep holidays in there for the calendar. 

    full_calendar.loc[full_calendar.student_holiday.notnull(), 'Subject'] = full_calendar.student_holiday
    full_calendar.loc[full_calendar.student_holiday.isnull(), 'Subject'] = full_calendar.generic_event_name

    # select the 2 columns needed and rename them as needed by google calendar
    new_cohort_calendar = full_calendar[['Subject', 'Date']]
    new_cohort_calendar.columns = ['Subject', 'Start Date']
    new_cohort_calendar[new_cohort_calendar['Start Date'] == '2022-11-14']
    return new_cohort_calendar

def get_new_cohort_calendar(cohort_name,
                        generic_lessons_filepath='generic_lessons_days_full_wednesdays.csv',
                        holidays_file_path = 'student_holidays.csv', 
                        se_pd_days_path = 'se_pd_days.csv'
                       ):
    se_pd_days = create_sepd_days()
    lesson_df = get_lessons(generic_lessons_filepath)
    cohort_days = get_cohort_days(cohort_name, holidays_file_path, se_pd_days_path)
    class_days = get_class_days(cohort_days)
    delivery_day_num = get_delivery_days(class_days, se_pd_days, cohort_name)
    lesson_dates = get_lesson_dates(class_days, delivery_day_num, lesson_df)
    new_cohort_calendar = get_full_calendar(cohort_days, lesson_dates)
    return new_cohort_calendar



def calendar_to_csv(cohort_name, generic_lessons_filepath='generic_lessons_days_full_wednesdays.csv',
                    holidays_file_path = 'student_holidays.csv', se_pd_days_path = 'se_pd_days.csv'):
    # name your calendar with the cohort name
    new_cohort_calendar = get_new_cohort_calendar(cohort_name,
                                                  generic_lessons_filepath, 
                                                  holidays_file_path, 
                                                  se_pd_days_path)
    csv_name = cohort_name+'_cal.csv'
    new_cohort_calendar.to_csv(csv_name)

# def read_convert_save_calendar(cohort_ics, cohort_csv):
#     convert = Convert()
#     convert.CSV_FILE_LOCATION = cohort_csv
#     convert.SAVE_LOCATION = cohort_ics

#     convert.read_ical(convert.SAVE_LOCATION)
#     convert.make_csv()
#     convert.save_csv(convert.CSV_FILE_LOCATION)

    
# def read_calendar_csv(cohort):
#     read_convert_save_calendar(cohort + '.ics', cohort + '.csv')
#     df = pd.DataFrame(columns=['event','start','end','cohort'])
#     temp_df = pd.read_csv(cohort + '.csv', header = None, usecols = [0, 1, 2], names=['event', 'start', 'end'])
#     temp_df['cohort'] = cohort
#     df = pd.concat([df, temp_df], axis=0)
#     return df


# def get_generic_lessons_days(file_path="generic_lessons_days.csv"):
#     lesson_df = pd.read_csv(file_path)
#     return lesson_df
    
             
# # half-day wednesdays

# def get_class_dates(cohort_name):
#     cohort_df = create_cohort_start_stop_df()
#     holiday_df = create_holiday_df(file_path='student_holidays.csv')

#     dates_df = cohort_df[cohort_df.cohort==cohort_name]
#     dates_df = pd.DataFrame({'date': [dates_df.start_date.iloc[0], dates_df.end_date.iloc[0]]})

#     #convert to datetime
#     dates_df = pd.DataFrame(pd.to_datetime(dates_df.date)).set_index(dates_df.date).asfreq('D')

#     # join on holidays dataframe
#     dates_df = dates_df.join(holiday_df, how='left').drop(columns=['date', 'Date'])

#     # get weekday
#     dates_df['weekday'] = dates_df.index.day_name()

#     # label weekends
#     dates_df.loc[dates_df.weekday == 'Saturday', 'Student Holidays'] = 'Weekend'
#     dates_df.loc[dates_df.weekday == 'Sunday', 'Student Holidays'] = 'Weekend'

#     # new column names
#     dates_df.columns = ['student_holiday', 'weekday']

#     dates_df['is_classday'] = dates_df.student_holiday.isnull().astype(int)
#     class_days = dates_df[dates_df.is_classday==1].drop(columns=('student_holiday'))

#     # half-day wednesdays
# #     hours = pd.DataFrame({'weekday': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
# #                    'is_classday': [1, 1, 1, 1, 1, 0, 0], 'class_hours': [6, 7, 3.5, 6.5, 7, 0, 0]})
#     hours = pd.DataFrame({'weekday': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
#                     'is_classday': [1, 1, 1, 1, 1, 0, 0], 'class_hours': [6, 7, 7, 6.5, 7, 0, 0]})

#     class_days_df = class_days.merge(hours, how='left', on=['weekday', 'is_classday'])

#     # give new dataframe the original date index. 
#     class_days_df.index = class_days.index

# #     class_days_df = pd.concat([class_days_df, class_days_df[class_days_df.weekday != 'Wednesday']]).sort_index()
    

# #     class_days_df['halfday_num'] = np.arange(class_days_df.shape[0])
# #     class_days_df = pd.concat([
# #         class_days_df.halfday_num.rank().rename('halfday_num2'), class_days_df],
# #        axis=1).drop(columns='halfday_num').rename(columns={'halfday_num2': 'halfday_num'})
#     class_days_df = class_days_df.reset_index()
#     class_days_df['start'] = class_days_df['index']
#     class_days_df = class_days_df.drop(columns=['index'])
# #     class_days_df['day_segment'] = class_days_df.groupby('start')['halfday_num'].rank("min")
    
#     class_days_df = class_days_df[['start', 'day_segment', 'halfday_num']]


#     return class_days_df


# def clean_cal(df):

#     # filter out all events with a time
#     df = df[~df.start.str.contains("\s([0-9]{2}:){2}.+$", case=True, flags=0, na=None, regex=True)]

#     # create a start date field
#     df['start'] = pd.to_datetime(df.start)

#     # get the name of the day
#     df['day_of_week'] = df['start'].dt.day_name()

#     # drop end date as each event we are concerned with is one day only 
#     df = df.drop(columns=['end'])

#     # filter out where 'OOO' is in the entry
#     df = df[~df.event.str.contains("(OOO|Out|Vacation|No\sClass|Staff\s*Day|(\
#                                (Faith|Adam|John|Madeleine|Maggie|Ravinder|Ryan|Sam|Zach)\s*(in\s*[a-z]|Out)))", 
#                                case=False, flags=0, na=None, regex=True)]

#     df = df.sort_values(by=['start']).reset_index(drop=True)

#     return df

# def extract_lesson_details(df):
    
#     # extract the module the lesson was in. 
#     df['module'] = df.event.str.extract(r'(^\w*)')

#     # extract the lesson name
#     lesson_name_df = df.event.str.extract(r'(L[0-9]{2})((\s+\w+)+)(\s+)(\[[A-Za-z]+\])')
#     # the first column has the lesson number
#     df['lesson_number'] = lesson_name_df[0]

#     # the fifth column has the instructor name
#     df['lesson_instructor'] = lesson_name_df[4]

#     # The third column will be the last word of the lesson name. 
#     # if it is a lesson review, the third column will say "Review"
#     # first, strip whitespace. 
#     lesson_name_df[2] = lesson_name_df[2].str.strip()

    
#     df['review'] = lesson_name_df[2] == 'Review'

#     # the second column has the lesson name
#     df['lesson_name'] = lesson_name_df[1]

#     # identify if the event is a lesson or not
#     df['is_lesson'] = (df['lesson_name'].notnull())
    
#     # standardize lesson names...start at L00 instead of L01. 
#     if list(df['lesson_number'].dropna().sort_values().head(1))[0]=='L01':
#         lessons = {'Orig_Lesson':['L01','L02','L03', 'L04', 'L05', 'L06', 'L07', 'L08', 'L09', 'L10', 'L11'],
#                    'New_Lesson':['L00', 'L01','L02','L03', 'L04', 'L05', 'L06', 'L07', 'L08', 'L09', 'L10']}
#         lessons = dict(zip(lessons['Orig_Lesson'], lessons['New_Lesson']))
#         df['lesson_number'] = df['lesson_number'].replace(lessons, regex=True)

#     df.loc[df['is_lesson']==False, 'lesson_name'] = df.event

#     df.loc[df['lesson_number'].isnull() == True, 'event_name'] = df['lesson_name']
    
#     df.loc[df['event_name'].isnull()==True, 'event_name'] = (
#         df['module'] + " " + df['lesson_number'] + " " +  df['lesson_name'] + " " + '[instr]')

#     # replace all instructor names with [instr]
#     df['event_name'] = df.event_name.str.replace('\[.*\]', '[instr]', regex=True)

#     # replace all cohort names with [Cohort]
#     df['event_name'] = df.event_name.str.replace('(Ada|Bayes|Curie|Darden|Easley|Florence|Germain)', 
#                                                  '[Cohort]', regex=True)

#     df['event_num'] = np.arange(df.shape[0])
#     df['day_segment'] = df.groupby('start')['event_num'].rank("min")

#     df.loc[df.event_num > 2.0, 'event_num'] = 2.0
#     df.loc[df.day_of_week == 'Wednesday', 'event_num'] = 1.0

#     return df[['start', 'day_segment', 'event_name']]
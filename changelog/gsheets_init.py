import gspread

spreadsheet_name = 'Student Github Activity Tracking'

gc = gspread.oauth()

sh = gc.open(spreadsheet_name)

print(sh.sheet1.get('A1'))


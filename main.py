import openpyxl as xl

excel_filepath = 'data/db.xlsx'

Worksheet = xl.load_workbook(filename=excel_filepath).active

print(Worksheet['A1'])
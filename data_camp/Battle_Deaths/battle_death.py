import pandas as pd

file = 'Battle_Deaths/battledeath.xls'

xls = pd.ExcelFile(file)

print(xls.sheet_names)

d = xls.parse('bdonly')

print(d.head())
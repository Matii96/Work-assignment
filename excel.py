#Import the toolbox
import sys
from workflow import association
from xlrd import open_workbook

if len(sys.argv) != 2:
    raise ValueError('You need to pass path to sheet')

wb = open_workbook(sys.argv[1])
for sheet in wb.sheets():
    for row in range(1, sheet.nrows):
        for col in range(sheet.ncols):
            print(sheet.cell(row,col).value)

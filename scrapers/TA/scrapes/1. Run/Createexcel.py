# unused
#source: https://xlsxwriter.readthedocs.io/tutorial03.html

import pandas as pd
import os
import openpyxl
import xlsxwriter
import numpy as np
from glob import glob

#create new excel file to append prices and dates
workbook = xlsxwriter.Workbook('joinedprices_Aphrodite.xlsx')
worksheet = workbook.add_worksheet('Prices_per_night_and_date')

#set rows and columns to 0
row = 0
col = 0

# write some data headers
bold = workbook.add_format({'bold': 1})
worksheet.write('A1', 'Price per night', bold)
worksheet.write('B1', 'Date of price', bold)
worksheet.set_column('A:B', 12)

workbook.close()

print("Excel created")

import pandas as pd
from glob import glob


#for entry in glob('data/next/Male.xlsx'):
#    with open(entry, 'r') as f:
#        df = pd.read_excel(entry, sheet_name='Male_Versuch_2')

#        df.to_csv('data/final/Male_k.csv', header=True, index=False)

#print('Dates appended - CSV saved')

for entry in glob('data/next/Dhabi.csv'):
    with open(entry, 'r') as f:
        df = pd.read_csv(entry)

        df.to_csv('data/final/Dhabi.csv', header=True, index=True)

print('Dates appended - CSV saved')

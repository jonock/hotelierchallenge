import pandas as pd
from glob import glob


for entry in glob('data/Versuch_5.xlsx'):
    with open(entry, 'r') as f:
        df = pd.read_excel(entry, sheet_name='Versuch_5')

        df.to_csv(entry + 'new.csv', header=True, index=True)

print('Dates appended - CSV saved')
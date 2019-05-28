import pandas as pd

output = pd.DataFrame([['a','b', 'e'], ['c', 'd', 'f']],
                        columns = ['Locality', 'AVG_Price', 'Date'])
output.to_excel("output.xlsx")

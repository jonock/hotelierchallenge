#this script will go through the hotel_price files and create one file with all data

import pandas as pd
from glob import glob


#fname = 'data/Test6.txt'

#with open (fname) as f:
    #lines = f.readlines()
#lines = [x.strip() for x in lines]

#fline = lines [1]

#print(fline[:2])

# Split by whitespace
filename = 'data/Test6.txt'
file = open(filename, 'wt')
text = file.read()

lines = text.split(',')                         # split into words by white space
lines = [x.strip() for x in lines]
file.close()

#print(lines[0])

file = open(filename, 'a')
file.write(lines)
file.close()

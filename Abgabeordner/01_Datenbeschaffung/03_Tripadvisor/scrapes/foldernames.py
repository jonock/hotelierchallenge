#import os
#rootdir = '/Users/TobiasRordorf/Desktop/UNI/MBI\ HSG/4.\ Semester/Python/GitHub/hotelierchallenge/scrapers/TA/scrapes/Test'

#for subdir, files in os.walk(rootdir):
#    for file in files:
#        print (os.path.join(subdir, file))


import os
from glob import iglob

rootdir_glob = '/Users/TobiasRordorf/Desktop/UNI/MBI\ HSG/4.\ Semester/Python/GitHub/hotelierchallenge/scrapers/TA/scrapes/Test/**/*' # Note the added asterisks
# This will return absolute paths
file_list = [f for f in iglob('**/*', recursive=True) if os.path.isfile(f)]

print(file_list)

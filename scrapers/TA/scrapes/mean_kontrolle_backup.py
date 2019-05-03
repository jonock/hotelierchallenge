#this script will go through the hotel_price files and create one file with all data per hotel

import pandas as pd
from glob import glob
from glob import iglob
import os

rootdir = './Test/kontrolle/'
#open every file in specified folder


for sfolder in os.listdir(rootdir):
#    print(sfolder)
    if sfolder == '.DS_Store':
        continue
    childdir = os.path.join(rootdir, sfolder)

    avg = pd.DataFrame()
    all_data = pd.DataFrame()
    avg.drop(avg.index, inplace=True)
    sfoler = childdir + '/*.csv'
    n=0
    for entry in glob(sfoler):
        checklist = ['test','testtest']
        with open(entry, 'r') as f:
            df = pd.read_csv(entry)
            #print('print: ' + df)
            timestamp = df.iloc[0,1]
            #print(timestamp)
            short_timestamp = timestamp[:13]
#           print('Short-timestamp ' +short_timestamp)
            for searchfname in glob(sfoler):
                if searchfname in checklist:
                    continue
                #print(searchfname)
                if short_timestamp.replace(':','-') in searchfname:
                    checklist.append(searchfname)
                    #print(searchfname + 'GEFUNDEN')
                    with open(searchfname, 'r') as g:
                        dg = pd.read_csv(searchfname)
                        all_data = all_data.append(dg, ignore_index=True)
                        #print ('all_data: ' + all_data)
                avgvar = (all_data.loc[:, "price_per_night"]).replace(' ','')
                #avgvar.apply(pd.to_numeric) #errors='coerce'
                avgvar = avgvar.str.strip()
                avgvar = pd.to_numeric(avgvar)
                #print(avgvar)
        print(avgvar)
        avgmean = avgvar.mean()
        avgmean_appended = pd.DataFrame()
        avgmean_appended = avgmean_appended.append(avgmean, ignore_index=True)
        print(avgmean_appended)
        all_data.drop(all_data.index, inplace=True)

#        print(str(checklist))

    filename = str(short_timestamp)+'_appended.csv'
    output = pd.DataFrame([['Mean_prices_per_night', 'Timestamp'],[avgmean_appended, short_timestamp]])
    output.to_csv('Test/appended/' + filename, header=True, index=False, encoding='utf-8-sig')
    avgmean_appended.drop(avgmean_appended.index, inplace=True)

print('Dates appended, average caluclated - Csv saved')


#region_prices = region_prices.apply(pd.to_numeric, errors='coerce').combine_first(region_prices)
#output = pd.DataFrame([[locality, avg, date]],
                        #columns = ['Locality', 'AVG_Price', 'Date'])
#output.to_excel(entry + "_average.xlsx")

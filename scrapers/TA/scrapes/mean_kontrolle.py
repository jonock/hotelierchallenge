#this script will go through the hotel_price files and create one file with all data per hotel

import pandas as pd
from glob import glob
from glob import iglob
import os

rootdir = './Test/Kontrolle/'
#open every file in specified folder


#Äusserste Schleife - Einzelne Ordner durchgehen (Jede Destination)
for sfolder in os.listdir(rootdir):
#    print(sfolder)
    if sfolder == '.DS_Store':
        continue
    childdir = os.path.join(rootdir, sfolder)

    avg = pd.DataFrame()
    all_data = pd.DataFrame()
    avgmean_appended = []
    avgmean_timestamps = []
    avg.drop(avg.index, inplace=True)
    sfoler = childdir + '/*.csv'
    n=0
    checklist = ['checklist']
#2. Schleife Jedes File in gegebenem Ordner durchgeben
    for entry in glob(sfoler):
        print(entry)
        # Falls File bereits gelesen wird übersprungen
        if entry in checklist:
            print('CONTINUE')
            continue
# Jedes file wird geöffnet und als Dataframe eingelesen -> Timestamp wird extrahiert
        with open(entry, 'r') as f:
            df = pd.read_csv(entry)
            #print('print: ' + df)
            timestamp = df.iloc[0,1]
            #print(timestamp)
            short_timestamp = timestamp[:13]
            #3. Schleife - Alle Files im Ordner werden erneut durchlaufen
            for searchfname in glob(sfoler):
                #print(searchfname)
                #Überprüfung ob Zeitstempel in einem der Filenamen vorkommt
                if short_timestamp.replace(':','-') in searchfname:
                    checklist.append(searchfname)
                    with open(searchfname, 'r') as g:
                        dg = pd.read_csv(searchfname)
                        all_data = all_data.append(dg, ignore_index=True)
                        #print ('all_data: ' + all_data)
                    avgvar = (all_data.loc[:, "price_per_night"]).replace(' ','')
                    #avgvar.apply(pd.to_numeric) #errors='coerce'
                    avgvar = avgvar.str.strip()
                    avgvar = pd.to_numeric(avgvar)
                #print(avgvar)
#        print(avgvar)
        avgmean = avgvar.mean()
        #Einzelner Durschnitt gerechnet - in avgmean abgespeichert
        avgmean_appended.append(avgmean)
        avgmean_timestamps.append(short_timestamp)
#        print(avgmean_timestamps)
        avgmean_df = pd.DataFrame(data=avgmean_appended)
        avgmean_timestamps_df = pd.DataFrame(data=avgmean_timestamps)
#        print(avgmean_df)
#        print(str(avgmean_appended)+ ' jetzt wird appended')
        short_timestamp = 0
        all_data.drop(all_data.index, inplace=True)
        avgmean = 0

#        print(str(checklist))

    filename = sfolder + str(short_timestamp)+'_appended.csv'
    avgmean_df = pd.concat([avgmean_df, avgmean_timestamps_df],axis=1)
    print(avgmean_df)
    output = pd.DataFrame([['Mean_prices_per_night', 'Timestamp'], [avgmean_df]])
    avgmean_df.to_csv('Test/appended/' + filename, header=False, index=False, encoding='utf-8-sig')
#    avgmean_appended.drop(avgmean_appended.index, inplace=True)
    avgmean_appended=[]
#    print(avgmean_appended)
    checklist= ['leer']

print('Dates appended, average caluclated - Csv saved')

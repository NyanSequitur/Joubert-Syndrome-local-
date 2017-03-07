import pandas as pd
from datetime import datetime


df = pd.read_excel('JS-LIFE Instrument Interval.xlsx')

# output dicitonary
d = {}

# also we will keep track of all unique instruments
unique_instruments = set()

row = df.iloc[0]

user_id =       row['Foreign Key']
instrument_id = row['Instrument ID'
                    
unique_instruments.add(instrument_id)
    # user has not been added to dict
if user_id not in d:
    d[user_id] = {}

    # this is a dictionary
user = d[user_id]

if instrument_id not in user:
    user[instrument_id] = []

    # list of time stamps
time_stamps = user[instrument_id]
                    
date_string = row['Date Answered']
datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
                    
table = {instrument: [] for instrument in unique_instruments}

# now for a column to hold the row index
table['user_id'] = []
           
for user in d.keys():

    # dict where instruments are keys
    # and list of time stamps are keys
    instrument_dict = d[user]

    # we will add a row to our output table
    table['user_id'].append(user)

    # itereate through instruments
    for instrument in unique_instruments.keys():

        # if instrument is not in the dict we give it a value of none
        if instrument not in instrument_dict:
            table[instrument].append(None)
            continue

        time_stamps = instrument_dict[instrument]
        duration = (max(time_stamps) - min(time_stamps)).seconds


# create pandas dataframe
output_table = pd.DataFrame(table)

# save to excel notebook
                    
pivot = pd.DataFrame.from_dict(d, orient='index')
                    
writer = pd.ExcelWriter('Instrument_Interval.xlsx')
pivot.to_excel(writer, 'Sheet1')
writer.save()

import pandas as pd
import arrow


# source data
df = pd.read_sql('put the file name here')

# output dicitonary
d = {}

# also we will keep track of all unique instruments
unique_instruments = set()

for i in range(len(df)):
    row = df.iloc[i]

    user_id = row['NAME OF USER ID COLUMN']
    instrument_id = row['NAME OF INSTRMENT ID COLUMN']

    # update our list of unique_instruments
    unique_instruments.update(instrument_id)

    # user has not been added to dict
    if user_id not in d:
        d[user_id] = {}

    # this is a dictionary
    user = d[user_id]

    # instrument has not been added
    if instrument_id not in user:
        user[instrument_id] = []

    # list of time stamps
    time_stamps = user[instrument_id]

    # cast this to a datetime obj
    # it might be none so lets do it in a try/except
    try:
        date_time = arrow.get(row['NAME OF COLUMN WITH TIME STAMP SHOULD GO HERE']).datetime
    except Excpetion as e:
        print(e) # print exception
        continue # continue, useless without a valid timestamp

    # add time stamp to list of time stamps
    time_stamps.append(row['NAME OF COLUMN WITH TIME STAMP SHOULD GO HERE'])
    
"""
now we have a dictionary of the form

{'user_id': {'instrument_id': [list, of, time, stamps]}}

so now we want to make a table where:
rows are user_ids
columns are instruments
values are the number of seconds it took the user to complete the instrument
"""

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
# blah blah saving to excel goes here
                                                                                                                                                                                                  90,3          Bot


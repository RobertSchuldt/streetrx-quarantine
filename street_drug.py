# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 13:13:26 2020

@author: 3043340
"""

import pandas as pd

#Import the data set 

file_s= 'C:\\Users\\3043340\\Desktop\\StreetRX Program\\streetrx.csv'

df = pd.read_csv(file_s)

#Want to upcase my names of var values
def upcase(var1):
    df[var1] = df[var1].str.upper()
    return

upcase('place_name')
upcase('product_name')


#Create a list of states for me to use
states = [
        'Alaska',
        'Alabama',
        'Arkansas',
        'Arizona',
        'California',
        'Colorado',
        'Connecticut',
        'District of Columbia',
        'Delaware',
        'Florida',
        'Georgia',
        'Hawaii',
        'Iowa',
        'Idaho',
        'Illinois',
        'Indiana',
        'Kansas',
        'Kentucky',
        'Louisiana',
        'Massachusetts',
        'Maryland',
        'Maine',
        'Michigan',
        'Minnesota',
        'Missouri',
        'Mississippi',
        'Montana',
        'North Carolina',
        'North Dakota',
        'Nebraska',
        'New Hampshire',
        'New Jersey',
        'New Mexico',
        'Nevada',
        'New York',
        'Ohio',
        'Oklahoma',
        'Oregon',
        'Pennsylvania',
        'Rhode Island',
        'South Carolina',
        'South Dakota',
        'Tennessee',
        'Texas',
        'Utah',
        'Virginia',
        'Virgin Islands',
        'Vermont',
        'Washington',
        'Wisconsin',
        'West Virginia',
        'Wyoming'
]

states = [state.upper() for state in states] 


#Identify the states in each of the rows and the corresponding quote ID
#Then I can concat the two lists to get the matching quote id to state

df_state = []
df_quote = []
for _, _, _, place_name, _, _, _, quote_id in df.values: 
    for state in states: 
        if state in place_name:
              df_state.append(state)
              df_quote.append(quote_id)
              break

#Now turn my list into dataframes that I can add to my original Df
              
from pandas import DataFrame
df_state= DataFrame(df_state, columns = ['State'])
df_quote = DataFrame(df_quote, columns = ['quote_id'])

state_id = pd.concat([df_state, df_quote], sort = False, axis = 1)

#create my merged data set with state names

streetrx_clean = df.merge(state_id, left_on = 'quote_id', right_on = 'quote_id')











#Now write to CSV for use in Tableau
streetrx_clean.to_csv('C:\\Users\\3043340\\Desktop\\StreetRX Program\\clean_streetrx.csv', header= True)
               
          
           
        
        

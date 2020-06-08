# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 12:48:34 2020

@author: Robert Schuldt

Explore the data on Street RX
"""
# Using street RX illicit drug data to look at information on 
# drug use during the months of may and april during the pandemic

import pandas as pd



street_file = "C:\\Users\\robsc\\Desktop\\Street Rx\\streetrx.csv"
#Grab my data st
df = pd.read_csv( filepath_or_buffer =  street_file )

#My names are quite messy and I just want to get state names out from the local

def upcase(var1):
    df[var1] = df[var1].str.upper()
    return

upcase('place_name')
upcase('product_name')

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

#    #I need to define a function where I check to see if a value in the place name matches the state
#    name in a list that I have created. I can go through each place and see if it matches a state name
#    from my list of state names. This would involve the IN operator and I need to define a function that compares
#    each line of my dataframe place name with the list of state names

states = [state.upper() for state in states]


locales = df['place_name']

df2 = []

for local in locales:
    for state in states:
        if state in local:
            df2.append(state)
            break
            


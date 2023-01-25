#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

'''
df = pd.read_csv('data.csv')
conditions_labels = [
    (df['dx1'].str.contains('Cognitively'), 'No Dementia'),
    (df['dx1'].str.contains('AD Dementia'), 'Dementia'),
    (df['dx1'].str.contains('No dementia'), 'No Dementia'),
    (df['dx1'].str.contains('Dementia/PD'), 'Dementia'),
    (df['dx1'].str.contains('DAT'), 'Dementia'),
    (df['dx1'].str.contains('Frontotemporal'), 'Dementia'),
    (df['dx1'].str.contains('Vascular'), 'Dementia'),
    (df['dx1'].str.contains('Incipient'), 'Dementia'),
    (df['dx1'].str.contains('DLBD'), 'Dementia'),
    (df['dx1'].str.contains('0.5'), 'No Dementia'),
    (df['norm_cog'] == 0, 'Dementia'), # if norm_cog is 0, patient is demented
    (df['gds'] >= 7, 'Dementia'), # if gds is greater than or equal to 7, patient is demented
]
df = label_rows(df, 'dx1', conditions_labels)
'''


def labeller(df, column, conditions_labels):
    for condition, label in conditions_labels:
        df.loc[condition(df[column]), column] = label
    return df

def clean_df(df):
    df = df.apply(lambda x: x.astype(str) if x.dtype != "object" else x)
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    df = df.apply(lambda x: x.str.replace(',','') if x.dtype == "object" else x)
    df = df.apply(lambda x: x.str.replace(' +', ' ') if x.dtype == "object" else x)
    return df


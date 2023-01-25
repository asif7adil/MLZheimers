#!/usr/bin/env python
# coding: utf-8

import pandas as pd

'''
# Example usage
file_list = ['file1.csv', 'file2.csv', 'file3.csv']
cols_to_extract = ['A', 'B', 'C']
cols_to_drop = ['Unwanted_column1', 'Unwanted_column2']

'''

def integrator_nkey(file_list, cols_to_extract=None, cols_to_drop=None):
    df_list = []
    for file in file_list:
        df = pd.read_csv(file)
        if cols_to_extract:
            df = df[cols_to_extract]
        if cols_to_drop:
            df = df.drop(columns=cols_to_drop)
        df_list.append(df)
    # merge all dataframes in the list
    merged_df = pd.concat(df_list)
    return merged_df


'''
# Example usage
file_list = ['file1.csv', 'file2.csv', 'file3.csv']
cols_to_extract = ['A', 'B', 'C']
cols_to_drop = ['Unwanted_column1', 'Unwanted_column2']
common_column = 'id'
'''


def integrator_key(file_list, cols_to_extract=None, cols_to_drop=None, key='id'):
    df_list = []
    for file in file_list:
        df = pd.read_csv(file)
        if cols_to_extract:
            df = df[cols_to_extract]
        if cols_to_drop:
            df = df.drop(columns=cols_to_drop)
        df_list.append(df)
    # merge all dataframes in the list
    merged_df = pd.merge(df_list[0], df_list[1], on=key)
    for i in range(2, len(df_list)):
        merged_df = pd.merge(merged_df, df_list[i], on=key)
    return merged_df


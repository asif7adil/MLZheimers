#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.experimental import enable_iterative_imputer
from sklearn.impute  import IterativeImputer

from sklearn.preprocessing import Normalizer
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

def preprocessing(df):
    cor = df.corr()
    plt.rcParams['font.size']=90
    plt.figure(figsize=(10,10))
    g = sns.heatmap(cor, xticklabels=cor.columns.values,yticklabels=cor.columns.values, annot=False, square=True, cmap=sns.diverging_palette(20, 220, n=100))
    g.set_xticklabels(g.get_xticklabels(),rotation=45, horizontalalignment='right', fontweight= 'bold')
    g.set_yticklabels(g.get_yticklabels(), fontweight='bold', )
    plt.savefig("E:/Alzheimers/Results/Corr1.svg")
    plt.show()
    user_response = input("Do you want to remove highly correlated features and columns with unique values? (yes/no)")
    if user_response.lower() == "yes":
        corr_matrix = df.corr().abs()
        high_corr_var=np.where(corr_matrix>0.8)
        high_corr_var=[(corr_matrix.columns[x],corr_matrix.columns[y]) for x,y in zip(*high_corr_var) if x!=y and x<y]
        print(high_corr_var)
        df.drop(columns=[field[0] for field in high_corr_var], inplace=True)

        # Remove fields with unique values
        unique_value_fields = []
        for field in df.columns:
            if df[field].nunique() == 1:
                unique_value_fields.append(field)
        df.drop(columns=unique_value_fields, inplace=True)
        cor = df_imputed.corr()
        plt.rc('font',weight='bold')
        plt.figure(figsize=(10,10))
        g = sns.heatmap(cor, xticklabels=cor.columns.values,yticklabels=cor.columns.values, annot=False, square=True, cmap=sns.diverging_palette(20, 220, n=100, s=100))
        g.set_xticklabels(g.get_xticklabels(),rotation=45, horizontalalignment='right', fontweight='bold')
        g.set_yticklabels(g.get_yticklabels(),fontweight='bold')
        return df
    else:
        return df


def impute_df(df):
    imputer = IterativeImputer(random_state=10)
    imputed = imputer.fit_transform(df)

    df_imputed = pd.DataFrame(imputed,columns=df.columns)

    df_imputed = round(df_imputed,2)
    return df_imputed


def splitter(df, split_size = 0.2):
    
    # Split the data into training and test sets
    X_trainval, X_test, y_trainval, y_test = train_test_split(X_normalized,y, test_size=0.2, random_state=42)
    
    user_resp = input("is the dataset imbalanced? (yes/no)")
    if user_response.lower()== "yes":
        # Apply SMOTE to the training data
        smote = SMOTE(random_state=42)
        X_resampled, y_resampled = smote.fit_resample(X_trainval, y_trainval)
        return X_resampled, y_resampled
    else:
        return X_trainval, X_test, y_trainval, y_test


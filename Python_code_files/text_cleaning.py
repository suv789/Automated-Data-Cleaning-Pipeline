import pandas as pd
import re

def clean_text_columns(df,columns=None):
    """Apply standardize text column cleaning to specified columns."""

    if columns is None:
         columns = df.select_dtypes(include=['object']).columns

    df = df.copy()

    for column in columns:
         if column not in df.columns:
             continue
         df[column] = (df[column]
                       .astype(str)
                       .str.strip()
                       .str.lower()
                       .replace(r'\s+', ' ', regex=True) # remove extra spaces
                       .replace(r'[^\w\s]', '', regex=True)) # remove special characters
    return df
         

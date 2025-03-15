import pandas as pd
from pathlib import Path

def load_dataset(file_path,**kwargs):
    '''load data from various file formats'''
    file_type = Path(file_path).suffix.lower()

    handlers = {
        '.csv': pd.read_csv,
        '.xlsx': pd.read_excel,
        '.pkl': pd.read_pickle,
        '.json': pd.read_json,
        '.parquet': pd.read_parquet
    }
    reader = handlers.get(file_type)
    if reader is None:
        raise ValueError('Unsupported file format')
    
    df = reader(file_path, **kwargs)
    #standardize column names\
    df.columns = df.columns.str.strip().str.lower()
    df = df.replace('',pd.NA)
    return df
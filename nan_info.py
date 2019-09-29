#SCRIPT TO GET INFO ABOUT UNIQUE VALUES AND NAN VALUES FOR EVERY COLUMN IN ORDER
#TO DYNAMICALLY HANDLE NANS

import pandas as pd 
import numpy as np 

PTH = 'D:/Machine Learning Datasets/titanic/train.csv'
df = pd.read_csv(PTH)

nan_info = {col:{'uniques': len(df[col].unique()), 'nan_count': df[col].isnull().sum()} for col in df.columns}
print(nan_info)
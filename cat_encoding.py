#GENERALIZED CODE FOR AUTOMATICALLY ENCODING CATEGORICAL VALUES IN A GIVEN DATASET IN PANDAS

import pandas as pd 
import numpy as np 

PTH = #ENTER PATH TO DATASET HERE
#READ CSV FILE, BE SURE TO INCLUDE WHICHEVER SPECIFICIATIONS NEEDED WHILE IMPORTING (E.G. DATEPART)
df = pd.read_csv(PTH)

#FIND COLUMNS WHOSE DTYPES ARE NOT NUMERICAL
cats = [col for col in df.columns if df[col].dtype == np.dtype('O')]

#ENCODE USING .CAT.CODES
for col in cats:
	df[col] = df[col].astype('category')
	df[col] = df[col].cat.codes

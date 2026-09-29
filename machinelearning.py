import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer 
data = pd.read_csv("datamachinelearning.csv")
print(data)
#step 1: check for missing data
print(data.isna().sum())
#step 2: clean dataset
object = SimpleImputer(missing_values=np.nan,strategy="mean")
object.fit(data.iloc[:,1:3])
data.iloc[:,1:3] = object.transform(data.iloc[:,1:3])
print(data)

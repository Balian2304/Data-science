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
#step 3: split data into features and target
X = data.iloc[:,0:3]
y = data.iloc[:,3]
#step 4: encoding, convert non-numeric to numeric (onehot encoding, label encoding)
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
object = ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[0])],remainder="passthrough")
X = object.fit_transform(X)
from sklearn.preprocessing import LabelEncoder
object2 = LabelEncoder()
y = object2.fit_transform(y)
print(X)
print(y)
# step 5: splitting the data into training data and testing data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.5,random_state=3)
print(X_train)
print(X_test)
print(y_train)
print(y_test)
import numpy as np
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')

## must 2-D Array
data = [[2,3,5,1,7,np.nan],[4,2,2,np.nan,4,2]]

## orginal data with nan values
print("Orginal Data: \n", data)

## apply mean stategy to impute and fill nan value with the mean(method)
imputer = imputer.fit(data)
data = imputer.transform(data)
print("Imputed Data: \n", data)

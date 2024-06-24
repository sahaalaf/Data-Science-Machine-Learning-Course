import numpy as np
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
data = [[2,3,5,1,7,np.nan],[4,2,2,np.nan,4,2]]
print("Orginal Data: \n", data)

imputer = imputer.fit(data)
data = imputer.transform(data)
print("Imputed Data: \n", data)

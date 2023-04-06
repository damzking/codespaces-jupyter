import pandas as pd


#Import models from scikit learn module:

col_names = ['age', 'workclass', 'fnlwgt','education', 'education-num', 
'marital-status', 'occupation', 'relationship', 'race', 'sex',
'capital-gain','capital-loss', 'hours-per-week','native-country', 'income']
df = pd.read_csv('atlantis.csv', header=None, names = col_names)
print(df.head())

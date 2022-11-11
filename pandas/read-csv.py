import pandas as pd

data = pd.read_csv('panda-foo.csv', sep='\t')
for row in data:
    print(row)

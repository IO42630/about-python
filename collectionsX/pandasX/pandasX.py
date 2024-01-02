import numpy as np
import pandas as pd

from helpers.helpers import pp

print('\nDF1')
df1 = pp(pd.DataFrame(
    {'col1': [1, 2], 'col2': [3, 4]}
))

print('\nDF2')
df2 = pp(pd.DataFrame(
    np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    columns=['a', 'b', 'c'])
)

print('\nDF3')
df3 = pp(pd.read_csv('./test_data.csv'))


#
pp(df3.columns)
pp(df3.iloc)
pp(df3.loc)
pp(df3.shape)
pp(df3.values)


pp(df3.apply(lambda x: x + 1, 1))
pp(df3.describe())
# drop()
# groupby()
# head()
pp(df3.info())
# isnull()
# sort_values()
# value_counts()
# where()




print('\nSLICING')
df3.index = ['row1', 'row2']
pp(df3.loc['row1'])
pp(df3.loc[['row1', 'row2']])
pp(df3.loc[:'row2'])
pp(df3.iloc[0])

print('\nCOLUMN SELECTION')

print(df3['C'])
print(df3[['A', 'C']])
pp(df3.A)



pp(df3.loc[:, ['B', 'C']])
pp(df3.loc[['row1', 'row2'], ['B', 'C']])


print(df3.iloc[:, [1,2]])

print(df3.loc[df3.index[0:3], 'B'])




clothes = pd.DataFrame({'type': ['pants', 'shirt', 'shirt', 'pants', 'shirt', 'pants'],
                        'color': ['red', 'blue', 'green', 'blue', 'green', 'red'],
                        'price_usd': [20, 35, 50, 40, 100, 75],
                        'mass_g': [125, 440, 680, 200, 395, 485]})

print(clothes)

clothes.to_csv('./clothes.csv', index=True)
clothesRedux = pp(clothes[['type', 'price_usd', 'mass_g']])


group = clothesRedux.groupby('type' ) # just a DataFrameGroupBy object
pp(group.mean()) # can perform operations on it

pp(clothes[['price_usd', 'mass_g']].agg(['sum', 'mean']))

pp(clothes.groupby('color').agg({'price_usd': ['mean', 'max'],
                                 'mass_g': ['mean', 'max']}))


grouped = clothes.groupby(['color', 'type']).agg(['mean', 'min'])


clothes.groupby(['color', 'type'], as_index=False).mean()


print('COMBINE')
df3.merge(df4, on='A', how='left')
df3.concat(df4, axis=0)
df3.join(df4, on='A', how='left')

print('\nEXTRACT (columns)')
var = df3[['animal', 'legs']]  # select columns
df2 = df2.select_dtypes(include=['int64'])

print('\nFILTER (rows)')
df2= df2[df2['class']=='Aves']


df3.sort_values(by=['legs'], ascending=False)
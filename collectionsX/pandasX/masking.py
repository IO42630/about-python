print('\nMASKING')
mask = pp(df3['B'] > 2)         # construct mask
filtered = pp(df3[mask])        # apply mask

print('\nDF4')
df4 = pd.concat([df3, 2* df3, df3], axis=0)
df4.index = ['row1', 'row2', 'row3', 'row4', 'row5', 'row6']
pp(df4)

# masking operators: |, &, ~ (or, and, not)
mask2 = (df4['A'] < 2) & ~ (df4['B'] > 4)     # construct mask
pp(df4[mask2])     # apply mask
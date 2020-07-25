i = [1,2,3]   # create the list instance, and bind it to i
j = i         # bind j to the same list as i
i[0] = 5      # change the first item of i
print( j)       # j is still bound to the same list as i


test = { 'one' : 'two'}
print(test)

test.update({'one' : 'tree'})

print(test)

test['one']='four'

print(test['one'])
print(test)

print(test.get('two'))

arr = [1,2]

print([arr[1]])
print([arr[4]])
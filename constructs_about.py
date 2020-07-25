# LISTS
# ------------------------------------------------------------------------------
a = ['a1', 'a2', 'a3', 'a4']
b = ['b1', 'b2', 'b3']
c = [b, a]

print(a[1:3])
print(c)

print(c[1][1])

# You add values using append
a.append('onions')
print(c)

# Insert item at given index
a.insert(1, "Pickle")

# Remove item from list
a.remove("a1")

# Sorts items in list
a.sort()

# Reverse sort items in list
a.reverse()

# del deletes an item at specified index
del a[4]
print(c)

# We can combine lists with a +
c = b + a
print(c)

# Get length of list
print(len(c))

# Get the max item in list
print(max(c))

# Get the minimum item in list
print(min(c))

# TUPLES
# ------------------------------------------------------------------------------
# Values in a tuple can't change like lists

pi_tuple = (3, 1, 4, 1, 5, 9)

# Convert tuple into a list
new_tuple = list(pi_tuple)

# Convert a list into a tuple
# new_list = tuple(a)

# tuples also have len(tuple), min(tuple) and max(tuple)


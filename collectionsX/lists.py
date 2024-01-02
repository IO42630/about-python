# LISTS
# ------------------------------------------------------------------------------
a = ['a1', 'a2', 'a3', 'a4']
b = ['b1', 'b2', 'b3']
c = [b, a]

print(a[1:3])
print(c)

print(c[1][1])

# You add values using append
a.append('apple')
print(c)

# Insert item at given index
a.insert(1, "orange")
print(c)

# Remove item from list
a.remove("a1")
a.append("a1")
a.pop(3) # remove & return
print(c)

# Sorts items in list
a.sort()
print(c)

# Reverse sort items in list
a.reverse()
print('08 ' + str(c))

# del deletes an item at specified index
del a[4]
print('09 ' + str(c))

# We can combine lists with a +
c = b + a
print(c)


print(f'14 - {len(c)} {max(c)} {min(c)}')

c.clear()


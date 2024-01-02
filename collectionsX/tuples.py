# TUPLES
# ------------------------------------------------------------------------------
# Values in a tuple can't change like lists

pi_tuple = (3, 1, 4, 1, 5, 9)

# Convert tuple into a list
new_tuple = list(pi_tuple)

# Convert a list into a tuple
# new_list = tuple(a)

# tuples also have len(tuple), min(tuple) and max(tuple)


print((1, 2))               # (1, 2)
print((1, ) + (1, 2))       # (1, 1, 2)
print(() + (1, 2))          # (1, 2)


# zip
letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
zipped = zip(letters, numbers)       # [('a', 0), ('b', 1), ('c', 2)]
print(list(zipped))
scientists = [('Nikola', 'Tesla'), ('Charles', 'Darwin'), ('Marie', 'Curie')]
given_names, surnames = zip(*scientists)
print(given_names)
print(surnames)

letters = ['a', 'b', 'c']
for index, letter in enumerate(letters):
    print(index, letter)

letters = ['a', 'b', 'c']
for index, letter in enumerate(letters, 2):
    print(index, letter)


# List comprehensions
numbers = [1, 2, 3, 4, 5]
new_list = [x + 10 for x in numbers]
print(new_list)

words = ['Emotan', 'Amina', 'Ibeno', 'Sankwala']
new_list = [(word[0], word[-1]) for word in words if len(word) > 5]
print(new_list)

tuple((1, 2, 3))            # (1, 2, 3)
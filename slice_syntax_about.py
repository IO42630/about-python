a = [1, 2, 3, 4, 5, 6]
start = 1
end = 4

print(a[start:end])  # items start through end-1
a[start:]  # items start through the rest of the array
a[:end]  # items from the beginning through end-1
a[:]  # a copy of the whole array

test = [1, 2, 3, 4, 5, 6]

pos = 4
test = test[:pos] + test[pos:]
print(test)
print(test[:pos])
print(test[pos + 1:])

print('test')

test = [1, 2, 3, 4, 4, 5, 6, 6, 6]
print(test)
for x in test[:len(test) - 1]:
    x_postion = test.index(x)
    y = test[x_postion + 1]
    if x == y:
        # remove x
        test = test[:x_postion] + test[x_postion + 1:]

print(test)

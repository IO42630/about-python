import numpy as np

from helpers.helpers import pp


np.array([1, 2, '3'])
a1d: int = pp(np.array([1, 2, 3]))
a2d = pp(np.array([(1, 2, 3), (4, 5, 6)]))
a3d = pp(np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]))

print(np.zeros((3, 3)))
print(np.ones((3, 3)))
print(np.full((3, 3), -1))


a2dtr = np.transpose(a2d)

a2dre = np.reshape(a2d, (3, 2))

a2list = a2d.tolist()


print(a3d.max())
print(a3d.max(2))

print(a3d.min())
print(a3d.mean())
print(a3d.sum())
print(a3d.std())

print(a3d.shape)
print(a3d.dtype)
print(a3d.size)
print(a3d.T)


print("\nK3: INDEXING AND SLICING =============")

a = np.array([(1, 2, 3), (4, 5, 6)])
print(a)
print()

print(a[1])
print(a[0, 1])
print(a[1, 2])

a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(a)
print()

print(a[:, :])
print(a[:, 1:])


a = np.array([(1, 2, 3), (4, 5, 6)])
b = np.array([[1, 2, 3], [1, 2, 3]])
print('a:')
print(a)
print()
print('b:')
print(b)
print()
print('a + b:')
print(a + b)
print()
print('a * b:')
print(a * b)



# contetnts of arrays can be chaged, but the grid itself is fixed
# numpy also uses some memory optimization techniques
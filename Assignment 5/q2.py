import numpy as np

array1 = np.array([10, 52, 62, 16, 16, 54, 453])

print(np.sort(array1))
print(np.argsort(array1))
print(np.sort(array1)[:4])
print(np.sort(array1)[-5:])

array2 = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
print(array2[array2 == array2.astype(int)])
print(array2[array2 != array2.astype(int)])

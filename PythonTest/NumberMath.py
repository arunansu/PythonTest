import numpy as np

array = np.array([1,4,5,8], float)
print array
print "array[1]"
print array[1]
print "array[:2]"
print array[:2]
print "array[1] = 5.0"
array[1] = 5.0
print array[1]
array = np.array([[1,2,3], [4,5,6]], float)
print array
print "array[0][1]"
print array[0][1]
print "array[1, :]"
print array[1, :]
print "array[:, 2]"
print array[:, 2]
array1 = np.array([[1, 2], [3, 4]], float)
array2 = np.array([[5, 6], [7, 8]], float)
print array1
print array2
print "array1 + array2"
print array1 + array2
print "array1 - array2"
print array1 - array2
print "array1 * array2"
print array1 * array2
array1 = np.array([1,2,3], float)
array2 = np.array([[6], [7], [8]], float)
print array1
print "mean"
print np.mean(array1)
print "median"
print np.median(array1)
print "std"
print np.std(array1)
print array2
print "mean"
print np.mean(array2)
print "np.dot(array1, array2)"
print np.dot(array1, array2)
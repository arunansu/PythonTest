import numpy as np
print(np.empty( (5,1))) #5 rows, 1 column empty array
print(np.empty((5,4,3))) #Empty array with 5 rows, 4 column and 3 depth
print(np.ones((5,4), dtype=np.int_)) #Array of 1s with 5 rows and 4 columns
print(np.random.random((5,4))) #array of random numbers from 0.0 to 1.0
print(np.random.rand(5,4)) #same as np.random.random with different syntax
print(np.randm.normal(size=(2,3))) #normal distribution matrix with mean 0 and s.d 1
print(np.random.normal(50, 10, size=(2,3))) #normal distribution matrix with mean 50 and s.d. 10
print(np.random.randint(10)) #a single integer in 0 to 10
print(np.random.randint(0, 10)) #same as abobe with explicit low and high
print(np.random.randint(0, 10, size=5)) #5 random integers as 1D array
print(np.random.randint(0, 10, size=(2,3))) #2x3 array of random integers
a = np.random.rand(5,4)
print(a.shape) #Gives shape of the array like (5,4)
print(len(a.shape)) #Dimension of the array = 2
print(a.shape[0]) #rows of the array = 5
print(a.shape[1]) #columns of the array = 4
print(a.size) #number of elements in the array
print(a.dtype) #datatype of elements of the array
print(a.sum()) #sum of all elements in array
print(a.sum(axis=0)) #sum of reach column
print(a.sum(axis=1)) #sum of each row
print(a.max(axis=0)) #max of each column
print(a.max(axis=1)) #max of each row
print(a.argmax()) #index of maximum 
t1 = time.time() #current time
t2 = time.time() #time later 
print(t2 - t1) #time gap
print(a[:, 0:3:2]) #print 0 and 2 column of each row, 2 is step size

array = np.array([1,4,5,8], float)
print(array)
print("array[1]")
print(array[1])
print("array[:2]")
print(array[:2])
print("array[1] = 5.0")
array[1] = 5.0
print(array[1])
array = np.array([[1,2,3], [4,5,6]], float) #np.array([(1,2,3), (4,5,6)], float)
print(array)
print("array[0][1]")
print(array[0][1])
print("array[1, :]")
print(array[1, :])
print("array[:, 2]")
print(array[:, 2])
array1 = np.array([[1, 2], [3, 4]], float)
array2 = np.array([[5, 6], [7, 8]], float)
print(array1)
print(array2)
print("array1 + array2")
print(array1 + array2)
print("array1 - array2")
print(array1 - array2)
print("array1 * array2")
print(array1 * array2)
array1 = np.array([1,2,3], float)
array2 = np.array([[6], [7], [8]], float)
print(array1)
print("mean")
print(np.mean(array1))
print("median")
print(np.median(array1))
print("std")
print(np.std(array1))
print(array2)
print("mean")
print(np.mean(array2))
print("np.dot(array1, array2)")
print(np.dot(array1, array2))
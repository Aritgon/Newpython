import numpy as np

# basic numpy.
array = np.array([1,2,3,4,5])
# print(array.ndim) # this will print dimensions of the array.

array1 = np.array([[1,2,3], [4,5,6]])
# print(array1.ndim)
# print(array1[0,1] + array1[1,1]) # sum of 2 elems with slicing.

arr = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
# print(arr.ndim)
# print(arr[1,1,0]) #10.

arr = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print(arr.ndim) # 3 dimensions.
print(arr.dtype) # datatype.
# array iteration with numpy.
for a in np.nditer(arr[0:, 0:, 2]):
    print(a)
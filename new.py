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
# print(arr.ndim) # 3 dimensions.
# print(arr.dtype) # datatype.
# array iteration with numpy.
# for a in np.nditer(arr[0:, 0:, 2]):
#     print(a)

array = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# flatting an 2-D array
# with (-1) we can flatten every dimension array.

# newarr = array.reshape(-1)
# print("before flatting", array)
# print("after flattening", newarr)

# ndenumerate prints out the sequence of the elements of an array and also the sequence of the array.
for x,y in np.ndenumerate(array):
    print(f"{x} -> {y}")

for id, x in np.ndenumerate(array[0:, 2]):
    print(f"{id} -> {x}")
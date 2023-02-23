import numpy as np

# n-dimensional array

# my_array = np.arange(8)
# my_array = np.arange(1,10,2)
# my_array = np.arange(-1,10,.3)
# print(my_array)
# print(type(my_array))

from_list = np.array([1, 2, 3], dtype=np.int8)

# print(from_list)
# print(type(from_list))
# print(type(from_list[0]))
# output is <class 'numpy.int32'> indicating that it is an integer that takes up 32 bits
# add dtype=np.int8 and it becomes <class 'numpy.int8'>

# 2-d -option one

from_list = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int8)
# print(from_list)
# 2-d -option two
array_2d = np.array((np.arange(0, 8, 2), (np.arange(1, 8, 2))))

# print(array_2d)
# print("shape of array:",array_2d.shape)

array_2d = array_2d.reshape((4, 2))
# print(array_2d)
# print("shape of array:",array_2d.shape)


# empty arrays

# https://www.youtube.com/watch?v=lLRBYKwP8GQ

# https://www.youtube.com/watch?v=4IFq7_s9NEA

empty_arrays = np.zeros((2, 2))

# print(empty_arrays)
empty_arrays = np.ones((2, 2))
# print(empty_arrays)
empty_arrays = np.empty((2, 2))
# careful empty is not the same, it will return random values if you change the shape.
# print(empty_arrays)
# changing shape
empty_arrays = np.empty((2, 2, 2))
# print(empty_arrays)

# ways to create eigenvalues/vectors
eye = np.eye(3)
# print(eye)
identity = np.identity(3)
# print(identity)

# you can shift the diagonal by adding a k =value , K=1 for right handed /above shifts, k = -1 for left handed /below shifts

eye = np.eye(3, k=-1)
print(eye)

# how to change values in arrays/ matrix
# how to filter out values and exchange them for something else:
eye[eye == 0] = 2
print(eye)
# cant seem to save this as a new matrix, need to make a copy first and change that?
# can filter out values < or > a number
eye[eye < 2] = 9
print(eye)

# can I do !=?
eye[eye != 2] = 6
print(eye)
# yup

# how to change a row, matrix[0] is first row, matrix [1] is second row and so on
eye[0] = 2
print(eye)
# replace whole row
eye[0] = 1, 2, 3
print(eye)
# replace multi rows, this can be set = to a single number (eye[0:2]=3) or you can overwrite each row with the same numbers eye[0:2]=[1,2,3].
eye[0:2] = [1, 2, 3], [4, 5, 6]
print(eye)
# how to change a column, you have to open a filter command [] select all rows[:]+ "," then add in the column you wish to change after a comma. again you
# can enter single digits or a whole new set of values.
eye[:, 0] = 1, 2, 3
print(eye)

# how to change sections of the array: open filter command [], select the rows ":"+ ","  + ":" + select columns
eye[1:, :1] = 10
print(eye)

# example 2 of this
# selecting every row but the last ":-1" , selecting every column after and including the second "1:"
eye[:-1, 1:] = 13, 15
print(eye, "\n")

# x=eye[:-1,1:] =15
# print(x)
# still cant save it
# how to sort rows
# now I can save it?
sorted_eye = np.sort(eye)
print(sorted_eye)

# sort by column
sorted_eye = np.sort(eye, axis=0)
print(sorted_eye)

# this default is quick sort, there is also mergesort, and heapsort...this is not covered in this tutorial.

# copy arrays- humm
# view will change the original as well as the new if you make changes to the my_view later
my_view = sorted_eye.view()
# or
# copy will maintain the original
my_copy = sorted_eye.copy()

# make an arrary 3x3 all = to 2
a = np.zeros((3, 3), dtype=np.int32)
a[:] = 2
#print(a.dtype)
# turning array 1d into 2d

b = np.arange(1, 10).reshape((3, 3))

#print(b.dtype)

# methods
a.fill(8)  # assigns automatically, no need to save as a new variable
a+=3
a-=3
a*=3
#dont do "/=" if the data type is dtype=np.int32
a = np.zeros((3, 3))
a[:] = 2
a.fill(8)  # assigns automatically, no need to save as a new variable
a+=3
a-=3
a*=3
a /= 6.2 #######6/28 min

print(a)
#print(b)


a = np.zeros((3, 3), dtype=np.int32)
a[:] = 3
#sum an array
array_sum = a.sum()
print(array_sum)

#sum columns  (axis=0)
array_sum = b.sum(0)
print(array_sum)
#pythonic sum columns
array_sum = b.sum(axis=0)
print(array_sum)

# sum of rows    (axis=1)
array_sum = b.sum(1)
print(array_sum)
#pythonic sum rows
array_sum = b.sum(axis=1)
print(array_sum)

#product 8.45/28 min
array_prod = b.prod()
print(array_prod)

#average/mean
array_average = b.mean()
print(array_average)

#max/min
array_max,array_min = b.max(),b.min()
print(array_max, array_min)

#index of min/max
array_max_indx,array_min_indx = b.argmax(),b.argmin()
print(array_max_indx, array_min_indx)

#peak to peak = max-min
peak_to_peak = b.ptp()
print()

#flatten array into a line
array_flat = b.reshape(b.size)
# or array_flat =b.flatten()
#or array_flat =b.ravel() () carful this is a view version, it will change the original.
print(array_flat)

#repeat
array_repeat = np.repeat(255,3)
print(array_repeat)
array_repeat = np.repeat(b,3)
print(array_repeat)
array_repeat = np.repeat(b,3,axis = 1)
print(array_repeat)
array_repeat = np.repeat(b,3,axis = 0)
print(array_repeat)









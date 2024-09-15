import array

# array module in python supports only 1-D array and is limited to int,float and chars data type
# Time complexity:
# Appending and accessing or initialising an array is O(1)
# Inserting ,Iterating is O(n)
my_array = array.array('i');
print(my_array)
my_array1 = array.array('i',[1,2,3,4,5,6,7,8,9,10])
print(my_array1)

# Numpy library supports 2D,3D etc array and is faster for complex operations as it is written in C language 
# Time complexity:
# Appending and accessing or initialising an array is O(1)
# Inserting ,Iterating is O(n)

import numpy as np
np_array = np.array([],dtype=int)
print(np_array)
np_array1=np.array([2,3,4,6,7,3])
print(np_array1)

# Still for more complex operations we have to use numpy library as it much faster 


# Space complexity of both array and numpy is 0(n) but numpy uses memory more effeciently as compared to array So Numpy use Krna h bruh!!
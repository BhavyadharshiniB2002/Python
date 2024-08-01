
#numpy
#list items
'''import numpy
arr=numpy.array([1,2,3,4,5,6,7,8,9,10])
print(arr)
print(arr[1])
print(arr[2]+arr[3])
print(arr[1:5])
print(arr[4:])
print(arr[:4])
print(arr[-3:-1])
print(arr[1:10:2])'''

#types
'''import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
a=[]
print(type(a))
print(type(arr))'''

#np versio
'''import numpy as np
print(np.__version__)
arr=np.array([[1,2,3],[4,5,6]])
print(arr)
print("2nd element on 1st row:",arr[0,1])'''

#dimensional array
'''import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0,2])
print("1.",arr[1,1:4])
print("2.",arr[0:2,2])
print("2.",arr[0:2,1:4])'''

# The nested for loop create that the dimension depend 
# How many dimension and create more than for loops 
'''import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("4.",arr)
print("5.",arr[0,1,2])
'''
# Task1
'''import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
for i in arr:
        for j in i:
              for k in j:
                    print(k)'''

# Task2
''''import numpy as np
arr=np.array([[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]]])
for i in arr:
        for j in i:
               for k in j:
                       for l in k:
                             print(l)'''




from numpy import *

arr = array([
    [1,2,3],
    [2,3,4],
    [7,8,9]

])

print(arr)

print(arr.dtype)

print(arr.size) #no of elements


print(arr.ndim) #no of dimension

print(arr.shape) # no row and column in tuple

# one 2d array to 1d arr
arr2= arr.flatten()
print(arr2)

# Reshaping the array
arr3=arr2.reshape(3,3)
print(arr3)

m = matrix(arr3)
print(m)

print("mimimum elements in python")
print(m.min())



print("Diagonal elements in python")
print(diagonal(m))

print("maximum elements in python")
print(m.max())

print("transpose elements in python")
print(m.transpose())


print('matrix P initilization')
p = matrix('1 2 3 ; 2 5 6')
print(p)

print('matrix q initilization')
q= matrix('1 2 3 ; 2 5 6 ; 8 9 5')
print(q)

'''print("Addtion of two matrix")
r= p+q
print(r)'''

print("Multiplication of two matrix")
z= p*q
print(z)
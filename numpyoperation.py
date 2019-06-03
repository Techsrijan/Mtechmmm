from numpy import *
import time
arr = array([1,2,3,4,5])
arr = arr+10
print(arr)

arr =arr *5
print(arr)

arr1 =  array([1,2,3,4,5])
arr2 = array([1, 2, 3, 4, 5])
arr3 = arr1 + arr2
print(arr3)

print(concatenate([arr1,arr2]))



''' copy an array to another arrray'''
''' aliasing '''
arr4 = arr1
print(arr4)

print(id(arr4))
print(id(arr1))
''' copy '''
''' what if you want to create a different array with same content'''
print('what if you want to create a different array with same content')
arr5= arr1.view()
print(arr5)

print(id(arr5))
print(id(arr1))

''' shallow copy exp'''
arr5[4]=50000
print(arr5)
print(arr1)

''' shallow copy'''
print('shallow copy')
arr1[1] =500
print(arr1)
print(arr4)


''' "if we change in another then change occurs in both"'''
arr4[0]=6000
print(arr4)
print(arr1)


''' deep copy'''
print('Deep copy')
arr6= array([4,5,8,9,7,8])
arr7 = arr6.copy()
print(arr7)
print(arr6)
print(id(arr6))
print(id(arr7))
arr6[3]=45555
print(arr6)
print(arr7)


print('aa')
print(min([arr6]))



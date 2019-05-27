from numpy import *
import time
arr = array([1,2,3,4,5])
print(arr)
for e in arr:
   # time.sleep(2)
    print(e)

print(arr.dtype)

arr1 =array([1,2,3,4,5.5])
print(arr1.dtype)
print(arr1)

arr2 = array([1,2,3,4,5],float)
print(arr2.dtype)
print(arr2)

arr3 =array([1,2,3,4,5.5],int)
print(arr3.dtype)
print(arr3)


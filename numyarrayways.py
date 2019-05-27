'''
there are 6 ways to create an array using numpy
1. array()
2. linespace()
3.  logspace()
4. arange()
5. zeros()
6. ones()


'''
from numpy import *
import time

''' array ()'''
arr = array([1,2,3,4,5])
print(arr)

''' linspace()'''

arr1 =linspace(1,15,15)
print(arr1)

''' linespace(start,stop,noofdivision)
by default noofdivision=50
'''
arr2 =linspace(0,15)
print(arr2)

''' logspace()'''

arr3 =logspace(1,40,5)
print(arr3)

'''zeros'''

arr4= zeros(10)
print(arr4)


''' ones'''
arr5 = ones (5,int)
print(arr5)

'''arange()'''
arr6 = arange(1,15)
print(arr6)


arr7 = arange(1,15,2)
print(arr7)
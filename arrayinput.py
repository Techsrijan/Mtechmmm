from array import *

arr=array('i',[]) # creates an empty array

length = int(input("enter the no  of students"))

for i in range(length):
    n = int(input("enter the marks of students"))
    arr.append(n)

for maria in arr:
    print(maria)
#import array
from array import *
value=array('i',[45,6,7,8,9])
print(value)
print(value.buffer_info())
print(value.typecode)
for i in range(5):
    print(value[i],end="")

print("by using length")
for i in range(len(value)):
    print(value[i],end="")

print("another special way for an array")
for maria in value:
    print(maria)

charr = array('u', ['a','s','h','w','a','n','i'])
for maria in charr:
    print(maria)
print('create a new array with the same value')
newarr = array(charr.typecode,(a for a in charr))

for maria in newarr:
    print(maria)
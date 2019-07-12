import nameexpspecial
'''
https://www.guru99.com/date-time-and-datetime-classes-in-python.html
'''
import time as t
#return no of second from 1970 to today
print(t.time())
print(t.localtime(t.time()))
print(t.asctime(t.localtime(t.time())))
print(t.mktime(t.localtime(t.time())))
print(t.clock())

lst = [3,4,5,6,7,8,7]

for i in lst:
    print(i)
    t.sleep(1)

print("Module name=",__name__)






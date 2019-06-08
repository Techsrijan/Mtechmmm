from functools import reduce
'''def cube(x):
    return x**3

print(cube(5))'''

# function without name is called anonymous function
f= lambda x:x**3

res=f(5)
print(res)

# in python functions are objects


f1= lambda p,q:p+q

res1=f1(5,5)
print(res1)


# filter , map and reduce


'''def even(a):
    return a%2==0'''
#filter
num = [3,44,6,2,7,9,55,66]
even=list(filter(lambda n:n%2==0,num))

print(even)
#map
triple=list(map(lambda a:a*3,even))

print(triple)

#reduce
sum= reduce(lambda a,b:a+b ,triple)
print(sum)

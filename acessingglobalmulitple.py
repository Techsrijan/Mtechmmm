a=10
print(id(a))
b=20

def test():
    a=20
    print(a)
    print(id(a))
    #we need global and local variable in same function
    x=globals()['a']
    print(x)
    print(id(x))

test()
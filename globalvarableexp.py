
a = 50 #global varable

def inc():
    a = 10 #local varable
    print('inc=',a)

def dec():
    #a = 10
    print(a)
    

print('global=',a)
inc()
#dec()
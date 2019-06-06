def getList(lst):
    even =0
    odd=0
    for i in lst:
        if i%2==0:
            even=even+1
        else:
            odd=odd+1

    return even,odd

lst = [1,5,6,7,8,12,99,108,107]
even,odd=getList(lst)
print("even=",even)
print("odd=",odd)
print("even={} snd odd:{}".format(even,odd))
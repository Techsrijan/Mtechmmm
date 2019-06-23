#f=open("myfile","r")
# read() reads all data in file
#print(f.read())

# readline() reads first line of file
#print(f.readline())

# readline(3) reads 3 charater of file
#print(f.readline(3))

f1=open("Techfile","r")
#f1.write("Dekhiya likha gaya")
#f1.write("Kya mazak hi")
#f1.write("Ab aggae likhega mitega nahi peeche wala")
f2=open("Copyfile","w")
for data in f1:
    print(data)
    f2.write(data)
    print("file wriiten")


 # opening an image file
f3 = open("Koala.gif", "rb")
f4 = open("Gola.gif", "wb")
for data in f3:
    print(data)
    f4.write(data)
    print("duplicate image created ")








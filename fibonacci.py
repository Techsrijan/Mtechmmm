num = int(input("enter num of terms: "))
first = 0
second = 1
i = 0
while i < num:
    third = first + second
    first = second
    second = third
    print(third)
    i = i + 1
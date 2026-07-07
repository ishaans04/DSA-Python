def reversal(n):
    new_num=0
    while n>0:
        last_num=n%10
        new_num = (new_num * 10) + last_num
        n//=10

    return new_num

i=int(input("Enter the number"))
print("The reversed Number is ", reversal(i))

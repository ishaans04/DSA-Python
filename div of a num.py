def check_div(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)
    return 1

x=int(input("Enter number : "))
check_div(x)
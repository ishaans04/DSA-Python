def check_arm(n):
    org=n
    t=len(str(n))
    sum=0

    while n>0:
        last_dig=n%10
        sum+=last_dig**t
        n//=10

    return sum==org

x=int(input("Enter a number to check if it is armstrong : "))
if check_arm(x):
    print("Yes")
else:
    print("No")





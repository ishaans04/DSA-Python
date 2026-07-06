def pattern2(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=' ')
        print()
n=int(input("Enter your number"))
pattern2(n)
n=int(input("Enter your number"))
pattern2(n)
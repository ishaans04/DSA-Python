def pattern10(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print()

    for i in range(1,n+1):
        for j in range(n-i-1):
            print("*",end=" ")
        print()

pattern10(5)

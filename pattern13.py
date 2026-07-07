'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''




def pattern13(n):
    c=1
    for i in range(1,n+1):
        for j in range (1,i+1):
            print(c, end = " ")
            c+=1
        print()


x=int(input("Enter The number of rows you want"))
pattern13(x)
        
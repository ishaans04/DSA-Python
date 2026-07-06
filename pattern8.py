'''
Inverted Pyramid of *
[space,*,space]

0->[0,9,0]
1->[1,7,1]
2->[2,5,2]
3->[3,3,3]
4->[4,1,4]  

stars=[2n-(2i+1)]

'''

def pattern6(n):
    for i in range(n):
        for j in range(i):
            print(' ', end=" ")
        for j in range((2*n)-((2*i)+1)):
            print('*',end=" ")
        for j in range(i):
            print(' ', end=" ")
        print()

pattern6(5)

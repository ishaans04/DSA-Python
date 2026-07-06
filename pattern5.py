'''
            * * * * *
            * * * *
            * * *       (n= number of rows)
            * *
            *

            1->5
            2->4
            3->3    (n-row+1)
            4->2
            5->1   
'''

def pattern5(n):
    for i in range(1,n+1):
        for j in range(n-i+1):
            print('*', end=' ')
        print()


pattern5(5)
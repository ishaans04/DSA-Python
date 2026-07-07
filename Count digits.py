''' Count digits in a number '''
#Brute Force
def count_dig(n):
    c=0
    while n>0:
        c+=1
        n=n//10
    return c

num=int(input("Enter The number"))
print("The number of digits in ",num," are ",count_dig(num))

    
#Optimal approach

import math
def count_opt(n):
    c = int(math.log10(n)+1)
    return c 

n=int(input("Enter Number"))
print(count_opt(n))


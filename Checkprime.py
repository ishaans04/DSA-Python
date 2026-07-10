##Brute force 
def check_prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
        
    return c==2

x=int(input("Enter a number : "))
y=check_prime(x)

if y:
    print(x, "Is a prime number")
else:
    print("Not a prime number")

##Optimal approach  

def check_prime2(n):
    c=0
    for i in range (1,int(n**0.5)+1):
        if n%i==0:
            c+=1

            if n//i!=i:
                c+=1
        
    return c==2

t=int(input("Enter a number "))
y=check_prime2(t)

if y:
    print(x , "is prime number ")
else:
    print("Not prime")

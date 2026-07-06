def pushz(arr):

    n=len(arr)
    count=0

    for i in range (n):
        if arr[i]!=0:
            arr[count]=arr[i]
            count+=1

    while count<n:
        arr[count]=0
        count+=1

if __name__=='__main__':
    x=[3,4,0,5,4,1,0,6,9]
    n=len(x)
    pushz(x)
    for i in x:
        print(i, end = ' ' )



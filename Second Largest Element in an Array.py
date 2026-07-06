def secondlargest(arr):
    n=len(arr)
    
    lar=0
    slar=0

    for i in range(n):
        if arr[i]>lar:
            slar=lar
            lar=arr[i]
        
        elif arr[i]<lar and arr[i]>slar:
            slar=arr[i]

    return slar

if __name__=="__main__":
    arr=[10,20,30,5,6,7]
    print(secondlargest(arr))


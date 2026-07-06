def reversalarr(arr):
    n=len(arr)
    
    left = 0
    right = n-1

    while left<right:
        arr[left] , arr[right] = arr[right] , arr[left]

        left+=1
        right-=1

if __name__=='__main__':
    arr=[10,33,4,5,6,69]
    reversalarr(arr)
    n=len(arr)

    for i in range(n):
        print(arr[i],end=' ')

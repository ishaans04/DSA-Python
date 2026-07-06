def countmax(arr):
    maxct , ct = 0 , 1
    n=len(arr)

    for i in range(1,n):
        if arr[i]==arr[i-1]:
            count+=1
        
        else:
            maxct=max(ct,maxct)

    
    return max(maxct,ct)

if __name__ == '__main__':
    arr=[1,0,1,1,0]
    print(countmax(arr))
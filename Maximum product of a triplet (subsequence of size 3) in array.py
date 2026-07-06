def tripleprod(arr):
    n=len(arr)

    max1 = float('-inf')
    max2 = float('-inf')
    max3 = float('-inf')

    min1 = float('inf')
    min2 = float('inf')

    for i in range (n):

        if arr[i]>max1:
            max3=max2
            max2=max1
            max1=arr[i]

        elif arr[i]>max2:
            max3=max2
            max2=arr[i]

        elif arr[i]>max3:
            max3=arr[i]
        
        if arr[i]<min1:
            min2=min1
            min1=arr[i]

        elif arr[i]<min2:
            min2=arr[i]

    return max(min1 * min2 * max3 , max1 * max2 * max3)

if __name__ == '__main__':
    arr=[2,4,-3,5,8]
    print(tripleprod(arr))

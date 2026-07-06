def thirdlargest(arr):
    n=len(arr)

    first=float('-inf')
    sec=float('-inf')
    third=float('-inf')

    if n<3:
        print(arr[-1])

    for i in range(n):
        if arr[i]>first:
            third=sec
            sec=first
            first=arr[i]
        
        elif arr[i]>sec:
            third=sec
            sec=arr[i]

        elif arr[i]>third:
            third=arr[i]

    return third

if __name__=='__main__':
    arr=[3,5,88,99,56]
    print(thirdlargest(arr))
            





    
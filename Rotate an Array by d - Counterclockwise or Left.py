def rotatearr(arr,d):
    n = len(arr)

    d%=n #(If d is greater than size of array then suppose n=6 & d=8 so 8%6=2 same as 2 rotations)

    reverse(arr,0,d-1)

    reverse(arr, d, n-1)

    reverse(arr, 0, n-1)


def reverse(arr, start, end):
    while start<end:
        arr[start], arr[end] = arr[end], arr[start]

        start+=1
        end-=1

if __name__=='__main__':
    
    arr=[1,3,4,5,6]
    d=2

    n = len(arr)
    rotatearr(arr,d)

    for i in range(n):
        print(arr[i],end = ' ')

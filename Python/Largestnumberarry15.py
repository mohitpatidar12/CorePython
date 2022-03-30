def largest (arr,n):
    max = arr[0]
    for i in range (1,n):
        if arr[i]>max:
            max=arr[i]
    return max

arr = [20,66,545,87,100,8887]
n = len(arr)
ans = largest(arr,n)
print("largest array ",ans)
def good_pair(arr,target):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                return 1
    return 0
a=list(map(int,input().split()))
b=int(input())
result=good_pair(a,b)
print(result)


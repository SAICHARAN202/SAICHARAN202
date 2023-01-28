def binary_search(n, arr, target):
    low = 0  
    high = n - 1 
    while low <= high:
        mid = (low + high) // 2 
        if arr[mid] == target :
            return mid 
        elif arr[mid] > target:
            low = mid + 1 
        else:
            high = mid - 1 
    return -1 
n = int(input())
arr = [int(x) for x in input().split()]
target = int(input())
print(binary_search(n, arr, target))
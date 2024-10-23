def binarySearch(arr, target):
    low=0
    high=len(arr)-1
    while low <= high:   
        mid = (low + high) // 2     
        if(arr[mid] == target):
            return mid
        elif(arr[mid] > target):
            high = mid-1           
        else:
            low = mid + 1 
    return -1

    # return binarySearchRec(arr, target, low, high)


# Recursion

def binarySearchRec(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarySearchRec(arr, target, low, mid-1)
    else:
        return binarySearchRec(arr, target, mid+1, high)

n = binarySearch([2,6,13,22,36,51,75], 13)
print(n)
        
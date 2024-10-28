def quickSort(arr):
    qshelper(arr, 0, len(arr)-1)

def qshelper(arr, start, end):
    if(start >= end):
        return
    
    pivot = start
    left = start + 1
    right = end

    while right >= left:

        if arr[left] > arr[pivot] and arr[right] < arr[pivot]:
            arr[left], arr[right] = arr[right], arr[left]

        if arr[left] <= arr[pivot]:
            left += 1

        if arr[right] >= arr[pivot]:
            right -= 1

    arr[pivot], arr[right] = arr[right], arr[pivot]

    qshelper(arr, start, right-1)
    qshelper(arr, left, end)

arr = [3,1,8,6,4,2,9]
print("before", arr)
quickSort(arr)
print("after", arr)


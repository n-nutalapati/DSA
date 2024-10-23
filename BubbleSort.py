def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


nums = [2,10,7,5,3,1]
print("before", nums)
bubbleSort(nums)
print("after", nums)


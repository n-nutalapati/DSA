def selectionSort(arr):
    
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

n = [6,1,8,3,4]
print("before", n)
selectionSort(n)
print("after", n)
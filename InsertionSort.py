def insertionSort(arr):
    for i in range(1, len(arr)):
        key=arr[i]
        j=i-1
        while(j>=0 and key < arr[j]):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
num = [7,3,6,4,8,1,0]
print("before:", num)
insertionSort(num)
print("after:", num) 
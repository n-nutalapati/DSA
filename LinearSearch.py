def linearSearch(arr, target):
    for i in range(len(arr)):
        if(arr[i] == target):
            return i
    
    return -1


num = linearSearch([1,6,8,13,72], 72)
print(num)
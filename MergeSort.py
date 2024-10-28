def mergeSort(arr):
    if len(arr) == 1:
        return arr
    
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    left_result = mergeSort(left)
    right_result = mergeSort(right)

    return merge(left_result, right_result)

def merge(left_arr, right_arr):
    
    result = [None] * (len(left_arr) + len(right_arr))

    i = j = k =  0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            result[k] = left_arr[i]
            i += 1
        else:
            result[k] = right_arr[j]
            j += 1
        
        k += 1
    
    while i < len(left_arr):
        result[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        result[k] = right_arr[j]
        j += 1
        k += 1
    
    return result


arr = [3,1,8,6,4,2,9]

print(mergeSort(arr))

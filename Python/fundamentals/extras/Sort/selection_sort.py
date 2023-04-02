arr = [0, 14, 11, 9, 6, 5, 3, 1, 8, 7, 2, 4]*10
def selection_sort(arr) :
    for i in range (len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min] :
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr
print(selection_sort(arr))
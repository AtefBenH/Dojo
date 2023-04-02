arr = [0, 14, 11, 9, 6, 5, 3, 1, 8, 7, 2, 4]
def insertion_sort(arr):
    for i in range(1, len(arr)):
        element = arr[i]
        j = i - 1
        while j >= 0 and element < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = element
    return arr

print (insertion_sort(arr))

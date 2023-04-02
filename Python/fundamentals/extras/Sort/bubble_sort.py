arr = [0, 14, 11, 9, 6, 5, 3, 1, 8, 7, 2, 4]*10
def bubble_sort(arr) :
    for i in range (len(arr)-1) :
        for j in range (len(arr)-1-i) :
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print (bubble_sort(arr))
            

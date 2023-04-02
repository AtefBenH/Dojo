import unittest
class InsertionSort(unittest.TestCase) :
    def testOne(self): 
        self.assertEqual(insertion_sort([3,1,2,5,4]), [1,2,3,4,5])
    def testTwo(self):
        self.assertEqual(insertion_sort([7,3,4,1,8,9]), [1,3,4,7,8,9])

def insertion_sort(arr):
    for i in range(1, len(arr)):
        element = arr[i]
        j = i - 1
        while j >= 0 and element < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = element
    return arr

if __name__ == "__main__" :
    unittest.main()

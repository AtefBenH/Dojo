import unittest

def bubble_sort(arr) :
    for i in range (len(arr)-1) :
        for j in range (len(arr)-1-i) :
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

class BubbleSortTests (unittest.TestCase):
    def testOne(self):
        self.assertEqual(bubble_sort([7,3,4,1,8,9]), [1,3,4,7,8,9])

    def testTwo(self):
        self.assertEqual(bubble_sort([3,1,2,5,4]), [1,2,3,4,5])

    def setUp(self):
        # Runs before the tests
        print("Running setUp tasks")
    
    def tearDown(self):
        # Runs after the tests
        print("Running tearDown tasks")

if __name__== '__main__' :
    unittest.main() # this runs our tests
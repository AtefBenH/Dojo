class Underscore:
    def map(self, iterable, callback):
        for i in range (len(iterable)) :
            iterable[i] = callback(iterable[i])
        return iterable
        
    def find(self, iterable, callback):
        for item in iterable :
            if callback(item) :
                return item
    
    def filter(self, iterable, callback):
        truth = []
        for item in iterable :
            if callback(item) :
                truth.append(item)
        return truth
    
    def reject(self, iterable, callback):
        reject = []
        for item in iterable :
            if not callback(item) :
                reject.append(item)
        return reject
    

# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
print(_.map([1,2,3], lambda x: x*2)) # should return [2,4,6]
print(_.find([1,2,3,4,5,6], lambda x: x>4)) # should return the first value that is greater than 4
print(_.filter([1,2,3,4,5,6], lambda x: x%2==0)) # should return [2,4,6]
print(_.reject([1,2,3,4,5,6], lambda x: x%2==0)) # should return [1,3,5]



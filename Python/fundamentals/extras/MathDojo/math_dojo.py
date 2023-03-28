class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for num in nums :
            self.result+= num
        return self
    
    def subtract(self, num, *nums):
        self.result -= num
        for num in nums :
            self.result-= num
            return self
    
# create instances :
md = MathDojo()
md1 = MathDojo()
md2 = MathDojo()

# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!
x= md1.add(4,3,10).add(3,5,7,4).add(4).result
print(x)    # should print 40
x= md2.subtract(5,5).subtract(3,1).subtract(2,4).result
print(x)    # should print -20

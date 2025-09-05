class Difference:
    def __init__(self, a):
        self.__elements = a
        
	# Add your code here
    def computeDifference(self):
        maxi = a[0]
        mini = a[0]
        
        for num in a:
            if num > maxi:
                maxi = num
                
            if num < mini:
                mini = num
                
        self.maximumDifference = maxi - mini

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

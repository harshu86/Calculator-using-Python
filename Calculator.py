class calc:
    
    def add(self,a,b):
        ans = a + b
        return ans
    
    def sub(self,a,b):
        ans = a-b
        return ans
    
    def multi(self,a,b):
        ans = a*b
        return ans
    
    def div(self,a,b):
        ans = a / b
        return ans
    
    def per(self,a,b):
        ans = (a * b) / 100
        return ans
    
    def avg(self,a,b):
        ans = (a+b)/2
        return ans
    
    def maxmin(self,a,b):
        if(a>b):
            return a
        else:
            return b
    
    
d = calc()
print("addition of two numbers: ",d.add(5,6))
print("**********************************************************")
print("subtraction of two numbers: ",d.sub(6,5))
print("**********************************************************")
print("multiplication of two number: ",d.multi(5,6))
print("**********************************************************")
print("Division of two numbers: ",d.div(10,2))
print("**********************************************************")
print("Percentage of numbers: ",d.per(100,2))
print("**********************************************************")
print("Average differance between two numbers: ",d.avg(10,5))
print("**********************************************************")
print("Maximum or Minimum number is: ",d.maxmin(6,5))




    
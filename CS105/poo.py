class Rectangle:
	def __init__(self,x,y):
		self.length=x
		self.width=y
	def __str__(self):
		return 'Length='+str(self.length)+' Width='+str(self.width)
	def area(self):
		return self.width*self.length
	def perimeter(self):
		return 2*self.width+2*self.length
	def rescale(self,a):
		self.width=a*self.width
		self.length=a*self.length
	def __del__(self):
		print("This object no longer exists")
examp1=Rectangle(3,5)
print(type(examp1))
print(examp1)
print(examp1.area())
print(examp1.perimeter())
examp1.rescale(2)
print(examp1)
examp2=Rectangle(2,4)
print(examp2)
print(examp2.area())
print(examp2.perimeter())
 
examp1=42
del examp2
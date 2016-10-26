Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> class Animate :
	pass

>>> class Animate :
	def breathe :
		
SyntaxError: invalid syntax
>>> class Animate :
	def breathe() :
		print ('breathing')
	def move() :
		print ('moving')

		
>>> class Mammals(Animate) :
	def feed_young_with_milk() :
		print ('feeding youngs')

		
>>> class Giraffes (Mammals) :
	def eat_leaves() :
		print ('eating leaves from trees')

		
>>> reginald=Giraffes()
>>> reginald.move()

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    reginald.move()
TypeError: move() takes no arguments (1 given)
>>> class Animate :
	def breathe(self) :
		print ('breathing')
	def move(self) :
		print ('moving')

		
>>> class Mammals(Animate) :
	def feed_young_with_milk(self) :
		print ('feeding youngs')

		
>>> class Giraffes (Mammals) :
	def eat_leaves(self) :
		print ('eating leaves from trees')

		
>>> reginald=Giraffes()
>>> reginald.move()
moving
>>> class Giraffes (Mammals) :
	def find_food(self) :
		self.move()
		print ("I've found food")
		self.eat_leaves()

		
>>> class Giraffes (Mammals) :
	def dance_a_jig(self) :
		self.move()
		self.move()
		self.move()
		self.move()

		
>>> reginald=Giraffes()
>>> reginald.dance_a_jig
<bound method Giraffes.dance_a_jig of <__main__.Giraffes instance at 0x7ff31f2065f0>>
>>> reginald.dance_a_jig()
moving
moving
moving
moving
>>> 
class Giraffes (Mammals) :
	def dance_a_jig(self) :
		self.move()
		self.move()
		self.move()
		self.move()
	def find_food(self) :
		self.move()
		print ("I've found food")
		self.eat_leaves()

		
>>> reginald=Giraffes()
>>> reginald.find_food()
moving
I've found food

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    reginald.find_food()
  File "<pyshell#46>", line 11, in find_food
    self.eat_leaves()
AttributeError: Giraffes instance has no attribute 'eat_leaves'
>>> class Giraffes (Mammals) :
	def dance_a_jig(self) :
		self.move()
		self.move()
		self.move()
		self.move()
	def eat_leaves(self) :
		print ('eating leaves from trees')
	def find_food(self) :
		self.move()
		print ("I've found food")
		self.eat_leaves()

		
>>> reginald.find_food()
moving
I've found food

Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    reginald.find_food()
  File "<pyshell#46>", line 11, in find_food
    self.eat_leaves()
AttributeError: Giraffes instance has no attribute 'eat_leaves'
>>> reginald=Giraffes()
>>> reginald.find_food()
moving
I've found food
eating leaves from trees
>>> # use the __init__ function
>>> # special type of function in Py classes and must have this name
>>> # Py will automatically call this function when we create a new object
>>> class Giraffes (Mammals) :
	def __init__(self, spots) :
		self.giraffe_spots = spots
	def dance_a_jig(self) :
		self.move()
		self.move()
		self.move()
		self.move()
	def eat_leaves(self) :
		print ('eating leaves from trees')
	def find_food(self) :
		self.move()
		print ("I've found food")
		self.eat_leaves()

		
>>> # just as one function in a class can call another function using the self parameter, variables in the class are also accessed using self.
>>> ozwald=Giraffes(100)
>>> gertrude=Giraffes(150)
>>> print(ozwald.giraffe_spots)
100
>>> print(gertrude.giraffe_spots)
150
>>> # refer to the variables and functions of an object using the dot.
>>> print(gertrude.breathe())
breathing
None
>>> # but when creating a variable of function inside a class you use the self parameter.
>>> class Giraffes (Mammals) :
	def __init__(self, spots) :
		self.giraffe_spots = spots
	def dance_a_jig(self) :
		self.move()
		self.move()
		self.move()
		self.move()
	def eat_leaves(self) :
		print ('eating leaves from trees')
	def find_food(self) :
		self.move()
		print ("I've found food")
		self.eat_leaves()
	def left_foot_forward (self) :
		print('left foot forward')
	def left_foot_backward (self) :
		print ('left foot backward')
	def right_foot_forward (self) :
		print ('rigt foot forward')
	def right_foot_backward(self) :
		print('right foot backward')
	def dance(self) :
		self.right_foot_forward()
		self.right_foot_backward()
		self.left_foot_forward()
		self.left_foot_backward()
		self.right_foot_forward()
		self.right_foot_backward()

		
>>> reginald=Giraffes()

Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    reginald=Giraffes()
TypeError: __init__() takes exactly 2 arguments (1 given)
>>> reginald=Giraffes(120)
>>> reginald.dance()
rigt foot forward
right foot backward
left foot forward
left foot backward
rigt foot forward
right foot backward
>>> 

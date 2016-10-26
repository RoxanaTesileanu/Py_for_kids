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
>>> 

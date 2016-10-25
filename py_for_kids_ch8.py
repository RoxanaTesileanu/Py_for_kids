Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> # an object can be thought of as a member of a class
>>> class Things:
	pass

>>> # if a class is a part of another class => child of that class, and parent class
>>> # Inanimate and Animate are both children of the class Things:
>>> class Inanimate(Things) :
	pass

>>> class Animate(Things) :
	pass

>>> class Sidewalks(Inanimate) :
	pass

>>> class Animals (Animate) :
	pass

>>> class Mammals (Animals) :
	pass

>>> class Giraffes(Mammals) :
	pass

>>> # Adding objects to classes
>>> reginald=Giraffes()
>>> # when we create our classes, we also need to define functions that can be used with the objects in that class
>>> 
>>> def this_is_a_normal_function() :
	print('I am a normal function')

	
>>> class ThisIsMySillyClass :
	def this_is_a_normal_function() :
		print ('I am a normal class function')
	def this_is_also_a_normal_function() :
		print ('I am also a normal class function')

		
>>> 
>>> # a characteristic is a trait that all members of the class (incl. children) share.
>>> class Animals(Animate) :
	def breathe (self) :
		pass
	def move (self) :
		pass
	def eat_food(self) :
		pass

	
>>> class Mammals(Animals) :
	def feed_young_with_milk(self) :
		pass

	
>>> class Giraffes(Mammals) :
	def eat_leaves_from_trees(self) :
		pass

	
>>> reginald=Giraffes()
>>> reginald.move()
>>> reginald.eat_leaves_from_trees()
>>> harold=Giraffes()
>>> class Animals(Animate) :
	def breathe(self) :
		print ('breathing')
	def move(self) :
		print ('moving')
	def eat_food(self) :
		print ('eating food')

		
>>> class Mammals(Animals) :
	def feed_young_with_milk(self) :
		print ('feeding young')

		
>>> class Giraffes(Mammals) :
	def eat_leaves_from_trees(self) :
		print('eating leaves')

		
>>> reginald.move()
>>> reginald = Giraffes()
>>> harold = Giraffes()
>>> reginald.move()
moving
>>> harold.move()
moving
>>> harold.eat_leaves_from_trees()
eating leaves
>>> 

Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t=turtle.Pen()
>>> t.forwoard(50)

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t.forwoard(50)
AttributeError: 'Turtle' object has no attribute 'forwoard'
>>> t.forward(50)
>>> t.left(90)
>>> t.forward(50)
>>> t.left(90)
>>> t.forward(50)
>>> t.left (90)
>>> t.forward(50)
>>> t.up()
>>> t.forward (30)
>>> t.left(90)
>>> t.down()
>>> t.left(45)
>>> t.right(45)
>>> t.right(45)
>>> t.forward(30)
>>> t.right(90)
>>> t.forward(30)
>>> t.right(45)
>>> t.right(90)
>>> ipot=2*30^2
>>> ipot
62
>>> sqrt(ipot)

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    sqrt(ipot)
NameError: name 'sqrt' is not defined
>>> import numpy as np
>>> np.sqrt(ipot)
7.8740078740118111
>>> t.forward(np.sqrt(ipot))
>>> t.forward(7.8740078740118111)
>>> ipot=2*(30^2)
>>> ipot
56
>>> ipot=2*(30**2)
>>> ipot
1800
>>> 3^2
1
>>> np.sqrt(ipot)
42.426406871192853
>>> t.forward(42.426406871192853 -7.8740078740118111)
>>> t.up()
>>> t.forward(80)
>>> t.forward(80)
>>> t.down()
>>> t.forward(30)
>>> t.up()
>>> t.forward(10)
>>> t.right(90)
>>> t.forward(30)
>>> t.backward(30)
>>> t.down()
>>> t.forward(30)
>>> t.up()
>>> t.forward(10)
>>> t.down()
>>> t.right(90)
>>> t.forward(10)
>>> t.left(90)
>>> t.up()
>>> t.forward(100)
>>> t.forward(10)
>>> t.down()
>>> t.forward(30)
>>> t.up()
>>> t.forward(10)
>>> t.right(90)
>>> t.forward(10)
>>> t.down()
>>> t.forward(30)
>>> t.up()
>>> t.forward(10)
>>> t.right(90)
>>> t.forward(10)
>>> t.down()
>>> t.forward(30)
>>> t.up()
>>> t.forward(10)
>>> t.right(90)
>>> t.forward(10)
>>> t.down()
>>> t.forward(30)
>>> t.up()
>>> t.forward(100)
>>> 

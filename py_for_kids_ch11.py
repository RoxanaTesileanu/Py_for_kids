Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t=turtle.Pen()
>>> t.forward(50)
>>> t.left(90)

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t.left(90)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 1614, in left
    self._rotate(angle)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 3108, in _rotate
    self._update()
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 2564, in _update
    self._update_data()
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 2550, in _update_data
    self.screen._incrementudc()
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 1239, in _incrementudc
    raise Terminator
Terminator
>>> t=turtle.Pen()
>>> t.window_height()
810
>>> t.window_width()
1855
>>> t.window_width(800)

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    t.window_width(800)
TypeError: window_width() takes exactly 1 argument (2 given)
>>> t.window_width()
1855
>>> t.screen()

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    t.screen()
TypeError: '_Screen' object is not callable
>>> t.forward(50)
>>> t.left(90)
>>> t.forward(50)
>>> t.left(90)
>>> t.forward(50)
>>> t.left(90)
>>> t.forward(50)
>>> t.reset()
>>> for x in range (1,5) :
	t.forward(50)
	t.left(90)

	
>>> t.reset()
>>> for x in range(1,9) :
	t.forward(100)
	t.left(225)

	
>>> t.reset()
>>> for x in range(1,9) :
	t.forward(100)
	t.left(225)

	
>>> t.reset()
>>> for x in range (1,38) :
	t.forward(100)
	t.left(175)

	
>>> t.reset()
>>> for x in range(1,20) :
	t.forward(100)
	t.left(95)

	
>>> t.reset()
>>> for x in range(1,19) :
	t.forward(100)
	if x%2 == 0 :
		t.left(175)
	else :
		t.left(225)

		
>>> t.reset
<bound method Turtle.reset of <turtle.Turtle object at 0x7f10a1557c10>>
>>> t.reset()
>>> t.color(1,0,0)
>>> t.begin_fill()
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(120)
>>> t.left(90)
>>> t.forward(20)
>>> t.right(90)
>>> t.forward(20)
>>> t.left(90)
>>> t.forward(60)
>>> t.right(90)
>>> t.forward(90)
>>> t.left(90)
>>> t.forward(20)
>>> t.end_fill()
>>> t.color(0,0,0)
>>> t.up()
>>> t.forward(10)
>>> t.down()
>>> t.begin_fill()
>>> t.circle(10)
>>> t.end_fill()
>>> t.setheading(0)
>>> t.up()
>>> t.forward(90)
>>> t.right(90)
>>> t.forward(70)
>>> t.right(90)
>>> t.setheading(0)
>>> t.forward(20)
>>> t.right(90)
>>> t.forward(40)
>>> t.forward(10)
>>> t.setheading(0)
>>> t.begin_fill()
>>> t.down()
>>> t.circle(20)
>>> t.end_fill()
>>> t.reset()
>>> t.color(1,1,0)
>>> t.begin_fill()
>>> t.circle(50)
>>> t.end_fill()
>>> def mycircle(red, green, blue) :
	t.color(red, green, blue)
	t.begin_fill()
	t.circle(50)
	t.end_fill()

	
>>> t.forward(100)
>>> mycircle(0,1,0)
>>> t.forward(100)
>>> mycircle(1,0,0)
>>> t.up()
>>> t.forward(100)
>>> t.down()
>>> mycircle(0.5, 0,0)
>>> t.up()
>>> t.right(90)
>>> t.forward(150)
>>> t.down()
>>> mycircle(0,0,1)
>>> t.up()
>>> t.left(90)
>>> t.left(180)
>>> t.forward(40)
>>> t.forward(100)
>>> mycircle(0,0,0.5)
>>> t.up()
>>> t.forward(100)
>>> t.forward(20)
>>> t.down()
>>> mycircle(0.9, 0.75, 0)
>>> t.up()
>>> t.forward(100)
>>> t.down()
>>> mycircle(1,0.7,0.75)
>>> t.up()
>>> 
>>> t.heading(0)

Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    t.heading(0)
TypeError: heading() takes exactly 1 argument (2 given)
>>> t.heading(0)

Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    t.heading(0)
TypeError: heading() takes exactly 1 argument (2 given)
>>> t.setheading(0)
>>> t.right(90)
>>> t.forward(12)
>>> t.down()
>>> mycircle(1,0.5,0)
>>> t.up
<bound method Turtle.penup of <turtle.Turtle object at 0x7f10a1557c10>>
>>> t.up()
>>> t.forward(100)
>>> t.down()
>>> mycircle(0.9, 0.5, 0.15)
>>> mycircle(1,1,1)
>>> mycircle(0,0,0)
>>> t.reset()
>>> def mysquare(size) :
	for x in range (1,5) :
		t.forward(size)
		t.left(90)

		
>>> mysquare(50)
>>> t.reset
<bound method Turtle.reset of <turtle.Turtle object at 0x7f10a1557c10>>
>>> t.reset()
>>> mysquare(25)
>>> mysquare(50)
>>> mysquare(75)
>>> mysquare(100)
>>> mysquare(125)
>>> t.reset()
>>> t.begin_fill()
>>> mysquare(50)
>>> t.end_fill()
>>> t.reset()
>>> def mysquare(size, filled) :
	if filled==True :
		t.begin_fill()
	for x in range(1,5) :
		t.forward(size)
		t.left(90)
	if filled==True :
		t.end_fill()

		
>>> mysquare(50, True)
>>> mysquare(50, False)
>>> mysquare(150, False)
>>> t.reset()
>>> for x in range (1,19) :
	t.forward(100)
	if x%2 == 0 :
		t.left(175)
	else :
		t.left(225)

		
>>> def mystar(size, filled) :
	if filled == True :
		t.begin_fill()
	for x in range (1,19) :
		t.forward(size)
		if x%2 == 0 :
			t.left(175)
		else :
			t.left(225)
	if filled == True :
		t.end_fill()

		
>>> t.reset()
>>> mystar(100)

Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    mystar(100)
TypeError: mystar() takes exactly 2 arguments (1 given)
>>> mystar(150, True)
>>> t.reset()
>>> t.color(0.9, 0.75, 0)
>>> mystar(120, True)
>>> t.color(0, 0, 0)
>>> mystar(120, False)
>>> 

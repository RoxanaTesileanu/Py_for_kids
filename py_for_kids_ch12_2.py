Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from Tkinter import *
>>> tk = Tk()
>>> btn=Button(tk, text='click me')
>>> btn.pack()
>>> btn.mainloop()
>>> btn.pack()

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    btn.pack()
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 1944, in pack_configure
    + self._options(cnf, kw))
TclError: can't invoke "pack" command: application has been destroyed
>>> tk = Tk()
>>> btn=Button(tk, text='click me')
>>> btn.pack()
>>> tk = Tk()
>>> 
=============================== RESTART: Shell ===============================
>>> def hello() :
	print ('hello there')

	
>>> 
>>> from Tkinter import *
>>> tk=Tk()
>>> btn=Button(tk, text='click me', command=hello)
>>> btn.pack()
>>> btn.mainloop()
hello there
hello there
hello there
hello there
hello there
hello there
>>> def person (width, height) :
	print ('I am %s feet wide , %s feet high' % (width, height))

	
>>> person(3,4)
I am 3 feet wide , 4 feet high
>>> person(height=4, width=3)
I am 3 feet wide , 4 feet high
>>> tk=Tk()
>>> canvas=Canvas(tk, width=500, height=500)
>>> canvas.pack()
>>> canvas.mainloop()
>>> tk=Tk()
>>> canvas=Canvas(tk, width=500, height=500)
>>> canvas.pack(side='top')
>>> print canvas
.139801073647696
>>> 
=============================== RESTART: Shell ===============================
>>> import Tkinter as tk
>>> root = tk.Tk()
>>> btn = tk.Button(root, text ='click me')
>>> btn.pack()
>>> root.mainloop()
>>> canvas.create_line(0,0,500, 500)

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    canvas.create_line(0,0,500, 500)
NameError: name 'canvas' is not defined
>>> canvas=tk.Canvas(root, width=500, height=500)

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    canvas=tk.Canvas(root, width=500, height=500)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2234, in __init__
    Widget.__init__(self, master, 'canvas', cnf, kw)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2094, in __init__
    (widgetName, self._w) + extra + self._options(cnf))
TclError: can't invoke "canvas" command: application has been destroyed
>>> root = tk.Tk()
>>> canvas=tk.Canvas(root, width=500, height=500)
>>> canvas.create_line(0,0, 500, 500)
1
>>> canvas.pack()
>>> root.mainloop()
>>> 
=============================== RESTART: Shell ===============================
>>> from Tkinter import tk

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    from Tkinter import tk
ImportError: cannot import name tk
>>> import Tkinter as tk
>>> window=tk.Tk()
>>> canvas=tk.Canvas(window, width=400, height=400)
>>> canvas.pack()
>>> canvas.create_rectangle(10, 10, 50, 50)
1
>>> window.mainloop()
>>> window=tk.Tk()
>>> canvas=tk.Canvas(window, width=400, height=400)
>>> canvas.pack()
>>> canvas.create_rectangle(10, 10, 50,20)
1
>>> window.mainloop()
>>> window=tk.Tk()
>>> canvas=tk.Canvas(window, 400, 400)

Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    canvas=tk.Canvas(window, 400, 400)
TypeError: __init__() takes at most 3 arguments (4 given)
>>> canvas=tk.Canvas(window, width=400, height=400)
>>> canvas.pack()
>>> canvas.create_rectangle(10, 10, 40, 300)
1
>>> window.mainloop()
>>> 
>>> window=tk.Tk()
>>> canvas=tk.Canvas(window, width=400, height=400)
>>> canvas.pack()
>>> def random_rectangle(width, height) :
	x1=random.randrange(width)
	y1=random.randrange(height)
	x2=x1 + random.randrange(width)
	y2=y1 + random.randrange(height)
	canvas.create_rectangle(x1,y1,x2,y2)
	window.mainloop()

	
>>> random_rectangle(400, 400)

Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    random_rectangle(400, 400)
  File "<pyshell#73>", line 2, in random_rectangle
    x1=random.randrange(width)
NameError: global name 'random' is not defined
>>> import random
>>> random_rectangle(400, 400)
>>> for x in range(0, 100) :
	random_rectangle(400, 400)

	

Traceback (most recent call last):
  File "<pyshell#79>", line 2, in <module>
    random_rectangle(400, 400)
  File "<pyshell#73>", line 6, in random_rectangle
    canvas.create_rectangle(x1,y1,x2,y2)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2330, in create_rectangle
    return self._create('rectangle', args, kw)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2309, in _create
    *(args + self._options(cnf, kw))))
TclError: invalid command name ".140489114914896"
>>> def random_rectangle(width, height) :
	x1=random.randrange(width)
	y1=random.randrange(height)
	x2=x1 + random.randrange(width)
	y2=y1 + random.randrange(height)
	canvas.create_rectangle(x1,y1,x2,y2)

>>> 
>>> for x in range(0, 100) :
	random_rectangle(400, 400)

	

Traceback (most recent call last):
  File "<pyshell#84>", line 2, in <module>
    random_rectangle(400, 400)
  File "<pyshell#81>", line 6, in random_rectangle
    canvas.create_rectangle(x1,y1,x2,y2)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2330, in create_rectangle
    return self._create('rectangle', args, kw)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2309, in _create
    *(args + self._options(cnf, kw))))
TclError: invalid command name ".140489114914896"
>>> window=tk.Tk()
>>> canvas=tk.Canvas(window, width=400, height=400)
>>> canvas.pack()
>>> def random_rectangle(width, height) :
	x1=random.randrange(width)
	y1=random.randrange(height)
	x2=x1 + random.randrange(width)
	y2=y1 + random.randrange(height)
	canvas.create_rectangle(x1,y1,x2,y2)

	
>>> for x in range(0, 100) :
	random_rectangle(400, 400)
	window.mainloop()

	

Traceback (most recent call last):
  File "<pyshell#92>", line 2, in <module>
    random_rectangle(400, 400)
  File "<pyshell#89>", line 6, in random_rectangle
    canvas.create_rectangle(x1,y1,x2,y2)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2330, in create_rectangle
    return self._create('rectangle', args, kw)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2309, in _create
    *(args + self._options(cnf, kw))))
TclError: invalid command name ".140489114949680"
>>> window=tk.Tk()
>>> canvas=tk.Canvas(window, width=400, height=400)
>>> canvas.pack()
>>> for x in range(0, 100) :
	random_rectangle(400, 400)

	
>>> 
>>> window.mainloop()
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> window=tk.Tk()

Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    window=tk.Tk()
NameError: name 'tk' is not defined
>>> import Tkinter as tk
>>> import random
>>> window=tk.Tk()
>>> canvas=tk.Canvas(window, width=400, height=400)
>>> canvas.pack()
>>> canvas.create_rectangle(10, 10, 50, 50, 'red')

Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    canvas.create_rectangle(10, 10, 50, 50, 'red')
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2330, in create_rectangle
    return self._create('rectangle', args, kw)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2309, in _create
    *(args + self._options(cnf, kw))))
TclError: wrong # coordinates: expected 0 or 4, got 5
>>> def random_rectangle(width, height, fill_color) :
	x1=random.randrange(width)
	y1=random.randrange(height)
	x2=x1 + random.randrange(width)
	y2=y1 + random.randrange(height)
	canvas.create_rectangle(x1,y1,x2,y2, fill=fill_color)

	
>>> random_rectangle(400, 400, 'green')
>>> window.mainloop()
>>> window=tk.Tk()
>>> canvas=tk.Canvas(window, width=400, height=400)
>>> canvas.pack()
>>> random_rectangle(400, 400, 'red')
>>> 
>>> window.mainloop()
>>> window=tk.Tk()
>>> canvas=tk.Canvas(window, width=400, height=400)
>>> random_rectangle(400, 400, 'green')
>>> random_rectangle(400, 400, 'red')
>>> random_rectangle(400, 400, 'pink')
>>> random_rectangle(400, 400, 'pink')
>>> random_rectangle(400, 400, 'cyan')
>>> random_rectangle(400, 400, 'blue')
>>> window.mainloop()
>>> 
>>> window=tk.Tk()
>>> canvas=tk.Canvas(window, width=400, height=400)
>>> random_rectangle(400, 400, 'green')
>>> window.mainloop()
>>> window=tk.Tk()
>>> canvas=tk.Canvas(window, width=400, height=400)
>>> canvas.pack()
>>> random_rectangle(400, 400, 'red')
>>> random_rectangle(400, 400, 'green')
>>> random_rectangle(400, 400, 'pink')
>>> random_rectangle(400, 400, 'cyan')
>>> random_rectangle(400, 400, 'blue')
>>> window.mainloop()
>>> 

Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import Tkinter as tk
>>> import random
>>> def random_rectangle(width, height) :
	x1=random.randrange(width)
	y1=random.randrange(height)
	x2=x1+random.randrange(width)
	y2=y1 + random.randrange(height)
	canvas.create_rectangle(x1,y1,x2,y2)

	
>>> window=tk.Tk()
>>> canvas=tk.Canvas(width=600, height=600)
>>> canvas.pack()
>>> random_rectangle(400, 400)
>>> window.mainloop()
>>> 
>>> def random_rectangle(width, heigt, fill_color) :
	x1=random.randrange(width)
	y1=random.randrange(height)
	x2=x1+random.randrange(width)
	y2=y1 + random.randrange(height)
	canvas.create_rectangle(x1,y1,x2,y2, fill=fill_color)

	
>>> window=tk.Tk()
>>> canvas=tk.Canvas(width=600, height=600)
>>> canvas.pack()
>>> random_rectangle(400, 400, 'red')

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    random_rectangle(400, 400, 'red')
  File "<pyshell#17>", line 3, in random_rectangle
    y1=random.randrange(height)
NameError: global name 'height' is not defined
>>> def random_rectangle(width, height, fill_color) :
	x1=random.randrange(width)
	y1=random.randrange(height)
	x2=x1+random.randrange(width)
	y2=y1 + random.randrange(height)
	canvas.create_rectangle(x1,y1,x2,y2, fill=fill_color)

	
>>> random_rectangle(400, 400, 'red')
>>> window.mainloop()
>>> random_rectangle(400, 400, '#ffd800')

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    random_rectangle(400, 400, '#ffd800')
  File "<pyshell#23>", line 6, in random_rectangle
    canvas.create_rectangle(x1,y1,x2,y2, fill=fill_color)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2330, in create_rectangle
    return self._create('rectangle', args, kw)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2309, in _create
    *(args + self._options(cnf, kw))))
TclError: invalid command name ".139743485844368"
>>> print ('%s' % 15)
15
>>> print('%x' % 15)
f
>>> print('%20x' % 15)
                   f
>>> print('%02x' % 15)
0f
>>> tk.colorchooser.askcolor()

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    tk.colorchooser.askcolor()
AttributeError: 'module' object has no attribute 'colorchooser'
>>> colorchooser.askcolor()

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    colorchooser.askcolor()
NameError: name 'colorchooser' is not defined
>>> import Tkinter.colorchooser

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    import Tkinter.colorchooser
ImportError: No module named colorchooser
>>> import tkinter.colorchooser

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    import tkinter.colorchooser
ImportError: No module named tkinter.colorchooser
>>> import Tkinter.colorchooser

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    import Tkinter.colorchooser
ImportError: No module named colorchooser
>>> import tkinter.colorchooser

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    import tkinter.colorchooser
ImportError: No module named tkinter.colorchooser
>>> import ttk
>>> import tkColorChooser
>>> tkColorChooser.askcolor()
(None, None)
>>> canvas=tk.Canvas(width=600, height=600)
>>> canvas.pack()
>>> random_rectangle(400, 400, 'red')
>>> mainloop()

Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    mainloop()
NameError: name 'mainloop' is not defined
>>> ttk.Button('click here')

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    ttk.Button('click here')
  File "/usr/lib/python2.7/lib-tk/ttk.py", line 610, in __init__
    Widget.__init__(self, master, "ttk::button", kw)
  File "/usr/lib/python2.7/lib-tk/ttk.py", line 555, in __init__
    Tkinter.Widget.__init__(self, master, widgetname, kw=kw)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2085, in __init__
    BaseWidget._setup(self, master, cnf)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2063, in _setup
    self.tk = master.tk
AttributeError: 'str' object has no attribute 'tk'
>>> window=ttk()

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    window=ttk()
TypeError: 'module' object is not callable
>>> tkColorChooser.askcolor()

Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    tkColorChooser.askcolor()
  File "/usr/lib/python2.7/lib-tk/tkColorChooser.py", line 65, in askcolor
    return Chooser(**options).show()
  File "/usr/lib/python2.7/lib-tk/tkCommonDialog.py", line 48, in show
    s = w.tk.call(self.command, *w._options(self.options))
TclError: can't invoke "grab" command: application has been destroyed
>>> 
=============================== RESTART: Shell ===============================
>>> import Tkinter as tk
>>> import ttk
>>> import tkColorChooser
>>> window=tk.Tk()
>>> ttk.Button (window, 'click here')

Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    ttk.Button (window, 'click here')
TypeError: __init__() takes at most 2 arguments (3 given)
>>> btn=ttk.Button (window, 'click here')

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    btn=ttk.Button (window, 'click here')
TypeError: __init__() takes at most 2 arguments (3 given)
>>> btn=tk.Button (window, 'click here')

Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    btn=tk.Button (window, 'click here')
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2164, in __init__
    Widget.__init__(self, master, 'button', cnf, kw)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2089, in __init__
    for k in cnf.keys():
AttributeError: 'str' object has no attribute 'keys'
>>> btn=ttk.Button (window, text='click here')
>>> btn.pack()
>>> window.mainloop()
>>> 
=============================== RESTART: Shell ===============================
>>> import Tkinter as tk
>>> import ttk
>>> import tkColorChooser
>>> window=tk.Tk()
>>> tKColorChooser.askcolor()

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    tKColorChooser.askcolor()
NameError: name 'tKColorChooser' is not defined
>>> tkColorChooser.askcolor()
((116, 174, 220), '#74aedc')
>>> mycolor=((116, 174, 220), '#74aedc')
>>> mycolor[1]
'#74aedc'
>>> import pickle
>>> save_file=open('mycolor.dat', 'wb')
>>> pickle.dump(mycolor, save_file)
>>> save_file.close()
>>> load_file=open('mycolor.dat', 'rb')
>>> pickle.load(load_file)
((116, 174, 220), '#74aedc')
>>> myloaded_color= pickle.load(load_file)

Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    myloaded_color= pickle.load(load_file)
  File "/usr/lib/python2.7/pickle.py", line 1384, in load
    return Unpickler(file).load()
  File "/usr/lib/python2.7/pickle.py", line 864, in load
    dispatch[key](self)
  File "/usr/lib/python2.7/pickle.py", line 886, in load_eof
    raise EOFError
EOFError
>>> load_file.close()
>>> load_file=open('mycolor.dat', 'rb')
>>> myloaded_color= pickle.load(load_file)
>>> load_file.close()
>>> print (myloaded_color)
((116, 174, 220), '#74aedc')
>>> c=tkColorChooser.askcolor()
>>> print (c[1])
#80b6db
>>> canvas=tk.Canvas(width=600, height=600)
>>> canvas.pack()
>>> def random_rectangle(width, height, fill_color) :
	x1=random.randrange(width)
	y1=random.randrange(height)
	x2=x1+random.randrange(width)
	y2=y1 + random.randrange(height)
	canvas.create_rectangle(x1,y1,x2,y2, fill=fill_color)

	
>>> random_rectangle(400, 400, c[1])

Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    random_rectangle(400, 400, c[1])
  File "<pyshell#82>", line 2, in random_rectangle
    x1=random.randrange(width)
NameError: global name 'random' is not defined
>>> import random
>>> random_rectangle(400, 400, c[1])
>>> window.mainloop()
>>> 
>>> window = tk.Tk()
>>> canvas=tk.Canvas(window, width=600, height=600)
>>> canvas.pack()
>>> random_rectangle(400, 400, myloaded_color[1])
>>> window.mainloop()
>>> 
>>> window=tk.Tk()
>>> master=tk.Tk()
>>> canvas=tk.Canvas(width=600, height=600)
>>> canvas.pack()
>>> random_rectangle(400, 400, myloaded_color[1])
>>> window.mainloop()
>>> master=tk.Tk()
>>> canvas=tk.Canvas(width=600, height=600)
>>> canvas.pack()
>>> random_rectangle(400, 400, myloaded_color[1])
>>> window.mainloop()
>>> 
>>> master=tk.Tk()
>>> canvas=tk.Canvas(600, 600)

Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    canvas=tk.Canvas(600, 600)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2234, in __init__
    Widget.__init__(self, master, 'canvas', cnf, kw)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2085, in __init__
    BaseWidget._setup(self, master, cnf)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2063, in _setup
    self.tk = master.tk
AttributeError: 'int' object has no attribute 'tk'
>>> canvas=tk.Canvas(width=600, height=600)
>>> canvas.create_arc(10, 10, 200, 100, extent=180, style=ARC)

Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    canvas.create_arc(10, 10, 200, 100, extent=180, style=ARC)
NameError: name 'ARC' is not defined
>>> canvas.create_arc(10, 10, 200, 100, extent=180)
1
>>> window.mainloop()
>>> master=tk.Tk()
>>> canvas=tk.Canvas(600, 600)

Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    canvas=tk.Canvas(600, 600)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2234, in __init__
    Widget.__init__(self, master, 'canvas', cnf, kw)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2085, in __init__
    BaseWidget._setup(self, master, cnf)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2063, in _setup
    self.tk = master.tk
AttributeError: 'int' object has no attribute 'tk'
>>> canvas=tk.Canvas(width=600, height=600)
>>> canvas.pack()
>>> canvas.create_arc(10, 10, 200, 100, extent=180)
1
>>> window.mainloop()
>>> 
>>> 
master=tk.Tk()
>>> canvas=tk.Canvas(width=600, height=600)
>>> canvas.pack()
>>> canvas.create_arc(10, 10, 200, 100)
1
>>> window.mainloop()
>>> 
>>> master=tk.Tk()
>>> width=600
>>> height=600
>>> canvas=tk.Canvas()
>>> canvas.pack()
>>> canvas.create_arc(10, 10, 200, 80, extent=45)
1
>>> master.mainloop()
>>> canvas.create_arc(10, 10, 200, 80, extent=45)

Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    canvas.create_arc(10, 10, 200, 80, extent=45)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2312, in create_arc
    return self._create('arc', args, kw)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2309, in _create
    *(args + self._options(cnf, kw))))
TclError: invalid command name ".140512897205960"
>>> canvas=tk.Canvas()
>>> canvas.create_arc(10, 10, 200, 80, extent=45)
1
>>> master.mainloop()
>>> 
>>> canvas=tk.Canvas()
>>> canvas.create_arc(10, 80, 200, 160, extent=90)
1
>>> master.mainloop()
>>> canvas.pack()

Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    canvas.pack()
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 1944, in pack_configure
    + self._options(cnf, kw))
TclError: can't invoke "pack" command: application has been destroyed
>>> canvas=tk.Canvas()
>>> canvas.pack()
>>> canvas.create_arc(10, 80, 200, 160, extent=90)
1
>>> master.mainloop()
>>> 
>>> canvas=tk.Canvas()
>>> canvas.pack()
>>> canvas.create_arc(10, 160, 200, 240, extent=135)
1
>>> master.mainloop()
>>> 
>>> canvas=tk.Canvas()
>>> canvas.pack()
>>> canvas.create_arc(10, 160, 180, 240, extent=135)
1
>>> master.mainloop()
>>> 
>>> canvas=tk.Canvas()
>>> canvas.create_arc(10, 240, 200, 400, extent=180)
1
>>> master.mainloop()
>>> 
>>> canvas=tk.Canvas()
>>> canvas.create_arc(10, 240, 200, 400, extent=180)
1
>>> canvas.pack()
>>> master.mainloop()
>>> 
>>> canvas=tk.Canvas()
>>> canvas.pack()
>>> canvas.create_arc(10, 240, 200, 400, extent=180)
1
>>> master.mainloop()
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> import Tkinter as tk
>>> import ttk
>>> import tkColorChooser
>>> master=tk.Tk()
>>> width=600
>>> height=600
>>> canvas=tk.Canvas()
>>> canvas.pack
<bound method Canvas.pack_configure of <Tkinter.Canvas instance at 0x7f5c07b0bcb0>>
>>> canvas.pack()
>>> canvas.create_arc(10, 320, 200, 400, extent=359)
1
>>> master.mainloop()
>>> canvas=tk.Canvas()
>>> canvas.pack()
>>> canvas.create_arc(10, 320, 200, 400, extent=359)
1
>>> master.mainloop()
>>> canvas=tk.Canvas(width=600, height=600)
>>> canvas.pack()
>>> canvas.create_arc(10, 320, 200, 400, extent=359)
1
>>> master.mainloop()
>>> 
>>> 
>>> app=tk.Tk()
>>> canvas=tk.Canvas(app, width=400, height=400)
>>> canvas.pack()
>>> canvas.create_polygon(10,10, 100, 10, 100, 110, fill="", outline="black")
1
>>> app.mainloop()
>>> 
>>> canvas=tk.Canvas(app, width=400, height=400)

Traceback (most recent call last):
  File "<pyshell#197>", line 1, in <module>
    canvas=tk.Canvas(app, width=400, height=400)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2234, in __init__
    Widget.__init__(self, master, 'canvas', cnf, kw)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2094, in __init__
    (widgetName, self._w) + extra + self._options(cnf))
TclError: can't invoke "canvas" command: application has been destroyed
>>> app=tk.Tk()
>>> canvas=tk.Canvas(app, width=400, height=400)
>>> canvas.pack()
>>> canvas.create_polygon(10,10, 100, 10, 100, 110, fill="", outline="black")
1
>>> app.mainloop()
>>> app=tk.Tk()
>>> canvas=tk.Canvas(app, width=400, height=400)
>>> canvas.pack()
>>> canvas.create_polygon(10,10, 100, 10, 100, 110, fill="red", outline="black")
1
>>> app.mainloop()
>>> 
>>> app=tk.Tk()
>>> canvas=tk.Canvas(app, width=400, height=400)
>>> canvas.pack()
>>> canvas.create_text(150, 100, text="There once was a man from Toulouse")
1
>>> canvas.create_text(130, 120, text='Who rode around on a moose')
2
>>> canvas.create_text(130, 120, text='Who rode around on a moose', fill='red')
3
>>> canvas.create_text(150, 150, text='He said, "It\'s my curse,', font=('Times', 15))
4
>>> canvas.create_text(200, 200, text='But it could be worse,', font=("Helvetica", 20))
5
>>> canvas.create_text(220, 250, text='My cousin rides around', font=('Courrier', 22))
6
>>> canvas.create_text(220, 300, text='on a goose."', font=('Courrier', 30))
7
>>> app.mainloop()
>>> 
>>> 
>>> app=tk.Tk()
>>> canvas=tk.Canvas(app, width=600, height=600)
>>> canvas.pack()
>>> my_image=tk.PhotoImage(file='me.gif')
>>> canvas.create_image(0,0, anchor=NW, image=myimage)

Traceback (most recent call last):
  File "<pyshell#226>", line 1, in <module>
    canvas.create_image(0,0, anchor=NW, image=myimage)
NameError: name 'NW' is not defined
>>> canvas.create_image(0,0, anchor=NW, image=myimage)

Traceback (most recent call last):
  File "<pyshell#227>", line 1, in <module>
    canvas.create_image(0,0, anchor=NW, image=myimage)
NameError: name 'NW' is not defined

>>> canvas.create_image(0,0,anchor='NW', image=myimage)

Traceback (most recent call last):
  File "<pyshell#228>", line 1, in <module>
    canvas.create_image(0,0,anchor='NW', image=myimage)
NameError: name 'myimage' is not defined
>>> canvas.create_image(0,0,anchor='NW', image=my_image)

Traceback (most recent call last):
  File "<pyshell#229>", line 1, in <module>
    canvas.create_image(0,0,anchor='NW', image=my_image)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2318, in create_image
    return self._create('image', args, kw)
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2309, in _create
    *(args + self._options(cnf, kw))))
TclError: bad anchor position "NW": must be n, ne, e, se, s, sw, w, nw, or center
>>> canvas.create_image(0,0,anchor=nw, image=my_image)

Traceback (most recent call last):
  File "<pyshell#230>", line 1, in <module>
    canvas.create_image(0,0,anchor=nw, image=my_image)
NameError: name 'nw' is not defined
>>> canvas.create_image(0,0,anchor='nw', image=my_image)
2
>>> app.mainloop()
>>> app=tk.Tk()
>>> canvas=tk.Canvas(app, width=1600, height=1600)
>>> canvas.pack()
>>> my_image=tk.PhotoImage(file='me.gif')
>>> canvas.create_image(0,0,anchor='nw', image=my_image)
1
>>> app.mainloop()
>>> 

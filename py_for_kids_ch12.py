Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from tkinter import *
ImportError: No module named tkinter
>>> import _tkinter
>>> from _tkinter import *
>>> tk = Tk()

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tk = Tk()
NameError: name 'Tk' is not defined
>>> 
=============================== RESTART: Shell ===============================
>>> import Tkinter
>>> tk=Tk()

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tk=Tk()
NameError: name 'Tk' is not defined
>>> 
=============================== RESTART: Shell ===============================
>>> import Tkinter as *
SyntaxError: invalid syntax
>>> from Tkinter import *
>>> tk =Tk()
>>> btn = Button(tk, text="click me")
>>> btn.pack()
>>> 

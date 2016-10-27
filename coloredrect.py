import random
import Tkinter as tk
def random_rectangle(width, height, fill_color) :
	x1=random.randrange(width)
	y1=random.randrange(height)
	x2=x1 + random.randrange(width)
	y2=y1 + random.randrange(height)
	canvas.create_rectangle(x1,y1,x2,y2, fill=fill_color)



window=tk.Tk()
canvas=tk.Canvas(window, width=400, height=400)
canvas.pack()
random_rectangle(400, 400, 'red')
random_rectangle(400, 400, 'green')
random_rectangle(400, 400, 'pink')
random_rectangle(400, 400, 'cyan')
random_rectangle(400, 400, 'blue')
window.mainloop()


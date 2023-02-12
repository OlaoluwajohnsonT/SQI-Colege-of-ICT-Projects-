from tkinter import *
from tkinter.messagebox import *
import time

root = Tk()

root.geometry('600x700')
var = IntVar()
canva = Canvas(root, bg = 'blue', height = 600, width = 700, relief = 'raised', borderwidth =1)
canva.pack()
dim = 5,5,60,60
ova = canva.create_oval(dim, fill = 'red')
x1 = 5
y1 = 5

while True:
	canva.move(ova, x1,y1)
	p = canva.coords(ova)
	if p[3] >= 700 or p[1] <=0:
		y1 = -y1
	if p[2]>=600 or p[0]<= 0:
		x1 = -x1
	root.update()
	time.sleep(0.01)


root.mainloop()
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import random
import sys

class Calc:
	def __init__(self):
		self.root = Tk()
		self.root.title('Calculator')
		self.root.geometry('400x600')
		self.root.config(bg = '#233857')

		self.frameb = Frame(self.root).pack()
		self.standardC()

		self.root.mainloop()

	def standardC(self):
		# self.frameb.destroy()
		self.root.geometry('200x400')
		# self.frameb = Frame(self.root)
		self.sd_lbn = Label(self.frameb, text = 'Standard Calculator',font =('arial', 15, 'bold'),
			bg = '#233857', fg = 'white').grid(columnspan = 5)
		self.main_entry = Entry(self.frameb, font =('arial', 15, 'bold'),bd = 1).grid(columnspan =9 )
		self.ans_entry = Entry(self.frameb, font =('arial', 15, 'bold'),bd = 1).grid(columnspan = 9)

		self.btn_nine = Button(self.root, height = 1,width= 3 , font = ('arial', 20, 'bold'), 
    		bg = '#f5428a', bd = 4, text = '9')
		self.btn_nine.grid(row = 5, column = 1 , pady = 1)

		self.btn_eight = Button(self.root, height = 1,width= 3 , font = ('arial', 20, 'bold'), 
    		bg = '#f5428a', bd = 4, text = '8')
		self.btn_eight.grid(row = 5, column = 2 , pady = 1)

		self.btn_seven = Button(self.root, height = 1,width= 3 , font = ('arial', 20, 'bold'),
    	 bg = '#f5428a', bd = 4, text = '7')
		self.btn_seven.grid(row = 5, column = 3 , pady = 1)

		self.btn_six = Button(self.root, height = 1,width= 3 , font = ('arial', 20, 'bold'), 
    		bg = '#f5428a', bd = 4, text = '6')
		self.btn_six.grid(row = 6, column = 1 , pady = 1)

		self.btn_five = Button(self.root, height = 1,width= 3 , font = ('arial', 20, 'bold'),
    	 bg = '#f5428a', bd = 4, text = '5')
		self.btn_five.grid(row = 6, column = 2 , pady = 1)

		self.btn_four = Button(self.root, height = 1,width= 3 , font = ('arial', 20, 'bold'), 
    		bg = '#f5428a', bd = 4, text = '4')
		self.btn_four.grid(row = 6, column = 3 , pady = 1)

		self.btn_three = Button(self.root, height = 1,width= 3 , font = ('arial', 20, 'bold'),
    	 bg = '#f5428a', bd = 4, text = '3')
		self.btn_three.grid(row = 7, column = 1 , pady = 1)

		self.btn_two = Button(self.root, height = 1,width= 3 , font = ('arial', 20, 'bold'),
    	 bg = '#f5428a', bd = 4, text = '2')
		self.btn_two.grid(row = 7, column = 2 , pady = 1)

		self.btn_one = Button(self.root, height = 1,width= 3 , font = ('arial', 20, 'bold'),
    	 bg = '#f5428a', bd = 4, text = '1')

		self.btn_one.grid(row = 7, column = 3 , pady = 1)

		# self.frameb.grid()

calculator = Calc()
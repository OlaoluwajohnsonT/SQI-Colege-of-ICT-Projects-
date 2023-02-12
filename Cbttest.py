from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import random
import sys
import mysql.connector


class Cbt:
	def __init__(self):
		self.root = Tk()
		self.root.title('Englist Test')
		self.root.config(bg = '#400f7d')
		self.root.geometry('800x400')
		self.mark = 0
		self.percent = 0
		self.count = 0

		self.frameb = Frame(self.root, width = 800, height= 400)
		self.mainPage()
		self.matric = self.matric_entry.get()

		self.root.mainloop()



	def mainPage(self):
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.frameb.config(bg = '#400f7d')
		self.lbn = Label(self.frameb, font =('Calibri', 15, 'bold'), text= 'Final Year CBT Test', bg = 'white')
		self.lbn.grid(row = 2, columnspan = 5)

		self.lbn = Label(self.frameb, font =('Calibri', 15, 'bold'), text= 'Enter Matric No:', bg = 'white')
		self.lbn.grid(row = 3 , column = 1)

		self.matric_entry = Entry(self.frameb, font =('arial', 15, 'bold'),
        	justify = 'left', width = 35, bd = 0)
		self.matric_entry.grid(row = 4 , column = 2)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = 'Start Now', command = self.questions1)
		self.start_now.grid(row = 5, column= 2)

		self.frameb.pack()
		

	def questions1(self):
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.frameb.config(bg = '#400f7d')
		self.lbn = Label(self.frameb, font =('Calibri', 15, 'bold'), 
			text= '1. She was a devoted wife and looked _______ her husband.', fg = 'white', bg = 'black')
		self.lbn.grid(columnspan = 4)
		self.que1_anwser = StringVar()
		self.frame2 = Frame(self.frameb, width = 600, height = 5, bg = 'red').grid(columnspan = 4)
		A1 = Radiobutton(self.frameb, text = 'A. at ', variable = self.que1_anwser, value = 'A', tristatevalue = 0).grid(row =3 , column = 0)
		B1 = Radiobutton(self.frameb, text = 'B. upon', variable =self.que1_anwser, value = 'B', tristatevalue = 0).grid(row =3 , column = 1)
		C1= Radiobutton(self.frameb, text = 'C. after', variable =self.que1_anwser, value = 'C', tristatevalue = 0).grid(row =3 , column = 2)
		D1 = Radiobutton(self.frameb, text = 'D. for', variable = self.que1_anwser, value = 'D', tristatevalue = 0).grid(row =3 , column = 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '>>>', command = self.questions2)
		self.start_now.grid(row = 5, column= 3)

		self.frameb.pack()

	def questions2(self):
		if self.que1_anwser.get() =='C':
			self.count += 1
			self.percent += 5
		else:
			pass
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.frameb.config(bg = '#400f7d')
		self.lbn = Label(self.frameb, font =('Calibri', 15, 'bold'), 
			text= '2. Good sleep is necessary _______ good health.', fg = 'white', bg = 'black')
		self.lbn.grid(columnspan = 4)
		self.que2_anwser = StringVar()
		self.frame2 = Frame(self.frameb, width = 600, height = 5, bg = 'red').grid(columnspan = 4)
		A = Radiobutton(self.frameb, text = 'A. from ', variable = self.que2_anwser, value = 'A', tristatevalue = 0).grid(row =3 , column = 0)
		B = Radiobutton(self.frameb, text = 'B. for', variable =self.que2_anwser, value = 'B', tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C. of', variable =self.que2_anwser, value = 'C', tristatevalue = 0).grid(row =3 , column = 2)
		D = Radiobutton(self.frameb, text = 'D. at', variable = self.que2_anwser, value = 'D', tristatevalue = 0).grid(row =3 , column = 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '>>>', command = self.questions3)
		self.start_now.grid(row = 5, column= 3)
		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '<<<', command = self.questions1)
		self.start_now.grid(row = 5, column= 0)
		self.frameb.pack()

	def questions3(self):
		if self.que2_anwser.get() =='B':
			self.count += 1
			self.percent += 5
		else:
			pass
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.frameb.config(bg = '#400f7d')
		self.lbn = Label(self.frameb, font =('Calibri', 15, 'bold'), 
			text= '3. My voice reverberated _______ the walls of the castle', fg = 'white', bg = 'black')
		self.lbn.grid(columnspan = 4)
		self.que3_anwser = StringVar()
		self.frame2 = Frame(self.frameb, width = 600, height = 5, bg = 'red').grid(columnspan = 4)
		A = Radiobutton(self.frameb, text = 'A. from ', variable = self.que3_anwser, value = 'A', tristatevalue = 0).grid(row =3 , column = 0)
		B = Radiobutton(self.frameb, text = 'B. on', variable =self.que3_anwser, value = 'B', tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C. with', variable =self.que3_anwser, value = 'C', tristatevalue = 0).grid(row =3 , column = 2)
		D = Radiobutton(self.frameb, text = 'D. in', variable =self.que3_anwser, value = 'D', tristatevalue = 0).grid(row =3 , column = 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '>>>', command = self.questions4)
		self.start_now.grid(row = 5, column= 3)
		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '<<<', command = self.questions2)
		self.start_now.grid(row = 5, column= 0)
		self.frameb.pack()

	def questions4(self):
		if self.que3_anwser.get() =='A':
			self.count += 1
			self.percent += 5
		else:
			pass
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.frameb.config(bg = '#400f7d')
		self.lbn = Label(self.frameb, font =('Calibri', 15, 'bold'), 
			text= '4. A steady minds triumphs _______ difficulties.', fg = 'white', bg = 'black')
		self.lbn.grid(columnspan = 4)
		self.que4_anwser = StringVar()
		self.frame2 = Frame(self.frameb, width = 600, height = 5, bg = 'red').grid(columnspan = 4)
		A = Radiobutton(self.frameb, text = 'A. with ', variable = self.que4_anwser, value = 'A', tristatevalue = 0).grid(row =3 , column = 0)
		B = Radiobutton(self.frameb, text = 'B. at', variable =self.que4_anwser, value = 'B', tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C. in', variable =self.que4_anwser, value = 'C', tristatevalue = 0).grid(row =3 , column = 2)
		D = Radiobutton(self.frameb, text = 'D. over', variable = self.que4_anwser, value = 'D', tristatevalue = 0).grid(row =3 , column = 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '>>>', command = self.questions5)
		self.start_now.grid(row = 5, column= 3)
		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '<<<', command = self.questions3)
		self.start_now.grid(row = 5, column= 0)
		self.frameb.pack()

	def questions5(self):
		if self.que4_anwser.get() =='D':
			self.count += 1
			self.percent += 5
		else:
			pass
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.frameb.config(bg = '#400f7d')
		self.lbn = Label(self.frameb, font =('Calibri', 15, 'bold'), 
			text= "5. Jack's mind was attuned _______ music.", fg = 'white', bg = 'black')
		self.lbn.grid(columnspan = 4)
		self.que5_anwser = StringVar()
		self.frame2 = Frame(self.frameb, width = 600, height = 5, bg = 'red').grid(columnspan = 4)
		A = Radiobutton(self.frameb, text = 'A. on ', variable = self.que5_anwser, value = 'A', tristatevalue = 0).grid(row =3 , column = 0)
		B = Radiobutton(self.frameb, text = 'B. at', variable =self.que5_anwser, value = 'B', tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C. with', variable =self.que5_anwser, value = 'C', tristatevalue = 0).grid(row =3 , column = 2)
		D = Radiobutton(self.frameb, text = 'D. to', variable = self.que5_anwser, value = 'D', tristatevalue = 0).grid(row =3 , column = 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '>>>', command  = self.questions6)
		self.start_now.grid(row = 5, column= 3)
		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '<<<', command = self.questions4)
		self.start_now.grid(row = 5, column= 0)
		self.frameb.pack()

	def questions6(self):
		if self.que5_anwser.get() =='D':
			self.count += 1
			self.percent += 5
		else:
			pass
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.frameb.config(bg = '#400f7d')
		self.lbn = Label(self.frameb, font =('Calibri', 15, 'bold'), 
			text= '6. I bought him _______ with great difficulty.', fg = 'white', bg = 'black')
		self.lbn.grid(columnspan = 4)
		self.que6_anwser = StringVar()
		self.frame = Frame(self.frameb, width = 600, height = 5, bg = 'red').grid(columnspan = 4)
		A = Radiobutton(self.frameb, text = 'A. round ', variable = self.que6_anwser, value = 'A', tristatevalue = 0).grid(row =3 , column = 0)
		B = Radiobutton(self.frameb, text = 'B. up', variable =self.que6_anwser, value = 'B', tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C. in', variable =self.que6_anwser, value = 'C', tristatevalue = 0).grid(row =3 , column = 2)
		D = Radiobutton(self.frameb, text = 'D. about', variable = self.que6_anwser, value = 'D', tristatevalue = 0).grid(row =3 , column = 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '>>>' , command = self.questions7)
		self.start_now.grid(row = 5, column= 3)
		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '<<<', command = self.questions5)
		self.start_now.grid(row = 5, column= 0)
		self.frameb.pack()

	def questions7(self):
		if self.que6_anwser.get() =='B':
			self.count += 1
			self.percent += 5
		else:
			pass
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.frameb.config(bg = '#400f7d')
		self.lbn = Label(self.frameb, font =('Calibri', 15, 'bold'), 
			text= '7. My uncle has invested a lot of money _______ farming.', fg = 'white', bg = 'black')
		self.lbn.grid(columnspan = 4)
		self.que7_anwser = StringVar()
		self.frame2 = Frame(self.frameb, width = 600, height = 5, bg = 'red').grid(columnspan = 4)
		A = Radiobutton(self.frameb, text = 'A. in ', variable = self.que7_anwser, value = 'A', tristatevalue = 0).grid(row =3 , column = 0)
		B = Radiobutton(self.frameb, text = 'B. on', variable =self.que7_anwser, value = 'B', tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C. for', variable =self.que7_anwser, value = 'C', tristatevalue = 0).grid(row =3 , column = 2)
		D = Radiobutton(self.frameb, text = 'D. into', variable = self.que7_anwser, value = 'D', tristatevalue = 0).grid(row =3 , column = 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '>>>', command = self.questions8)
		self.start_now.grid(row = 5, column= 3)
		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '<<<', command = self.questions6)
		self.start_now.grid(row = 5, column= 0)
		self.frameb.pack()

	def questions8(self):
		if self.que7_anwser.get() =='A':
			self.count += 1
			self.percent += 5
		else:
			pass
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.frameb.config(bg = '#400f7d')
		self.lbn = Label(self.frameb, font =('Calibri', 15, 'bold'), 
			text= '8. India is committed _______ a policy of peaceful existence.', fg = 'white', bg = 'black')
		self.lbn.grid(columnspan = 4)
		self.que8_anwser = StringVar()
		self.frame2 = Frame(self.frameb, width = 600, height = 5, bg = 'red').grid(columnspan = 4)
		A = Radiobutton(self.frameb, text = 'A. with ', variable = self.que8_anwser, value = 'A', tristatevalue = 0).grid(row =3 , column = 0)
		B = Radiobutton(self.frameb, text = 'B. of', variable =self.que8_anwser, value = 'B', tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C. for', variable =self.que8_anwser, value = 'C', tristatevalue = 0).grid(row =3 , column = 2)
		D = Radiobutton(self.frameb, text = 'D. to', variable = self.que8_anwser, value = 'D', tristatevalue = 0).grid(row =3 , column = 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '>>>', command = self.questions9)
		self.start_now.grid(row = 5, column= 3)
		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '<<<', command = self.questions7)
		self.start_now.grid(row = 5, column= 0)
		self.frameb.pack()

	def questions9(self):
		if self.que8_anwser.get() =='D':
			self.count += 1
			self.percent += 5
		else:
			pass
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.frameb.config(bg = '#400f7d')
		self.lbn = Label(self.frameb, font =('Calibri', 15, 'bold'), 
			text= '9. Exercise is beneficial ______ health.', fg = 'white', bg = 'black')
		self.lbn.grid(columnspan = 4)
		self.que9_anwser = StringVar()
		self.frame2 = Frame(self.frameb, width = 600, height = 5, bg = 'red').grid(columnspan = 4)
		A = Radiobutton(self.frameb, text = 'A. towards ', variable = self.que9_anwser, value = 'A', tristatevalue = 0).grid(row =3 , column = 0)
		B = Radiobutton(self.frameb, text = 'B. in', variable =self.que9_anwser, value = 'B', tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C. for', variable =self.que9_anwser, value = 'C', tristatevalue = 0).grid(row =3 , column = 2)
		D = Radiobutton(self.frameb, text = 'D. to', variable = self.que9_anwser, value = 'D', tristatevalue = 0).grid(row =3 , column = 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '>>>', command  = self.questions10)
		self.start_now.grid(row = 5, column= 3)
		self.next = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '<<<', command  = self.questions8)
		self.next.grid(row = 5, column= 0)
		self.frameb.pack()

	def questions10(self):
		if self.que9_anwser.get() =='D':
			self.count += 1
			self.percent += 5
		else:
			pass
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.frameb.config(bg = '#400f7d')
		self.lbn = Label(self.frameb, font =('Calibri', 15, 'bold'), 
			text= '10. A good judge never jumps ________ to conclusion.', fg = 'white', bg = 'black')
		self.lbn.grid(columnspan = 4)
		self.que10_anwser = StringVar()
		self.frame2 = Frame(self.frameb, width = 600, height = 5, bg = 'red').grid(columnspan = 4)
		A = Radiobutton(self.frameb, text = 'A. to ', variable = self.que10_anwser, value = 'A', tristatevalue = 0).grid(row =3 , column = 0)
		B = Radiobutton(self.frameb, text = 'B. at', variable =self.que10_anwser, value = 'B', tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C. on', variable =self.que10_anwser, value = 'C', tristatevalue = 0).grid(row =3 , column = 2)
		D = Radiobutton(self.frameb, text = 'D. for', variable = self.que10_anwser, value = 'D', tristatevalue = 0).grid(row =3 , column = 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '>>>', command  = self.questions11)
		self.start_now.grid(row = 5, column= 3)
		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '<<<', command  = self.questions9)
		self.start_now.grid(row = 5, column= 0)
		self.frameb.pack()




	def questions11(self):
		if self.que10_anwser.get() =='B':
			self.count += 1
			self.percent += 5
		else:
			pass
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.frameb.config(bg = '#400f7d')
		self.lbn = Label(self.frameb, font =('Calibri', 15, 'bold'), 
			text= '11. A good judge never gropes _______ the conclusion.', fg = 'white', bg = 'black')
		self.lbn.grid(columnspan = 4)
		self.que11_anwser = StringVar()
		self.frame2 = Frame(self.frameb, width = 600, height = 5, bg = 'red').grid(columnspan = 4)
		A = Radiobutton(self.frameb, text = 'A. in ', variable = self.que11_anwser, value = 'A', tristatevalue = 0).grid(row =3 , column = 0)
		B = Radiobutton(self.frameb, text = 'B. on', variable =self.que11_anwser, value = 'B', tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C. for', variable =self.que11_anwser, value = 'C', tristatevalue = 0).grid(row =3 , column = 2)
		D = Radiobutton(self.frameb, text = 'D. into', variable = self.que11_anwser, value = 'D', tristatevalue = 0).grid(row =3 , column = 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '>>>', command  = self.questions12)
		self.start_now.grid(row = 5, column= 3)
		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '<<<', command  = self.questions10)
		self.start_now.grid(row = 5, column= 0)
		self.frameb.pack()

	def questions12(self):
		if self.que11_anwser.get() =='C':
			self.count += 1
			self.percent += 5
		else:
			pass
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.frameb.config(bg = '#400f7d')
		self.lbn = Label(self.frameb, font =('Calibri', 15, 'bold'), 
			text= '12. The principal called _______ the names of the winners.', fg = 'white', bg = 'black')
		self.lbn.grid(columnspan = 4)
		self.que12_anwser = StringVar()
		self.frame2 = Frame(self.frameb, width = 600, height = 5, bg = 'red').grid(columnspan = 4)
		A = Radiobutton(self.frameb, text = 'A. at ', variable = self.que12_anwser, value = 'A', tristatevalue = 0).grid(row =3 , column = 0)
		B = Radiobutton(self.frameb, text = 'B. on', variable =self.que12_anwser, value = 'B', tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C. for', variable =self.que12_anwser, value = 'C', tristatevalue = 0).grid(row =3 , column = 2)
		D = Radiobutton(self.frameb, text = 'D. out', variable = self.que12_anwser, value = 'D', tristatevalue = 0).grid(row =3 , column = 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '>>>',  command  = self.questions13)
		self.start_now.grid(row = 5, column= 3)
		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '<<<', command  = self.questions11)
		self.start_now.grid(row = 5, column= 0)
		self.frameb.pack()


	def questions13(self):
		if self.que12_anwser.get() =='D':
			self.count += 1
			self.percent += 5
		else:
			pass
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.frameb.config(bg = '#400f7d')
		self.lbn = Label(self.frameb, font =('Calibri', 15, 'bold'), 
			text= "13. Siva has no control ______ his temper.", fg = 'white', bg = 'black')
		self.lbn.grid(columnspan = 4)
		self.que13_anwser = StringVar()
		self.frame2 = Frame(self.frameb, width = 600, height = 5, bg = 'red').grid(columnspan = 4)
		A = Radiobutton(self.frameb, text = 'A. in ', variable = self.que13_anwser, value = 'A', tristatevalue = 0).grid(row =3 , column = 0)
		B = Radiobutton(self.frameb, text = 'B. after', variable =self.que13_anwser, value = 'B', tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C. at', variable =self.que13_anwser, value = 'C', tristatevalue = 0).grid(row =3 , column = 2)
		D = Radiobutton(self.frameb, text = 'D. over', variable = self.que13_anwser, value = 'D', tristatevalue = 0).grid(row =3 , column = 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '>>>', command  = self.questions14)
		self.start_now.grid(row = 5, column= 3)
		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '<<<', command  = self.questions12)
		self.start_now.grid(row = 5, column= 0)
		self.frameb.pack()

	def questions14(self):
		if self.que13_anwser.get() =='D':
			self.count += 1
			self.percent += 5
		else:
			pass
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.frameb.config(bg = '#400f7d')
		self.lbn = Label(self.frameb, font =('Calibri', 15, 'bold'), 
			text= "14. He was advised to abstain ________ all alcoholic drinks.", fg = 'white', bg = 'black')
		self.lbn.grid(columnspan = 4)
		self.que14_anwser = StringVar()
		self.frame2 = Frame(self.frameb, width = 600, height = 5, bg = 'red').grid(columnspan = 4)
		A = Radiobutton(self.frameb, text = 'A. tp ', variable = self.que14_anwser, value = 'A', tristatevalue = 0).grid(row =3 , column = 0)
		B = Radiobutton(self.frameb, text = 'B. at', variable =self.que14_anwser, value = 'B', tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C. from', variable =self.que14_anwser, value = 'C', tristatevalue = 0).grid(row =3 , column = 2)
		D = Radiobutton(self.frameb, text = 'D. for', variable = self.que14_anwser, value = 'D', tristatevalue = 0).grid(row =3 , column = 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '>>>', command  = self.questions15)
		self.start_now.grid(row = 5, column= 3)
		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '<<<', command  = self.questions14)
		self.start_now.grid(row = 5, column= 0)
		self.frameb.pack()

	def questions15(self):
		if self.que14_anwser.get() =='C':
			self.count += 1
			self.percent += 5
		else:
			pass
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.frameb.config(bg = '#400f7d')
		self.lbn = Label(self.frameb, font =('Calibri', 15, 'bold'), 
			text= "15. Minority asoirations cannot forever be kept in check _______ the gun.", fg = 'white', bg = 'black')
		self.lbn.grid(columnspan = 4)
		self.que15_anwser = StringVar()
		self.frame2 = Frame(self.frameb, width = 600, height = 5, bg = 'red').grid(columnspan = 4)
		A = Radiobutton(self.frameb, text = 'A. from ', variable = self.que15_anwser, value = 'A', tristatevalue = 0).grid(row =3 , column = 0)
		B = Radiobutton(self.frameb, text = 'B. by', variable =self.que15_anwser, value = 'B', tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C. under', variable =self.que15_anwser, value = 'C', tristatevalue = 0).grid(row =3 , column = 2)
		D = Radiobutton(self.frameb, text = 'D. with', variable = self.que15_anwser, value = 'D', tristatevalue = 0).grid(row =3 , column = 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '>>>', command  = self.questions16)
		self.start_now.grid(row = 5, column= 3)
		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '<<<', command  = self.questions14)
		self.start_now.grid(row = 5, column= 0)
		self.frameb.pack()

	def questions16(self):
		if self.que15_anwser.get() =='A':
			self.count += 1
			self.percent += 5
		else:
			pass
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.frameb.config(bg = '#400f7d')
		self.lbn = Label(self.frameb, font =('Calibri', 15, 'bold'), 
			text= "16.	_______ the whole, I like the book very much.", fg = 'white', bg = 'black')
		self.lbn.grid(columnspan = 4)
		self.que16_anwser = StringVar()
		self.frame2 = Frame(self.frameb, width = 600, height = 5, bg = 'red').grid(columnspan = 4)
		A = Radiobutton(self.frameb, text = 'A. from ', variable = self.que16_anwser, value = 'A', tristatevalue = 0).grid(row =3 , column = 0)
		B = Radiobutton(self.frameb, text = 'B. on', variable =self.que16_anwser, value = 'B', tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C. at', variable =self.que16_anwser, value = 'C', tristatevalue = 0).grid(row =3 , column = 2)
		D = Radiobutton(self.frameb, text = 'D. in', variable = self.que16_anwser, value = 'D', tristatevalue = 0).grid(row =3 , column = 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '>>>', command  = self.questions17)
		self.start_now.grid(row = 5, column= 3)
		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '<<<', command  = self.questions15)
		self.start_now.grid(row = 5, column= 0)
		self.frameb.pack()

	def questions17(self):
		if self.que16_anwser.get() =='B':
			self.count += 1
			self.percent += 5
		else:
			pass
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.frameb.config(bg = '#400f7d')
		self.lbn = Label(self.frameb, font =('Calibri', 15, 'bold'), 
			text= "17. My relations ______Suganya are good", fg = 'white', bg = 'black')
		self.lbn.grid(columnspan = 4)
		self.que17_anwser = StringVar()
		self.frame2 = Frame(self.frameb, width = 600, height = 5, bg = 'red').grid(columnspan = 4)
		A = Radiobutton(self.frameb, text = 'A. with ', variable = self.que17_anwser, value = 'A', tristatevalue = 0).grid(row =3 , column = 0)
		B = Radiobutton(self.frameb, text = 'B. on', variable =self.que17_anwser, value = 'B', tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C. against', variable =self.que17_anwser, value = 'C', tristatevalue = 0).grid(row =3 , column = 2)
		D = Radiobutton(self.frameb, text = 'D. to', variable = self.que17_anwser, value = 'D', tristatevalue = 0).grid(row =3 , column = 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '>>>', command  = self.questions18)
		self.start_now.grid(row = 5, column= 3)
		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '<<<', command  = self.questions16)
		self.start_now.grid(row = 5, column= 0)
		self.frameb.pack()

	def questions18(self):
		if self.que17_anwser.get() =='A':
			self.count += 1
			self.percent += 5
		else:
			pass
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.frameb.config(bg = '#400f7d')
		self.lbn = Label(self.frameb, font =('Calibri', 15, 'bold'), 
			text= "18. The teacher has no control ________ the students.", fg = 'white', bg = 'black')
		self.lbn.grid(columnspan = 4)
		self.que18_anwser = StringVar()
		self.frame2 = Frame(self.frameb, width = 600, height = 5, bg = 'red').grid(columnspan = 4)
		A = Radiobutton(self.frameb, text = 'A. over ', variable = self.que18_anwser, value = 'A', tristatevalue = 0).grid(row =3 , column = 0)
		B = Radiobutton(self.frameb, text = 'B. on', variable =self.que18_anwser, value = 'B', tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C. with', variable =self.que18_anwser, value = 'C', tristatevalue = 0).grid(row =3 , column = 2)
		D = Radiobutton(self.frameb, text = 'D. at', variable = self.que18_anwser, value = 'D', tristatevalue = 0).grid(row =3 , column = 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '>>>', command  = self.questions19)
		self.start_now.grid(row = 5, column= 3)
		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '<<<', command  = self.questions17)
		self.start_now.grid(row = 5, column= 0)
		self.frameb.pack()

	def questions19(self):
		if self.que18_anwser.get() =='A':
			self.count += 1
			self.percent += 5
		else:
			pass
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.frameb.config(bg = '#400f7d')
		self.lbn = Label(self.frameb, font =('Calibri', 15, 'bold'), 
			text= "19. I am angry with him _______ his carelessness.", fg = 'white', bg = 'black')
		self.lbn.grid(columnspan = 4)
		self.que19_anwser = StringVar()
		self.frame2 = Frame(self.frameb, width = 600, height = 5, bg = 'red').grid(columnspan = 4)
		A = Radiobutton(self.frameb, text = 'A. in ', variable = self.que19_anwser, value = 'A', tristatevalue = 0).grid(row =3 , column = 0)
		B = Radiobutton(self.frameb, text = 'B. for', variable =self.que19_anwser, value = 'B', tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C. at', variable =self.que19_anwser, value = 'C', tristatevalue = 0).grid(row =3 , column = 2)
		D = Radiobutton(self.frameb, text = 'D. on', variable = self.que19_anwser, value = 'D', tristatevalue = 0).grid(row =3 , column = 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '>>>', command  = self.questions20)
		self.start_now.grid(row = 5, column= 3)
		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '<<<', command  = self.questions18)
		self.start_now.grid(row = 5, column= 0)
		self.frameb.pack()

	def questions20(self):
		if self.que19_anwser.get() =='B':
			self.count += 1
			self.percent += 5
		else:
			pass
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.frameb.config(bg = '#400f7d')
		self.lbn = Label(self.frameb, font =('Calibri', 15, 'bold'), 
			text= "20. There is no exception _______ this rule.", fg = 'white', bg = 'black')
		self.lbn.grid(columnspan = 4)
		self.que20_anwser = StringVar()
		self.frame2 = Frame(self.frameb, width = 600, height = 5, bg = 'red').grid(columnspan = 4)
		A = Radiobutton(self.frameb, text = 'A. in ', variable = self.que20_anwser, value = 'A', tristatevalue= 1).grid(row =3 , column = 0)
		B = Radiobutton(self.frameb, text = 'B. to', variable =self.que20_anwser, value = 'B', tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C. for', variable =self.que20_anwser, value = 'C', tristatevalue = 0).grid(row =3 , column = 2)
		D = Radiobutton(self.frameb, text = 'D. about', variable = self.que20_anwser, value = 'D', tristatevalue = 0).grid(row =3 , column = 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = 'Finish', command = self.markFunction)
		self.start_now.grid(row = 5, column= 3)
		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = '<<<', command  = self.questions19)
		self.start_now.grid(row = 5, column= 0)
		self.frameb.pack()

	def markFunction(self):
		if self.que1_anwser.get() =='B':
			self.count += 1
			self.percent += 5
		else:
			pass
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.frameb.config(bg = '#400f7d')
		self.lbn = Label(self.frameb, font =('Calibri', 15, 'bold'), 
			text= ("Hello! " + str(self.matric)+ 'You have completed your test'), fg = 'white', bg = 'black')
		self.lbn.grid(columnspan = 4)

		self.lbn2 = Label(self.frameb, font =('Calibri', 15, 'bold'), 
			text= ("you score " + str(self.count)), fg = 'white', bg = 'black')
		self.lbn2.grid(columnspan = 4)

		self.lbn2 = Label(self.frameb, font =('Calibri', 15, 'bold'), 
			text= ("Your Final Graduation pacentage is " + str(self.percent)+'%'), fg = 'white', bg = 'black')
		self.lbn2.grid(columnspan = 4)

		self.frameb.pack()

		



		











































		# Que1 = self.que1_anwser.get()
		# Que2 = self.que2_anwser.get()
		# Que3 = self.que3_anwser.get()
		# Que4 = self.que4_anwser.get()
		# Que5 = self.que5_anwser.get()
		# Que6 = self.que6_anwser.get()
		# Que7 = self.que7_anwser.get()
		# Que8 = self.que8_anwser.get()
		# Que9 = self.que9_anwser.get()
		# Que10 = self.que10_anwser.get()
		# Que11 = self.que11_anwser.get()
		# Que12 = self.que12_anwser.get()
		# Que13 = self.que13_anwser.get()
		# Que14 = self.que14_anwser.get()
		# Que15 = self.que15_anwser.get()
		# Que16 = self.que16_anwser.get()
		# Que17 = self.que17_anwser.get()
		# Que18 = self.que18_anwser.get()
		# Que19 = self.que19_anwser.get()
		# Que20 = self.que20_anwser.get()



		
		# real_anwsers = ['C', 'B', 'A','D', 'D', 'B', 'A', 'D', 'D', 'B', 'C', 'D', 'D', 'C', 'A', 'B','A', 'A', 'B', 'B']
		# Student_choice = [Que1, Que2,Que3,Que4,Que5,Que6,Que7,Que8,Que9,Que10,Que11,Que12,Que13,Que14,Que15,Que16,Que17,Que18,Que19,Que20]
		# for real in real_anwsers:
		# 	for choice in Student_choice:
		# 		if real[self.count] == choice[self.count]:
		# 			self.mark += 1
		# 			self.percent +=5
		# 		else:
		# 			pass
		# 		self.count += 1

		# else:
		# 	print('You score'' '+ str(self.mark))
		# 	print('Your pacentage is '' '+ str(self.percent)+'%')

			









C = Cbt()
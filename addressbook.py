from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.filedialog import *
import random
import sys
import numpy as np
import mysql.connector
from PIL import ImageTk, Image, ImageGrab

mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'Adressbook_db')
mycursor = mydb.cursor()

class Addressbook:
	def __init__(self):
		self.root = Tk()
		self.root.title('Advance Contact Book')
		self.root.geometry('800x600')
		self.iD = None
		# self.root.config(bg = '#112573' )

		self.header1_lbn = Label(self.root, text = 'My Address Book', font = ('arial', 20, 'bold'), bg = '#4f0b05', fg = 'white')
		self.header1_lbn.place(x = 300, y = 0, width  = 250)

		# for the frame_entry
		self.header_lbn = Label(self.root, text = 'Contact Details', font = ('arial', 20, 'bold'), fg = '#4f0b05').place(x = 50, y = 30)
		self.fullname_lbn = Label(self.root, text = 'Full Name', font = ('arial', 14, 'bold'), fg = '#4f0b05').place(x = 50, y = 70)
		self.fullname_lbn = Label(self.root, text = 'Phone No', font = ('arial', 14, 'bold'), fg = '#4f0b05').place(x = 50, y = 100)
		self.fullname_lbn = Label(self.root, text = 'Sex', font = ('arial', 14, 'bold'), fg = '#4f0b05').place(x = 50, y = 130)
		self.fullname_lbn = Label(self.root, text = 'Email', font = ('arial', 14, 'bold'), fg = '#4f0b05').place(x = 50, y = 160)
		self.image_lbn = Label(self.root, text = 'Image', font = ('arial', 14, 'bold'), fg = '#4f0b05').place(x =50, y =190)   

		self.fullname_entry = Entry(self.root, width = 25, font = ('arial', 14, 'bold'))
		self.fullname_entry.place(x = 150, y = 70)

		self.phone_entry = Entry(self.root, width = 25, font = ('arial', 14, 'bold'))
		self.phone_entry.place(x = 150, y = 100)

		self.sex_entry = Entry(self.root, width = 25, font = ('arial', 14, 'bold'))
		self.sex_entry.place(x = 150, y = 130)

		self.email_entry = Entry(self.root ,width = 25, font = ('arial', 14, 'bold'))
		self.email_entry.place(x = 150, y = 160)

		self.image_entry = Entry(self.root, width = 40, font = ('arial', 8, 'bold'))
		self.image_entry.place(x = 150, y = 190) 

		self.image_btn = Button(self.root, text = 'Browse', fg = '#4f0b05', command = self.browseFunc).place(x = 380, y = 190)

		#for the picture
		loadcursor = Image.open('C:/PHYTON CLASS/Iconimage/contacticon.png')
		loadcursor.resize((10, 10), Image.ANTIALIAS)
		self.image_cursor = ImageTk.PhotoImage(loadcursor, master = self.root)
        

		self.image_display = Label(self.root, width  = 220, height = 200, bg = '#4f0b05', image = self.image_cursor )
		self.image_display.place(x = 500, y = 50)


		#for button
		self.add_btn = Button(self.root, text = 'ADD',font = ('arial', 10, 'bold'), fg = '#4f0b05', command = self.addFunction).place(x = 150, y = 220) 
		self.update_btn = Button(self.root, text = 'UPDATE',  font = ('arial', 10, 'bold'), fg = '#4f0b05',  command = self.updateFunc).place(x = 200, y = 220) 
		self.delete_btn = Button(self.root, text = 'DELETE',  font = ('arial', 10, 'bold'), fg = '#4f0b05', command = lambda:self.curSelect('delete')).place(x = 250, y = 220) 
		self.sort_btn = Button(self.root, text = 'SORT',  font = ('arial', 10, 'bold'), fg = '#4f0b05', command = self.sortFunc).place(x = 320, y = 220)
		self.exit_btn = Button(self.root, text = 'EXIT',  font = ('arial', 10, 'bold'), fg = '#4f0b05', command = self.exitFunc).place(x = 380, y = 220) 

		#for display contact
		self.textframe = Frame(self.root, width =248, height  = 350, bg = '#4f0b05').place(x = 150, y =260)
		self.selcontact = StringVar()
		self.yscrol = Scrollbar(self.root, orient = 'vertical')
		self.listbox = Listbox(self.root, yscrollcommand = self.yscrol.set, width = 34, height =21,  font = ('arial', 10, 'bold' ))
		self.yscrol.config(command = self.listbox.yview)
		self.yscrol.place()
		self.listbox.place(x = 153, y =263)

		#for search
		self.searchframe = Frame(self.root, width =350, height  = 80, bg = '#4f0b05').place(x = 420, y =263)
		self.selcontact = StringVar()
		self.namesearch_lbn = Label(self.searchframe, text = 'Name Search:', font = ('arial', 10, 'bold'),  bg = '#4f0b05', fg = 'white').place(x = 420, y = 263)
		self.phonesearch_lbn = Label(self.searchframe, text = 'Phone Search:', font = ('arial', 10, 'bold'),  bg = '#4f0b05', fg = 'white').place(x = 420, y = 293)

		self.ns_entry = Entry(self.root, width = 25, font = ('arial', 10, 'bold'))
		self.ns_entry.place(x = 520, y = 263)
		

		self.ps_entry = Entry(self.root, width = 25, font = ('arial', 10, 'bold'))
		self.ps_entry.place(x = 520, y = 293)
		

		self.nmsearch_btn = Button(self.root, text = 'Search',font = ('arial', 8, 'bold'), fg = '#4f0b05', command = self.namesearch).place(x = 700, y = 263)
		self.pssearch_btn = Button(self.root, text = 'Search',font = ('arial',8, 'bold'), fg = '#4f0b05', command = self.phonesearch).place(x = 700, y = 293)
		self.reset_btn = Button(self.root, text = 'Reset',font = ('arial', 10, 'bold'), fg = '#4f0b05', command = self.resetFunc).place(x = 560, y = 315)
		self.search_btn = Button(self.root, text = 'Display',font = ('arial', 10, 'bold'), fg = '#4f0b05', command = lambda:self.curSelect('display')).place(x = 620, y = 315)

		#for displaytext
		self.display_text = Text(self.root, width  =50, height = 15, font = ('arial', 10, 'bold') )
		self.display_text.place(x = 420, y = 345)

		self.displayFunc()

		self.root.mainloop()

	def addFunction(self):
		mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'Adressbook_db')
		mycursor = mydb.cursor()

		name = self.fullname_entry.get()
		phone = self.phone_entry.get()
		sex = self.sex_entry.get()
		email = self.email_entry.get()
		image = self.image_entry.get()

		query  = ("INSERT INTO contact_tb (Full_name, Phone, Sex, Email, Image_path ) VALUES('%s', '%s', '%s','%s' ,'%s')" %(name, phone, sex, email, image))
		mycursor.execute(query)
		mydb.commit()
		if mycursor.rowcount ==1:
				showinfo('Message', 'Added Succesfully!')
		else:
			showinfo('Message', 'Added failed')

	def displayFunc(self):
		mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'Adressbook_db')
		mycursor = mydb.cursor()
		query = "SELECT * FROM contact_tb"
		mycursor.execute(query)
		self.contact_info = mycursor.fetchall()
		for c in self.contact_info:
			con = str(c[0])+'. ' + c[1]+ ": "+ c[2]
			self.listbox.insert('end', con)
		self.listbox.bind('<<ListboxSelect>>', self.curSelect)

	def exitFunc(self):
		msg = askyesno('Warning','Do you want to Exit?')
		if msg == True:
			self.root.destroy()
		else:
			pass	
	def deleteFunc(self):
		pass

	def curSelect(self, event):
		mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'Adressbook_db')
		mycursor = mydb.cursor()
		self.selcontact.set(self.listbox.get(self.listbox.curselection()))
		self.sel = self.selcontact.get()
		split  = self.sel.split(' ')
		self.nm = split[0].split('.')[1]
		self.nm = self.nm.split(':')[0]
		self.ph = split[1]
		self.iD = split[0].split('.')[0]\
		#function for image display
		self.imageFunc()
		self.clearFunc()
		query = "SELECT * FROM contact_tb WHERE contact_id="+self.iD
		mycursor.execute(query)
		detail= mycursor.fetchone()
		print(detail)
		self.fullname_entry.insert(0, detail[1])
		self.phone_entry.insert(0, detail[2])
		self.sex_entry.insert(0, detail[3])
		self.email_entry.insert(0, detail[4])
		self.image_entry.insert(0, detail[5])

		if event == 'delete':
			mycursor.execute("DELETE FROM contact_tb WHERE contact_id = {}".format(self.iD))
			mydb.commit()
			self.listbox.delete(self.listbox.curselection())
			
		if event == 'display':
			self.display_text.delete('1.0', END)
			query = "SELECT * FROM contact_tb WHERE contact_id ="+str(self.iD)
			mycursor.execute(query)
			self.contact_info = mycursor.fetchone()
			delt = self.contact_info
			self.display_text.insert(END, 'First and Second name are '+delt[1]+'\n')
			self.display_text.insert(END, 'Yes!! A Strong '+delt[3]+'\n')
			self.display_text.insert(END, delt[2]+' is the number Yeah, Beep me'+'\n')
			self.display_text.insert(END, 'Email on this here '+delt[4]+'\n')


	def sortFunc(self):
		self.listbox.delete(0, 'end')
		query = "SELECT * FROM contact_tb order by Full_name asc"
		mycursor.execute(query)
		self.contact_info = mycursor.fetchall()
		for c in self.contact_info:
			con = str(c[0])+'. ' + c[1]+ ": "+ c[2]
			self.listbox.insert('end', con)
		self.listbox.bind('<<ListboxSelect>>', self.curSelect)

	def phonesearch(self):
		self.listbox.delete(0, 'end')
		ps = self.ps_entry.get()
		query = "SELECT * FROM contact_tb WHERE Phone ="+str(ps)
		mycursor.execute(query)
		self.contact_info = mycursor.fetchall()
		for c in self.contact_info:
			con = str(c[0])+'. ' + c[1]+ ": "+ c[2]
			self.listbox.insert('end', con)
		self.listbox.bind('<<ListboxSelect>>', self.curSelect)
	def namesearch(self):
		
		ns = self.ns_entry.get()
		print(ns)
		query = "SELECT * FROM contact_tb WHERE Full_name ="+str(ns)
		mycursor.execute(query)
		self.contact_info = mycursor.fetchall()
		for c in self.contact_info:
			con = str(c[0])+'. ' + c[1]+ ": "+ c[2]
			self.listbox.insert('end', con)
		self.listbox.bind('<<ListboxSelect>>', self.curSelect)
	def resetFunc(self):
		self.clearFunc()
		self.listbox.delete(0, 'end')
		self.displayFunc()

	def browseFunc(self):
		self.image_entry.delete(0,END)
		image = askopenfilename(initialdir = '/', title = 'Select File')
		self.image_entry.insert(END, image)

	def imageFunc(self):
		self.image_display.destroy()
		query = "SELECT Image_path FROM contact_tb WHERE contact_id="+self.iD
		mycursor.execute(query)
		self.imageD= mycursor.fetchone()
		real_image = self.imageD[0]
		loadcursor = Image.open(real_image)
		loadcursor.resize((10, 10), Image.ANTIALIAS)
		self.image_cursor = ImageTk.PhotoImage(loadcursor, master = self.root)

		self.image_display = Label(self.root, width  = 220, height = 200, bg = '#4f0b05', image = self.image_cursor )
		self.image_display.place(x = 500, y = 50)

	def clearFunc(self): 
		self.fullname_entry.delete(0, END)
		self.phone_entry.delete(0, END)
		self.sex_entry.delete(0, END)
		self.email_entry.delete(0, END)
		self.image_entry.delete(0,END)

	def updateFunc(self):
		mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'Adressbook_db')
		mycursor = mydb.cursor()
		name = self.fullname_entry.get()
		phone = self.phone_entry.get()
		sex = self.sex_entry.get()
		email = self.email_entry.get()
		image = self.image_entry.get()

		query = "UPDATE contact_tb set Full_name =%s, Phone = %s, Sex = %s, Email = %s , Image_path=%s WHERE contact_id = %s"
		values = (name, phone, sex, email, image, self.iD)
		mycursor.execute(query, values)
		mydb.commit()
		print('updated')





			






add = Addressbook()
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import random
import sys
import numpy as np
import mysql.connector
mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'contactbook_db')
mycursor = mydb.cursor()

class Contactbook:
	def __init__(self):
		self.root = Tk()
		self.root.title('Advance Contact Book')
		self.root.geometry('400x600')
		self.root.config(bg = '#7a3d46' )
		self.Regcontact = []

		self.frame_btn = Frame(self.root, width = 300 ,height = 600, bg= '#7a3d46', relief = RIDGE)
		self.frame_btn.pack(side = TOP)
		self.add_btn = Button(self.frame_btn, text = 'ADD',bg = '#7a3d46', fg = 'white',  command = self.add_Function).grid(row = 0, column = 0)
		self.update_btn = Button(self.frame_btn, text = 'UPDATE', bg = '#7a3d46', fg = 'white', command = lambda:self.curSelect('update')).grid(row = 0, column = 1)
		self.display_btn = Button(self.frame_btn, text = 'DISPLAY', bg = '#7a3d46', fg = 'white', command = lambda:self.curSelect('display')).grid(row = 0, column = 2)
		self.delete_btn = Button(self.frame_btn, text = 'DELETE', bg = '#7a3d46', fg = 'white', command = lambda:self.curSelect('delete')).grid(row = 0, column = 3)
		self.db_btn = Button(self.frame_btn, text = 'DASHBAORD', bg = '#7a3d46', fg = 'white', command =self.dashbaord_btn).grid(row = 0, column = 4)

		self.frame1 = Frame(self.root, width = 600 ,height = 100, bg= 'white', relief = RIDGE)
		self.frame1.pack(side = TOP)
		self.contactname = StringVar()
		self.contactinfo = Label(self.frame1, textvariable= self.contactname, font = ('arial', 20, 'bold')).grid(columnspan = 3)
		

		self.frame_real = Frame(self.root, width = 300, height = 600, bg = '#7a3d46' ,relief = RIDGE)
		self.dashbaord_btn()

		

		self.root.mainloop()

	def add_Function(self):
		self.frame_real.destroy()
		self.frame_real = Frame(self.root)
		self.flbn = Label(self.frame_real, text = ' Add New Contact', font = ('arial', 20, 'bold')).grid(columnspan = 7)

		self.fname_lbn = Label(self.frame_real, text = 'First Name', font = ('arial', 10, 'bold')).grid(row =1, column = 0)
		self.lname_lbn = Label(self.frame_real, text = 'Last Name', font = ('arial', 10, 'bold')).grid(row =2, column = 0)
		self.nickname_lbn = Label(self.frame_real, text = 'Nickname', font = ('arial', 10, 'bold')).grid(row =3, column = 0)
		self.company_lbn = Label(self.frame_real, text = 'Company Name', font = ('arial', 10, 'bold')).grid(row =4, column = 0)
		self.title_lbn = Label(self.frame_real, text = 'Title', font = ('arial', 10, 'bold')).grid(row =5, column = 0)
		self.phone_lbn = Label(self.frame_real, text = 'Phone Number', font = ('arial', 10, 'bold')).grid(row =6, column = 0)
		self.email_lbn = Label(self.frame_real, text = 'Email', font = ('arial', 10, 'bold')).grid(row =7, column = 0)
		self.address_lbn = Label(self.frame_real, text = 'Resident Address', font = ('arial', 10, 'bold')).grid(row =8, column = 0)
		self.website_lbn = Label(self.frame_real, text = 'Website', font = ('arial', 10, 'bold')).grid(row =9, column = 0)
		self.relationship_lbn = Label(self.frame_real, text = 'Relationship', font = ('arial', 10, 'bold')).grid(row =10, column = 0)
		self.city_lbn = Label(self.frame_real, text = 'City', font = ('arial', 10, 'bold')).grid(row =11, column = 0)
		self.state_lbn = Label(self.frame_real, text = 'State', font = ('arial', 10, 'bold')).grid(row =12, column = 0)
		self.zip_lbn = Label(self.frame_real, text = 'Zip Code', font = ('arial', 10, 'bold')).grid(row =13, column = 0)

		self.fname_entry = Entry(self.frame_real)
		self.fname_entry.grid(row = 1, column = 3)

		self.lname_entry = Entry(self.frame_real)
		self.lname_entry.grid(row = 2, column = 3)

		self.nickname_entry = Entry(self.frame_real)
		self.nickname_entry.grid(row = 3, column = 3)

		self.company_entry = Entry(self.frame_real)
		self.company_entry.grid(row = 4, column = 3)

		self.title_entry = Entry(self.frame_real)
		self.title_entry.grid(row = 5, column = 3)

		self.phone_entry = Entry(self.frame_real)
		self.phone_entry.grid(row = 6, column = 3)

		self.email_entry = Entry(self.frame_real)
		self.email_entry.grid(row = 7, column = 3)

		self.address_entry = Entry(self.frame_real)
		self.address_entry.grid(row = 8, column = 3)

		self.website_entry = Entry(self.frame_real)
		self.website_entry.grid(row = 9, column = 3)

		self.relationship_entry = Entry(self.frame_real)
		self.relationship_entry.grid(row = 10, column = 3)

		self.city_entry = Entry(self.frame_real)
		self.city_entry.grid(row = 11, column = 3)

		self.state_entry = Entry(self.frame_real)
		self.state_entry.grid(row = 12, column = 3)

		self.zip_entry = Entry(self.frame_real)
		self.zip_entry.grid(row = 13, column = 3)

		self.submit_now = Button(self.frame_real, text='Create Now' , bg = '#7a3d46', fg = 'white', command	 = self.addfunction).grid(row = 14, column = 3)
		self.frame_real.pack()

	def addfunction(self):
		mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'contactbook_db')
		mycursor = mydb.cursor()

		self.firstname = self.fname_entry.get()
		lname = self.lname_entry.get()
		nickname = self.nickname_entry.get()
		company = self.company_entry.get()
		city = self.city_entry.get()
		state = self.state_entry.get()
		Zip = self.zip_entry.get()
		relationship  = self.relationship_entry.get()
		email = self.email_entry.get()
		self.realphone  = self.phone_entry.get()
		title = self.title_entry.get()
		address = self.address_entry.get()
		website = self.website_entry.get()

		con = self.firstname +': '+self.realphone
		self.Regcontact.append(con)
		print(con)

		myquery = ("INSERT INTO contact_tb (First_name,Last_name, Nickname, Company , Title, Phone, email, address, Website, Relationship, City, State, Zip_code) VALUES('%s', '%s', '%s','%s', '%s', '%s','%s', '%s', '%s','%s', '%s', '%s', '%s')" 
			%(self.firstname, lname, nickname, company, title, self.realphone, email, address, website, relationship, city, state, Zip))
		mycursor.execute(myquery)
		mydb.commit()
		if mycursor.rowcount ==1:
				self.display_btn()
				showinfo('Message', 'Added Succesfully!')
		else:
			showinfo('Message', 'Added failed')


		self.frame_real.pack()

	def dashbaord_btn(self):
		self.frame_real.destroy()
		self.frame_real = Frame(self.root)
		mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'contactbook_db')
		mycursor = mydb.cursor()
		query = "SELECT * FROM contact_tb"
		mycursor.execute(query)
		info = mycursor.fetchall()
		self.yscrol = Scrollbar(self.frame_real, orient = 'vertical')
		self.listbox = Listbox(self.frame_real, yscrollcommand = self.yscrol.set, width = 40, height = 200 )
		self.yscrol.config(command = self.listbox.yview)
		self.yscrol.grid(row = 2, column = 1, sticky = 'ns')
		self.listbox.grid(row=2, column = 1)
		self.selcontact = StringVar()

		for c in info:
			co = str(c[0]) +'.'+ c[1] +': '+ c[6]
			self.listbox.insert('end', co)
		self.listbox.bind('<<ListboxSelect>>', self.curSelect)

		self.frame_real.pack()

	def curSelect(self, event):
		mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'contactbook_db')
		mycursor = mydb.cursor()
		self.selcontact.set(self.listbox.get(self.listbox.curselection()))
		self.sel = self.selcontact.get()
		split  = self.sel.split(' ')
		self.nm = split[0].split('.')[1]
		self.nm = self.nm.split(':')[0]
		self.ph = split[1]
		iD = split[0].split('.')[0]
		print(iD)

		if event == 'display':
			query = "SELECT * FROM contact_tb WHERE First_name = %s and Phone=%s"
			values = (self.nm, self.ph)
			mycursor.execute(query, values)
			self.detail = mycursor.fetchone()
			self.contactname.set(self.detail[1]+' '+self.detail[2])
			self.displayall()
		if event== 'delete':
			mycursor.execute("DELETE FROM contact_tb WHERE contact_id = "+str(iD))
			mydb.close()
			# values = (self.nm, self.ph)
			# mycursor.execute(query, values)
		if event == 'update':
			query = "SELECT * FROM contact_tb WHERE First_name = %s and Phone=%s"
			values = (self.nm, self.ph)
			mycursor.execute(query, values)
			self.detail = mycursor.fetchone()
			self.contactname.set(self.detail[1]+' '+self.detail[2])
			self.update()


	def displayall(self):
		self.frame_real.destroy()
		self.frame_real = Frame(self.root)

		self.flbn = Label(self.frame_real, text = self.detail[3] , font = ('arial', 15, 'bold'), fg = 'red').grid(columnspan = 5)
		
		self.fname_lbn = Label(self.frame_real, text = 'First Name: '+ self.detail[1], font = ('arial', 10, 'bold')).grid(row =1, column = 0)
		self.lname_lbn = Label(self.frame_real, text = 'Last Name: ' + self.detail[2], font = ('arial', 10, 'bold')).grid(row =2, column = 0)
		self.nickname_lbn = Label(self.frame_real, text = 'Nickname: '+ self.detail[3], font = ('arial', 10, 'bold')).grid(row =3, column = 0)
		self.company_lbn = Label(self.frame_real, text = 'Company Name: '+ self.detail[4], font = ('arial', 10, 'bold')).grid(row =4, column = 0)
		self.title_lbn = Label(self.frame_real, text = 'Title: '+ self.detail[5], font = ('arial', 10, 'bold')).grid(row =5, column = 0)
		self.phone_lbn = Label(self.frame_real, text = 'Phone Number: '+ self.detail[6], font = ('arial', 10, 'bold')).grid(row =6, column = 0)
		self.email_lbn = Label(self.frame_real, text = 'Email: '+ self.detail[7], font = ('arial', 10, 'bold')).grid(row =7, column = 0)
		self.address_lbn = Label(self.frame_real, text = 'Resident Address: '+ self.detail[8], font = ('arial', 10, 'bold')).grid(row =8, column = 0)
		self.website_lbn = Label(self.frame_real, text = 'Website: '+ self.detail[9], font = ('arial', 10, 'bold')).grid(row =9, column = 0)
		self.relationship_lbn = Label(self.frame_real, text = 'Relationship: '+ self.detail[10], font = ('arial', 10, 'bold')).grid(row =10, column = 0)
		self.city_lbn = Label(self.frame_real, text = 'City: '+ self.detail[11], font = ('arial', 10, 'bold')).grid(row =11, column = 0)
		self.state_lbn = Label(self.frame_real, text = 'State: '+ self.detail[12], font = ('arial', 10, 'bold')).grid(row =12, column = 0)
		self.zip_lbn = Label(self.frame_real, text = 'Zip Code: '+ self.detail[13], font = ('arial', 10, 'bold')).grid(row =13, column = 0)

		self.frame_real.pack()

	def update(self):
		self.frame_real.destroy()
		self.frame_real = Frame(self.root)
		self.flbn = Label(self.frame_real, text = 'Update Contact', font = ('arial', 20, 'bold')).grid(columnspan = 7)

		self.fname_lbn = Label(self.frame_real, text = 'First Name', font = ('arial', 10, 'bold')).grid(row =1, column = 0)
		self.lname_lbn = Label(self.frame_real, text = 'Last Name', font = ('arial', 10, 'bold')).grid(row =2, column = 0)
		self.nickname_lbn = Label(self.frame_real, text = 'Nickname', font = ('arial', 10, 'bold')).grid(row =3, column = 0)
		self.company_lbn = Label(self.frame_real, text = 'Company Name', font = ('arial', 10, 'bold')).grid(row =4, column = 0)
		self.title_lbn = Label(self.frame_real, text = 'Title', font = ('arial', 10, 'bold')).grid(row =5, column = 0)
		self.phone_lbn = Label(self.frame_real, text = 'Phone Number', font = ('arial', 10, 'bold')).grid(row =6, column = 0)
		self.email_lbn = Label(self.frame_real, text = 'Email', font = ('arial', 10, 'bold')).grid(row =7, column = 0)
		self.address_lbn = Label(self.frame_real, text = 'Resident Address', font = ('arial', 10, 'bold')).grid(row =8, column = 0)
		self.website_lbn = Label(self.frame_real, text = 'Website', font = ('arial', 10, 'bold')).grid(row =9, column = 0)
		self.relationship_lbn = Label(self.frame_real, text = 'Relationship', font = ('arial', 10, 'bold')).grid(row =10, column = 0)
		self.city_lbn = Label(self.frame_real, text = 'City', font = ('arial', 10, 'bold')).grid(row =11, column = 0)
		self.state_lbn = Label(self.frame_real, text = 'State', font = ('arial', 10, 'bold')).grid(row =12, column = 0)
		self.zip_lbn = Label(self.frame_real, text = 'Zip Code', font = ('arial', 10, 'bold')).grid(row =13, column = 0)

		
		
		

		
		
		nickname_en = StringVar()
		company_en = StringVar()
		title_en = StringVar()
		phone_en	=StringVar()
		email_en = StringVar()
		address_en = StringVar()
		website_en= StringVar()
		relationship_en = StringVar()
		city_en = StringVar()
		state_en = StringVar()
		Zip_en = StringVar()
		lname_en = StringVar()

		fname_en = StringVar()
		fname_entry = Entry(self.frame_real, textvariable = fname_en)
		fname_entry.grid(row = 1, column = 3)
		self.lname_en = StringVar()
		self.lname_entry = Entry(self.frame_real, textvariable = lname_en)
		self.lname_entry.grid(row = 2, column = 3)

		self.nickname_entry = Entry(self.frame_real, textvariable = nickname_en)
		self.nickname_entry.grid(row = 3, column = 3)

		self.company_entry = Entry(self.frame_real, textvariable = company_en)
		self.company_entry.grid(row = 4, column = 3)

		self.title_entry = Entry(self.frame_real, textvariable = title_en)
		self.title_entry.grid(row = 5, column = 3)

		self.phone_entry = Entry(self.frame_real, textvariable = phone_en)
		self.phone_entry.grid(row = 6, column = 3)

		self.email_entry = Entry(self.frame_real, textvariable = email_en)
		self.email_entry.grid(row = 7, column = 3)

		self.address_entry = Entry(self.frame_real, textvariable = address_en)
		self.address_entry.grid(row = 8, column = 3)

		self.website_entry = Entry(self.frame_real, textvariable = website_en)
		self.website_entry.grid(row = 9, column = 3)

		self.relationship_entry = Entry(self.frame_real, textvariable = relationship_en)
		self.relationship_entry.grid(row = 10, column = 3)

		self.city_entry = Entry(self.frame_real, textvariable = city_en)
		self.city_entry.grid(row = 11, column = 3)

		self.state_entry = Entry(self.frame_real, textvariable = state_en)
		self.state_entry.grid(row = 12, column = 3)

		self.zip_entry = Entry(self.frame_real, textvariable = Zip_en)
		self.zip_entry.grid(row = 13, column = 3)

		fname_en.set(self.detail[1])
		lname_en.set(self.detail[2])
		nickname_en.set(self.detail[3])
		company_en.set(self.detail[4])
		title_en.set(self.detail[5])
		phone_en.set(self.detail[6])
		email_en.set(self.detail[7])
		address_en.set(self.detail[8])
		website_en.set(self.detail[9])
		relationship_en.set(self.detail[10])
		city_en.set(self.detail[11])
		state_en.set(self.detail[12])
		Zip_en.set(self.detail[13])

		self.submit_now = Button(self.frame_real, text='Update Now' , bg = '#7a3d46', fg = 'white', command	 = self.updatefunction).grid(row = 14, column = 3)
		self.frame_real.pack()
	def updatefunction(self):
		mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'contactbook_db')
		mycursor = mydb.cursor()

		firstname = fname_en.get()
		lname = lname_en.get()
		nickname = self.nickname_entry.get()
		company = self.company_entry.get()
		city = self.city_entry.get()
		state = self.state_entry.get()
		Zip = self.zip_entry.get()
		relationship  = self.relationship_entry.get()
		email = self.email_entry.get()
		realphone  = self.phone_entry.get()
		title = self.title_entry.get()
		address = self.address_entry.get()
		website = self.website_entry.get()

		query  = "UPDATE contact_tb SET First_name = %s , Last_name= %s , Nickname= %s , Company= %s , Title= %s , Phone= %s , Email= %s , Address= %s , Website= %s , Relationship= %s , City= %s  ,State= %s , Zip_code= %s WHERE First_name=%s and Phone=%s"
		values = (firstname, lname, nickname, company, title, realphone, email, address, website, relationship, city, state, Zip, self.nm, self.ph)
		mycursor.execute(query, values)
		mydb.commit()

		if mycursor.rowcount ==1:
				showinfo('Message', 'Update Succesfully!')
		else:
			showinfo('Message', 'Update failed')







    	
    	



		
		self.frame_real.pack()
	def dasboardfunc(self):
		pass














	# def display_btn(self):
	# 	self.frame_real.destroy()
	# 	self.frame_real = Frame(self.root)
	# 	self.flbn = Label(self.frame_real, text = 'Profile Information', font = ('arial', 10, 'bold')).grid(columnspan = 7)

	# 	self.fname = IntVar()
	# 	self.lname = IntVar()
	# 	self.nickname = IntVar()
	# 	self.company = IntVar()
	# 	self.title = IntVar()
	# 	self.phone	=IntVar()
	# 	self.email = IntVar()
	# 	self.address = IntVar()
	# 	self.website= IntVar()
	# 	self.relationship = IntVar()
	# 	self.city = IntVar()
	# 	self.state = IntVar()
	# 	self.zip = IntVar()

		

	# 	self.fname_lbn = Checkbutton(self.frame_real, text = 'First Name', variable = self.fname, font = ('arial', 10, 'bold'), onvalue =1, 
	# 		offvalue = 0, command = lambda:self.checkButton('fname')).grid(row =1, column = 0)
	# 	self.lname_lbn = Checkbutton(self.frame_real, text = 'Last Name',variable = self.lname,  font = ('arial', 10, 'bold'),
	# 		command = lambda:self.checkButton('lname')).grid(row =2, column = 0)
	# 	self.nickname_lbn =Checkbutton(self.frame_real, text = 'Nickname', variable = self.nickname, font = ('arial', 10, 'bold'),
	# 		command = lambda:self.checkButton('nickname')).grid(row =3, column = 0)
	# 	self.company_lbn = Checkbutton(self.frame_real, text = 'Company Name',variable = self.company, font = ('arial', 10, 'bold'),
	# 		command = lambda:self.checkButton('company')).grid(row =4, column = 0)
	# 	self.title_lbn = Checkbutton(self.frame_real, text = 'Title', variable = self.title, font = ('arial', 10, 'bold'),
	# 		command = lambda:self.checkButton('title')).grid(row =5, column = 0)
	# 	self.phone_lbn = Checkbutton(self.frame_real, text = 'Phone Number', variable = self.phone, font = ('arial', 10, 'bold'),
	# 		command = lambda:self.checkButton('phone')).grid(row =6, column = 0)
	# 	self.email_lbn = Checkbutton(self.frame_real, text = 'Email', variable = self.email, font = ('arial', 10, 'bold'),
	# 		command = lambda:self.checkButton('email')).grid(row =7, column = 0)
	# 	self.address_lbn = Checkbutton(self.frame_real, text = 'Resident Address', variable = self.address, font = ('arial', 10, 'bold'),
	# 		command = lambda:self.checkButton('address')).grid(row =8, column = 0)
	# 	self.website_lbn = Checkbutton(self.frame_real, text = 'Website', variable = self.website, font = ('arial', 10, 'bold'),
	# 		command = lambda:self.checkButton('website')).grid(row =9, column = 0)
	# 	self.relationship_lbn = Checkbutton(self.frame_real, text = 'Relationship', variable = self.relationship, font = ('arial', 10, 'bold'),
	# 		command = lambda:self.checkButton('relationship')).grid(row =10, column = 0)
	# 	self.city_lbn = Checkbutton(self.frame_real, text = 'City',variable = self.city, font = ('arial', 10, 'bold'),
	# 		command = lambda:self.checkButton('city')).grid(row =11, column = 0)
	# 	self.state_lbn = Checkbutton(self.frame_real, text = 'State',variable = self.state, font = ('arial', 10, 'bold'),
	# 		command = lambda:self.checkButton('state')).grid(row =12, column = 0)
	# 	self.zip_lbn = Checkbutton(self.frame_real, text = 'Zip Code',variable = self.zip,  font = ('arial', 10, 'bold'),
	# 		command = lambda:self.checkButton('zip')).grid(row =13, column = 0)

	# 	self.submit_now = Button(self.frame_real, text='Create Now' , bg = '#7a3d46', fg = 'white').grid(row = 14, column = 3)
	# 	self.frame_real.pack()

	# 	self.fname_entry = Entry(self.frame_real, state = DISABLED, textvariable = self.fname_en)
	# 	self.fname_entry.grid(row = 1, column = 3)

	# 	self.lname_entry = Entry(self.frame_real, state = DISABLED, textvariable = self.lname_en)
	# 	self.lname_entry.grid(row = 2, column = 3)

	# 	self.nickname_entry = Entry(self.frame_real, state = DISABLED, textvariable = self.nickname_en)
	# 	self.nickname_entry.grid(row = 3, column = 3)

	# 	self.company_entry = Entry(self.frame_real, state = DISABLED, textvariable = self.company_en)
	# 	self.company_entry.grid(row = 4, column = 3)

	# 	self.title_entry = Entry(self.frame_real, state = DISABLED, textvariable = self.title_en)
	# 	self.title_entry.grid(row = 5, column = 3)

	# 	self.phone_entry = Entry(self.frame_real, state = DISABLED, textvariable = self.phone_en)
	# 	self.phone_entry.grid(row = 6, column = 3)

	# 	self.email_entry = Entry(self.frame_real, state = DISABLED, textvariable = self.email_en)
	# 	self.email_entry.grid(row = 7, column = 3)

	# 	self.address_entry = Entry(self.frame_real, state = DISABLED, textvariable = self.address_en)
	# 	self.address_entry.grid(row = 8, column = 3)

	# 	self.website_entry = Entry(self.frame_real, state = DISABLED , textvariable = self.website_en)
	# 	self.website_entry.grid(row = 9, column = 3)

	# 	self.relationship_entry = Entry(self.frame_real, state = DISABLED, textvariable = self.relationship_en)
	# 	self.relationship_entry.grid(row = 10, column = 3)

	# 	self.city_entry = Entry(self.frame_real, state = DISABLED, textvariable = self.city_en)
	# 	self.city_entry.grid(row = 11, column = 3)

	# 	self.state_entry = Entry(self.frame_real, state = DISABLED, textvariable = self.state_en)
	# 	self.state_entry.grid(row = 12, column = 3)

	# 	self.zip_entry = Entry(self.frame_real, state = DISABLED, textvariable = self.zip_en)
	# 	self.zip_entry.grid(row = 13, column = 3)

	# 	self.submit_now = Button(self.frame_real, text='Create Now' , bg = '#7a3d46', fg = 'white').grid(row = 14, column = 3)
	# 	self.frame_real.pack()

	# def checkButton(self, event):
	# 	if event == 'fname':
	# 		if self.fname.get()== 1:
	# 			self.fname_entry.config(state = NORMAL)
	# 			self.fname_entry.focus()
	# 			self.fname_entry.delete('0', END)
	# 			self.fname_en.set('')
	# 		elif self.fname.get()==0:
	# 			self.fname_entry.config(state = DISABLED)
	# 			self.fname_en.set('0')
	# 	if event == 'lname':
	# 		if self.lname.get()== 1:
	# 			self.lname_entry.config(state = NORMAL)
	# 			self.lname_entry.focus()
	# 			self.lname_entry.delete('0', END)
	# 			self.lname_en.set('')
	# 		elif self.lname.get()==0:
	# 			self.lname_entry.config(state = DISABLED)
	# 			self.lname_en.set('0')

	# 	if event == 'nickname':
	# 		if self.nickname.get()== 1:
	# 			self.nickname_entry.config(state = NORMAL)
	# 			self.nickname_entry.focus()
	# 			self.nickname_entry.delete('0', END)
	# 			self.nickname_en.set('')
	# 		elif self.nickname.get()==0:
	# 			self.nickname_entry.config(state = DISABLED)
	# 			self.nickname_en.set('0')
	# 	if event == 'company':
	# 		if self.company.get()== 1:
	# 			self.company_entry.config(state = NORMAL)
	# 			self.company_entry.focus()
	# 			self.company_entry.delete('0', END)
	# 			self.company_en.set('')
	# 		elif self.company.get()==0:
	# 			self.company_entry.config(state = DISABLED)
	# 			self.company_en.set('0')
	# 	if event == 'title':
	# 		if self.title.get()== 1:
	# 			self.title_entry.config(state = NORMAL)
	# 			self.title_entry.focus()
	# 			self.title_entry.delete('0', END)
	# 			self.title_en.set('')
	# 		elif self.title.get()==0:
	# 			self.title_entry.config(state = DISABLED)
	# 			self.title_en.set('0')
	# 	if event == 'email':
	# 		if self.email.get()== 1:
	# 			self.email_entry.config(state = NORMAL)
	# 			self.email_entry.focus()
	# 			self.email_entry.delete('0', END)
	# 			self.email_en.set('')
	# 		elif self.email.get()==0:
	# 			self.email_entry.config(state = DISABLED)
	# 			self.email_en.set('0')
	# 	if event == 'address':
	# 		if self.address.get()== 1:
	# 			self.address_entry.config(state = NORMAL)
	# 			self.address_entry.focus()
	# 			self.address_entry.delete('0', END)
	# 			self.address_en.set('')
	# 		elif self.address.get()==0:
	# 			self.address_entry.config(state = DISABLED)
	# 			self.address_en.set('0')
	# 	if event == 'website':
	# 		if self.website.get()== 1:
	# 			self.website_entry.config(state = NORMAL)
	# 			self.website_entry.focus()
	# 			self.website_entry.delete('0', END)
	# 			self.website_en.set('')
	# 		elif self.website.get()==0:
	# 			self.website_entry.config(state = DISABLED)
	# 			self.website_en.set('0')

	# 	if event == 'website':
	# 		if self.website.get()== 1:
	# 			self.website_entry.config(state = NORMAL)
	# 			self.website_entry.focus()
	# 			self.website_entry.delete('0', END)
	# 			self.website_en.set('')
	# 		elif self.website.get()==0:
	# 			self.website_entry.config(state = DISABLED)
	# 			self.website_en.set('0')

	# 	if event == 'relationship':
	# 		if self.relationship.get()== 1:
	# 			self.relationship_entry.config(state = NORMAL)
	# 			self.relationship_entry.focus()
	# 			self.relationship_entry.delete('0', END)
	# 			self.relationship_en.set('')
	# 		elif self.relationship.get()==0:
	# 			self.relationship_entry.config(state = DISABLED)
	# 			self.relationship_en.set('0')

	# 	if event == 'city':
	# 		if self.city.get()== 1:
	# 			self.city_entry.config(state = NORMAL)
	# 			self.city_entry.focus()
	# 			self.city_entry.delete('0', END)
	# 			self.city_en.set('')
	# 		elif self.city.get()==0:
	# 			self.city_entry.config(state = DISABLED)
	# 			self.city_en.set('0')
	# 	if event == 'state':
	# 		if self.state.get()== 1:
	# 			self.state_entry.config(state = NORMAL)
	# 			self.state_entry.focus()
	# 			self.state_entry.delete('0', END)
	# 			self.state_en.set('')
	# 		elif self.state.get()==0:
	# 			self.state_entry.config(state = DISABLED)
	# 			self.state_en.set('0')
	# 	if event == 'zip':
	# 		if self.zip.get()== 1:
	# 			self.zip_entry.config(state = NORMAL)
	# 			self.zip_entry.focus()
	# 			self.zip_entry.delete('0', END)
	# 			self.zip_en.set('')
	# 		elif self.zip.get()==0:
	# 			self.zip_entry.config(state = DISABLED)
	# 			self.zip_en.set('0')















		    	
    	
    	
    	 

        
		
		
		
        
        
        






		

contact = Contactbook()

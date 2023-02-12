from tkinter import *
from tkinter.messagebox import *
import random
import sys
import mysql.connector
#OLAOLUWA BANKING APP PROJECT DONE

class Banking:
    def __init__(self):
        self.root = Tk()
        self.root.title('Mobile Banking')
        self.root.geometry('800x800')
        self.root.config(bg = 'pink')
        self.frameb = Frame(self.root, width = 700, height= 700  )
        self.mainPage()
        self.account_number = ""
        self.epinreal = ""
       
        self.root.mainloop()

    def mainPage(self):
        self.frameb.destroy()
        self.frameb = Frame(self.root)
        self.mplbn = Label(self.frameb, font = ('Times New Roman', 20, 'bold'), fg = 'black', bd = 10, text = 'WELCOME TO OVB BANKING')
        self.mplbn.grid( columnspan= 5)  
        self.rgr = Button(self.frameb, font = ('arial', 12, 'bold'), bg = 'pink', fg = 'black', bd= 10, text = 'Registration', command=self.regPage)
        self.rgr.grid(row =2 , column = 1)
        self.lgn = Button(self.frameb, font = ('arial', 12, 'bold'), bg = 'pink', fg = 'black', bd = 5, text = 'Login', command = self.loginPage)
        self.lgn.grid(row = 3, column= 1)
        self.abt = Button(self.frameb, font = ('arial', 12, 'bold'), bg = 'pink', fg = 'black', bd = 5, text = 'About Us', command = self.aboutPage)
        self.abt.grid(row = 2, column= 3)
        self.dev = Button(self.frameb, font = ('arial', 12, 'bold'), bg = 'pink', fg = 'black', bd = 5, text = 'Developer', command = self.developerPage)
        self.dev.grid(row = 3, column= 3)
        self.exit = Button(self.frameb, font = ('arial', 8, 'bold'), bg = 'pink', fg = 'black', bd = 5, text = 'Exit', command= self.exitPage)
        self.exit.grid(row = 6, column= 4) 

        self.frameb.pack()

#****************************************************************************FOR REGISTRATION PAGE ANDF FUNCTION********************************************************
    def regPage(self):
        self.frameb.destroy()
        self.frameb = Frame(self.root)

        self.reglbn1 = Label(self.frameb, font = ('arial', 20, 'bold'),  fg = 'black', bd = 10,  text = 'Please Kindly Create Your Account With Us')
        self.reglbn1.grid(columnspan = 5)

        self.regtitle = Label(self.frameb, font = ('arial', 10, 'bold'), fg = 'black', bd = 10, text = 'Title').grid(row =1 , column = 0)
        self.regfname = Label(self.frameb, font = ('arial', 10, 'bold'), fg = 'black', bd = 10, text = 'First Name').grid(row =2 , column = 0)
        self.regname = Label(self.frameb, font = ('arial', 10, 'bold'), fg = 'black', bd = 10, text = 'Others Name').grid(row =2 , column = 3)
        self.gen = Label(self.frameb, font = ('arial', 10, 'bold'), fg = 'black', bd = 10, text = 'Gender').grid(row =3 , column = 0)
        self.Marstatus = Label(self.frameb, font = ('arial', 10, 'bold'), fg = 'black', bd = 10, text = 'Marital Status').grid(row =4 , column = 0)
        self.Marstatus_entry = StringVar()
        #for marital status
        self.married = Radiobutton(self.frameb, text = 'Married', variable = self.Marstatus_entry, value = 'Married').grid(row =4 , column = 1)
        self.single = Radiobutton(self.frameb, text = 'Single', variable =self.Marstatus_entry, value = 'Single').grid(row =4 , column = 2)
        self.divorce = Radiobutton(self.frameb, text = 'Divorce', variable =self.Marstatus_entry, value = 'Divorce').grid(row =4 , column = 3)
        
        self.country = Label(self.frameb, font = ('arial', 10, 'bold'), fg = 'black', bd = 10, text = 'Country').grid(row =5 , column = 0)
        self.mmn = Label(self.frameb, font = ('arial', 10, 'bold'), fg = 'black', bd = 10, text = "Mother's Maiden Name").grid(row =6 , column = 0)
        self.edulv = Label(self.frameb, font = ('arial', 10, 'bold'), fg = 'black', bd = 10, text = "Education Level").grid(row =7 , column = 0)

        self.edu_entry = StringVar()

        #education level check button
        self.under = Radiobutton(self.frameb, text = 'Undergraduate', value = 'Undergraduate', variable = self.edu_entry).grid(row = 7, column = 1)
        self.gra = Radiobutton(self.frameb, text = 'Graduate', value ='Graduate', variable = self.edu_entry).grid(row = 7, column = 2)
        self.post = Radiobutton(self.frameb, text = 'Postgraduate', value = 'Postgraduate', variable = self.edu_entry).grid(row = 7, column = 3)

        self.lga = Label(self.frameb, font = ('arial', 10, 'bold'),  fg = 'black', bd = 10, text = "Local Government Origin").grid(row =8 , column = 0)
        self.sto = Label(self.frameb, font = ('arial', 10, 'bold'),  fg = 'black', bd = 10, text = "State Of Origin").grid(row =9 , column = 0)
        self.regp = Label(self.frameb, font = ('arial', 10, 'bold'), fg = 'black', bd = 10, text = "Purpose of Account").grid(row =10 , column = 0)
        self.plotnum = Label(self.frameb, font = ('arial', 10, 'bold'), fg = 'black', bd = 10, text = 'Plot Number').grid(row =11 , column = 0)
        self.adr = Label(self.frameb, font = ('arial', 10, 'bold'), fg = 'black', bd = 10, text = 'Home Address').grid(row =12 , column = 0)
        self.phn = Label(self.frameb, font = ('arial', 10, 'bold'),  fg = 'black', bd = 10, text = 'Phone Number').grid(row =13 , column = 0)
        self.eml = Label(self.frameb, font = ('arial', 10, 'bold'),  fg = 'black', bd = 10, text = 'Email').grid(row =14 , column = 0)
        self.cty = Label(self.frameb, font = ('arial', 10, 'bold'),  fg = 'black', bd = 10, text = 'City/Town').grid(row =15 , column = 0)
        self.pin = Label(self.frameb, font = ('arial', 10, 'bold'),  fg = 'black', bd = 10, text = 'Four Digit PIN').grid(row =16 , column =0)

        #ENTRY FOR ALL THE REG DATA

        self.regtitle_entry = Entry(self.frameb, font =('arial', 8), bd= 5, insertwidth = 2, bg = 'white', justify = 'left')
        self.regtitle_entry.grid(row = 1, column = 2)
        self.regname_entry = Entry(self.frameb, font =('arial', 8), bd= 5, insertwidth = 2, bg = 'white', justify = 'left')
        self.regname_entry.grid(row = 2, column = 4)
        self.regfname_entry = Entry(self.frameb, font =('arial', 8), bd= 5, insertwidth = 2, bg = 'white', justify = 'left')
        self.regfname_entry.grid(row = 2, column = 2)
        self.gen_entry = Entry(self.frameb, font =('arial', 8), bd= 5, insertwidth = 2, bg = 'white', justify = 'left')
        self.gen_entry.grid(row = 3, column = 2)
        self.country_entry = Entry(self.frameb, font =('arial', 8), bd= 5, insertwidth = 2, bg = 'white', justify = 'left')
        self.country_entry.grid(row = 5, column = 2)
        self.mnn_entry = Entry(self.frameb, font =('arial', 8), bd= 5,  insertwidth = 2, bg = 'white', justify = 'left')
        self.mnn_entry.grid(row = 6, column = 2)
        self.lga_entry = Entry(self.frameb, font =('arial', 8), bd= 5,  insertwidth = 2, bg = 'white', justify = 'left')
        self.lga_entry.grid(row = 8, column = 2)
        self.sto_entry = Entry(self.frameb, font =('arial', 8), bd= 5,  insertwidth = 2, bg = 'white', justify = 'left')
        self.sto_entry.grid(row = 9, column = 2)
        self.regp_entry = Entry(self.frameb, font =('arial', 8), bd= 5,  insertwidth = 2, bg = 'white', justify = 'left')
        self.regp_entry .grid(row = 10, column = 2)
        self.plotnum_entry = Entry(self.frameb, font =('arial', 8), bd= 5,  insertwidth = 2, bg = 'white', justify = 'left')
        self.plotnum_entry.grid(row = 11, column = 2)
        self.adr_entry = Entry(self.frameb, font =('arial', 8), bd= 5, insertwidth = 2, bg = 'white', justify = 'left')
        self.adr_entry.grid(row = 12, column = 2)
        self.phn_entry = Entry(self.frameb, font =('arial', 8), bd= 5, insertwidth = 2, bg = 'white', justify = 'left')
        self.phn_entry.grid(row = 13, column = 2)
        self.eml_entry = Entry(self.frameb, font =('arial', 8), bd= 5,  insertwidth = 2, bg = 'white', justify = 'left')
        self.eml_entry.grid(row = 14, column = 2)
        self.cty_entry = Entry(self.frameb, font =('arial', 8), bd= 5, insertwidth = 2, bg = 'white', justify = 'left')
        self.cty_entry.grid(row = 15, column = 2)
        self.pin_entry = Entry(self.frameb, font =('arial', 8), bd= 5, insertwidth = 2, bg = 'white', justify = 'left')
        self.pin_entry.grid(row = 16, column = 2)

        self.regbtn = Button(self.frameb, font = ('arial', 15, 'bold'), bg = 'red', fg = 'white', bd= 10, text = 'Register', command = self.regDetail)
        self.regbtn.grid(row =17 , column = 2)
        #for mainpage and login button
        self.mainP = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'pink', fg = 'black', bd= 10, text = 'Home', command=self.mainPage)
        self.mainP.grid(row =18 , column = 0)
        self.lgn = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'pink', fg = 'black', bd = 5, text = 'Login', command = self.loginPage)
        self.lgn.grid(row = 18 , column= 1)
        self.frameb.pack()

        #FOR THE REG FUNCTION
    def regDetail(self):
        mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'bankingAPP_db' )
        mycursor = mydb.cursor()
        self.account_generated = random.randrange(1, 40000000000)
        self.regtitle = self.regtitle_entry.get()
        self.regname = self.regname_entry.get()
        self.regfname = self.regfname_entry.get()
        self.gender = self.gen_entry.get()
        self.country = self.country_entry.get()
        self.mother_name = self.mnn_entry.get()
        self.lga = self.lga_entry.get()
        self.statae_of_origin =self.sto_entry.get()
        self.account_purpose = self.regp_entry.get()
        self.plotnum = self.plotnum_entry.get()
        self.address = self.adr_entry.get()
        self.phone_no = self.phn_entry.get()
        self.email = self.eml_entry.get()
        self.city = self.cty_entry.get()
        self.epin = self.pin_entry.get()
        self.Marital_status = self.Marstatus_entry.get()
        self.education_status =self.edu_entry.get()


        myquery = ("INSERT INTO Users_detail(Title, Account_no, First_name, Other_name, Phone_no, E_PIN, Gender, Country, Mother_name, Local_Government, State_of_origin, Purpose_of_account, Address_plot_num, Address, Email, City, Marital_status, Education_status)  VALUES('%s',\
         '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(self.regtitle, self.account_generated, self.regfname,self.regname,self.phone_no, self.epin, self.gender,
            self.country, self.mother_name,self.lga, self.statae_of_origin,self.account_purpose , self.plotnum , self.address, self.email , self.city, self.Marital_status, self.education_status ))

        mycursor.execute(myquery)
        mydb.commit()
        if mycursor.rowcount ==1:
            showinfo('Message', 'Your account has been Registered Succesfullly')

        else:
            showinfo('Message', 'Your account Registration failed')

        query1 = "INSERT INTO transaction_detail (Account_no, E_PIN, phone_no) VALUES('%s','%s', '%s')" %(self.account_generated, self.epin, self.phone_no)
        mycursor.execute(query1)
        mydb.commit()
        mydb.close()

#****************************************************************************FOR LOGIN PAGE ANDF FUNCTION********************************************************
    def loginPage(self):
        self.frameb.destroy()
        self.frameb = Frame(self.root)
        self.loginlbn1 = Label(self.frameb, font = ('arial', 20, 'bold'),  fg = 'black', bd = 10,  text = 'Enter Your Info to login')
        self.loginlbn1.grid(columnspan  =5)
        self.accountlbn = Label(self.frameb, font = ('arial', 10, 'bold'), fg = 'black', bd = 10, text = 'Account No')
        self.accountlbn.grid(row= 3, column = 3)
        self.Epin = Label(self.frameb, font = ('arial', 10, 'bold'), fg = 'black', bd = 10, text = 'E-pin')
        self.Epin.grid(row= 4, column = 3)
        self.account_entry = Entry(self.frameb, font =('arial', 8), bd= 5,  insertwidth = 2, bg = 'white')
        self.account_entry.grid(row = 3, column = 4)
        self.epin_entry = Entry(self.frameb, font =('arial', 8), bd= 5,  insertwidth = 7, bg = 'white')
        self.epin_entry.grid(row = 4, column = 4)
        self.loginbtn = Button(self.frameb, font = ('arial', 15, 'bold'), bg = 'red', fg = 'white', bd= 10, text = 'Login', command = self.loginDetail )
        self.loginbtn.grid(row =5 , column = 4)
        self.forgetEpin = Button(self.frameb, font = ('arial', 7, 'bold'), bg = 'pink', fg = 'black', bd= 1, text = 'forget ePIN')
        self.forgetEpin.grid(row =6 , column =4 )
        self.mainP = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'pink', fg = 'black', bd= 10, text = 'Home', command=self.mainPage)
        self.mainP.grid(row =6 , column = 0)
        self.frameb.pack()

    def loginDetail(self):
    	account_no = self.account_entry.get()
    	ePIN  = self.epin_entry.get()

    	mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'bankingAPP_db' )
    	mycursor = mydb.cursor()

    	query = "SELECT Account_no, E_PIN FROM Users_detail WHERE Account_no = %s and E_PIN = %s"
    	values = (account_no, ePIN)
    	mycursor.execute(query, values)
    	mylogin = mycursor.fetchone()
    	self.account_number = mylogin[0]
    	self.epinreal = mylogin[1]
    	print(mylogin)

    	if mylogin !=None:
    		print('succesfully')
    		self.profilePage()

    	else:
    		showinfo('Message', 'You have entered invalid login detail')

    	query1 = "SELECT Account_balance FROM Users_detail WHERE Account_no =%s and E_PIN = %s"
    	values1= (account_no, ePIN)
    	mycursor.execute(query1, values1)
    	mybal = mycursor.fetchone()
    	x = mybal[0]

    	query3 = "UPDATE transaction_detail SET Account_balance =%s WHERE Account_no = %s"
    	values2= (x, account_no)
    	mycursor.execute(query3, values2)
    	mydb.commit()
    	mydb.close()
#****************************************************************************FOR EXIT PAGE ANDF FUNCTION********************************************************
    def exitPage(self):
        self.root.destroy()
#****************************************************************************FOR ABOUT US PAGE ANDF FUNCTION********************************************************
    def aboutPage(self):
        self.frameb.destroy()
        self.frameb = Frame(self.root)
        self.abt = Label(self.frameb, bg = 'red', fg= 'white', bd = 10, text = 'this is about us')
        self.abt.grid(columnspan = 4)
        self.mainP = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'pink', fg = 'black', bd= 10, text = 'Home', command=self.mainPage)
        self.mainP.grid(row =2 , column = 0)
        self.frameb.pack()

#****************************************************************************FOR DEVELOPER PAGE ANDF FUNCTION********************************************************
    def developerPage(self):
        self.frameb.destroy()
        self.frameb = Frame(self.root)
        self.dev = Label(self.frameb, bg = 'red', fg= 'white', bd = 10, text = 'this is about is about the developer')
        self.dev.grid(columnspan = 4)
        self.mainP = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'pink', fg = 'black', bd= 10, text = 'Home', command=self.mainPage)
        self.mainP.grid(row =2 , column = 0)
        self.frameb.pack()
#****************************************************************************FOR USERPAGE PAGE************************************************************************

    def profilePage(self):
        self.frameb.destroy()
        self.frameb = Frame(self.root)
        self.plbn = Label(self.frameb, fg= 'black', bd = 10, text = 'Hi! Welcome to your Account Profile \n Please Kindly Choose a Transaction to Perform')
        self.plbn.grid(columnspan = 9)
        self.depbtn = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'pink', fg = 'black', bd= 2, text = 'Deposit', command = self.deposit_page)
        self.depbtn.grid(row =2 , column = 0)
        self.balbtn = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'pink', fg = 'black', bd= 2, text = 'Balance', command = self.balanceChecker)
        self.balbtn.grid(row =3 , column = 0)
        self.airtimebtn = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'pink', fg = 'black', bd= 2, text = 'Recharge', command = self.airtimePage)
        self.airtimebtn.grid(row =4 , column = 0)
        self.pin_change = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'pink', fg = 'black', bd= 2, text = 'Change Pin', command = self.pinchPage)
        self.pin_change.grid(row =3 , column = 8)
        self.sendmoney = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'pink', fg = 'black', bd= 2, text = 'Send Money', command = self.sendmoneyPage)
        self.sendmoney.grid(row =2 , column = 8)
        self.quit = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'pink', fg = 'black', bd= 5, text = 'Exit', command = self.mainPage)
        self.quit.grid(row =4 , column = 8)
        self.frameb.pack()

#****************************************************************************FOR DEPOSIT PAGE ANDF FUNCTION********************************************************
    def deposit_page(self):
        self.frameb.destroy()
        self.frameb = Frame(self.root)
        self.depositlbn = Label(self.frameb, font = ('arial', 12, 'bold'), fg = 'black', bd = 10, text = 'Please Kindly Deposit Your Fund Below')
        self.depositlbn.grid(columnspan = 5)
        self.account_dbtn = Label(self.frameb, font = ('arial', 8, 'bold'), fg = 'black', text = 'Acount No')
        self.account_dbtn.grid(row =2 , column = 1)
        self.amount_dbtn = Label(self.frameb, font = ('arial', 8, 'bold'), fg = 'black', text = 'Amount')
        self.amount_dbtn.grid(row =3 , column = 1)
        self.e_pin = Label(self.frameb, font = ('arial', 8, 'bold'), bg = 'White', fg = 'black', text = 'E-PIN')
        self.e_pin.grid(row =4 , column = 1)
        self.account_no_entry = Entry(self.frameb, font =('arial', 12, 'bold'), bd= 5,  insertwidth = 2, bg = 'white', justify = 'right')
        self.account_no_entry.grid(row = 2, column = 3)
        self.amount_entry = Entry(self.frameb, font =('arial', 12, 'bold'), bd= 5, insertwidth = 2, bg = 'white', justify = 'right')
        self.amount_entry.grid(row = 3, column = 3)
        self.epin_entry = Entry(self.frameb, font =('arial', 12, 'bold'), bd= 5,  insertwidth = 2, bg = 'white', justify = 'right')
        self.epin_entry.grid(row = 4, column = 3)
        self.depositbtn = Button(self.frameb, font = ('arial', 15, 'bold'), bg = 'red', fg = 'white', bd= 10, text = 'Deposit', command =self.depositDetail)
        self.depositbtn.grid(row =5 , column = 3)
        self.PP = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'pink', fg = 'black', bd= 10, text = 'Profile', command=self.profilePage)
        self.PP.grid(row =6 , column = 0)
        self.frameb.pack()

    def depositDetail(self):
    	Account_num = self.account_no_entry.get()
    	Amount = self.amount_entry.get()
    	ePIN = self.epin_entry.get()

    	mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'bankingAPP_db' )
    	mycursor = mydb.cursor()

    	query = "SELECT Account_balance FROM Users_detail WHERE Account_no = %s and E_PIN = %s"
    	values = (Account_num, ePIN)
    	mycursor.execute(query, values)
    	mydep = mycursor.fetchone()
    	print(mydep[0])

    	if mydep !=	None:
    		newbalance = (int(mydep[0]) + int(Amount))
    		query1 = 'UPDATE Users_detail SET Account_balance = %s WHERE account_no = %s'
    		values = (newbalance, Account_num)
    		mycursor.execute(query1, values)
    		mydb.commit()		

    		query3 = ("UPDATE transaction_detail SET Account_balance= %s WHERE Account_no = %s")
    		values2 = (newbalance, Account_num)
    		mycursor.execute(query3, values2)
    		mydb.commit()
    		showinfo('Message', 'Your money has been deposited')

    	else:
    		showinfo('Message','Invalid detail')
    	mydb.close()

#****************************************************************************FOR BUY AIRTIME PAGE ANDF FUNCTION********************************************************

    def airtimePage(self):
        self.frameb.destroy()
        self.frameb = Frame(self.root)

        self.airlbn = Label(self.frameb, font = ('arial', 12, 'bold'), fg = 'black', text = 'Please Fill in the Info to Perform Transaction')
        self.airlbn.grid(columnspan = 5)
        self.amount_btn = Label(self.frameb, font = ('arial', 10, 'bold'),  fg = 'black', text = 'Amount').grid(row =1 , column = 1)
        self.phnbtn = Label(self.frameb, font = ('arial', 10, 'bold'),  fg = 'black', text = 'Beneficiary Phone number').grid(row =2 , column = 1)
        self.e_pin = Label(self.frameb, font = ('arial', 10, 'bold'),  fg = 'black', text = 'E-PIN').grid(row =3 , column = 1)

        self.amount_entry = Entry(self.frameb, font =('arial', 10, 'bold'), bd= 5, insertwidth = 2, bg = 'white', justify = 'right')
        self.amount_entry.grid(row = 1, column = 3)
        self.phn_entry = Entry(self.frameb, font =('arial', 10, 'bold'), bd= 5, insertwidth = 2, bg = 'white', justify = 'right')
        self.phn_entry.grid(row = 2, column = 3)
        self.epin_entry = Entry(self.frameb, font =('arial', 10, 'bold'), bd= 5, insertwidth = 2,bg = 'white', justify = 'right')
        self.epin_entry.grid(row = 3, column = 3)

        self.buybtn = Button(self.frameb, font = ('arial', 15, 'bold'), bg = 'red', fg = 'white', bd= 10, text = 'Buy Now', command= self.airtimeDetail)
        self.buybtn.grid(row =4 , column = 3)

        self.PP = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'pink', fg = 'black', bd= 10, text = 'Profile', command=self.profilePage)
        self.PP.grid(row =5 , column = 0)

        self.frameb.pack()

    def airtimeDetail(self):
    	mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'bankingAPP_db' )
    	mycursor = mydb.cursor()

    	query = "SELECT Account_balance FROM Users_detail WHERE Account_no = %s and E_PIN= %s"
    	values = (self.account_number, self.epin_entry.get())
    	mycursor.execute(query, values)
    	mybal = mycursor.fetchone()
    	loaderbalance = mybal[0]
    	print(mybal[0])

    	if mybal[0] > int(self.amount_entry.get()) and mybal !=None:
    		newbalance = loaderbalance - int(self.amount_entry.get())

    		query = "UPDATE Users_detail SET Account_balance = %s WHERE Account_no = %s"
    		values = (newbalance, self.account_number)
    		mycursor.execute(query, values)
    		mydb.commit()

    		query1 = "UPDATE transaction_detail SET Account_balance = %s WHERE Account_no = %s"
    		values1 = (newbalance, self.account_number)
    		mycursor.execute(query1, values1)
    		mydb.commit()
    		showinfo('Message', 'Dear customer, Your transaction has been successfully')

    	else:
    		showinfo('Message', 'Dear customer, Invalid Detail')

    	mydb.close()
#****************************************************************************FOR CHAGING PIN PAGE ANDF FUNCTION********************************************************
    def pinchPage(self):
        self.frameb.destroy()
        self.frameb = Frame(self.root)
        self.pinlbn = Label(self.frameb, font = ('arial', 12, 'bold'), fg = 'black', text = 'DEAR CUSTOMER, KINDLY CHANGE YOUR PIN:')
        self.pinlbn.grid(columnspan = 5)
        self.old_pinlbn = Label(self.frameb, font = ('arial', 10, 'bold'),  fg = 'black', text = 'Old e-PIN').grid(row =1 , column = 1)
        self.new_pinlbn = Label(self.frameb, font = ('arial', 10, 'bold'),  fg = 'black', text = 'New e-PIN').grid(row =2 , column = 1)
        self.oldpin_entry = Entry(self.frameb, font =('arial', 10, 'bold'), bd= 5, insertwidth = 2, bg = 'white', justify = 'right')
        self.oldpin_entry.grid(row = 1, column = 3)
        self.newpin_entry = Entry(self.frameb, font =('arial', 10, 'bold'), bd= 5, insertwidth = 2, bg = 'white', justify = 'right')
        self.newpin_entry.grid(row = 2, column = 3)
        self.pinbtn = Button(self.frameb, font = ('arial', 15, 'bold'), bg = 'red', fg = 'white', bd= 10, text = 'Change PIN', command= self.pinDetail)
        self.pinbtn.grid(row =3 , column = 3)
        self.PP = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'pink', fg = 'black', bd= 10, text = 'Profile', command=self.profilePage)
        self.PP.grid(row =4 , column = 0)

        self.frameb.pack()
    def pinDetail(self):
    	oldpin  = self.oldpin_entry.get()
    	mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'bankingAPP_db' )
    	mycursor = mydb.cursor()
    	query = "SELECT E_PIN FROM Users_detail WHERE Account_no = %s and E_PIN = %s"
    	values = (self.account_number, self.epinreal)
    	mycursor.execute(query, values)
    	pin = mycursor.fetchone()
    	print(pin)

    	if str(pin[0]) == self.oldpin_entry.get():
    		query = "UPDATE Users_detail SET E_PIN = %s WHERE Account_no = %s"
    		values = (self.newpin_entry.get(), self.account_number)
    		mycursor.execute(query, values)
    		mydb.commit()

    		query1 = "UPDATE transaction_detail SET E_PIN = %s WHERE Account_no = %s"
    		values1 = (self.newpin_entry.get(), self.account_number)
    		mycursor.execute(query1, values1)
    		mydb.commit()
    		showinfo('Message', 'Dear customer, Your PIN has been Changed succesfully')

    	else:
    		showinfo('Alert!', 'Invalid pin')

#****************************************************************************FOR CHAGING PIN PAGE ANDF FUNCTION********************************************************
    def sendmoneyPage(self):
        self.frameb.destroy()
        self.frameb = Frame(self.root)

        self.sendmoneylbn = Label(self.frameb, font = ('arial', 12, 'bold'), fg = 'black', text = 'KINDLY ENTER BENEFICIARY DETAIL')
        self.sendmoneylbn.grid(columnspan = 7)

        self.befAcct = Label(self.frameb, font = ('arial', 8, 'bold'), fg = 'black', text = 'Account No')
        self.befAcct.grid(row =1 , column = 1)

        self.befamount = Label(self.frameb, font = ('arial', 8, 'bold'),  fg = 'white', text = 'Amount')
        self.befamount.grid(row =2 , column = 1)

        self.e_pin = Label(self.frameb, font = ('arial', 12, 'bold'), bg = 'White', fg = 'black', text = 'Enter PIN')
        self.e_pin.grid(row =3 , column = 1)

        self.acctno_entry = Entry(self.frameb, font =('arial', 10, 'bold'), bd= 5, insertwidth = 2, bg = 'white', justify = 'right')
        self.acctno_entry.grid(row = 1, column = 3)

        self.befmount_entry = Entry(self.frameb, font =('arial', 10, 'bold'), bd= 5, insertwidth = 2, bg = 'white', justify = 'right')
        self.befmount_entry.grid(row = 2, column = 3)

        self.epin_entry = Entry(self.frameb, font =('arial', 10, 'bold'), bd= 5, insertwidth = 2, bg = 'white', justify = 'right')
        self.epin_entry.grid(row = 3, column = 3)

        self.sendmoneybtn = Button(self.frameb, font = ('arial', 15, 'bold'), bg = 'red', fg = 'white', bd= 10, text = 'Send Money', command =self.sendmoneyDetail)
        self.sendmoneybtn.grid(row =4 , column = 3)

        self.PP = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'pink', fg = 'black', bd= 10, text = 'Profile', command=self.profilePage)
        self.PP.grid(row =5 , column = 0)

        self.frameb.pack()

    def sendmoneyDetail(self):
    	self.account_to_receive = self.acctno_entry.get()
    	self.amt_to_send = self.befmount_entry.get()
    	self.epin1 =self.epin_entry.get()
    	mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'bankingAPP_db' )
    	mycursor = mydb.cursor()

    	query = "SELECT Account_balance FROM Users_detail WHERE Account_no = %s and E_PIN= %s"
    	values = (self.account_number, self.epin1)
    	mycursor.execute(query, values)
    	mybal = mycursor.fetchone()
    	senderbalance = mybal[0]
    	print(mybal[0])

    	query1 = "SELECT Account_balance FROM Users_detail WHERE Account_no = "+(self.account_to_receive)
    	mycursor.execute(query1)
    	bal = mycursor.fetchone()
    	receiverbalance = bal[0]
    	print(bal[0])

    	if int(senderbalance) > int(self.amt_to_send) and mybal !=None:
    		newbalance_debit = senderbalance - int(self.amt_to_send)
    		newbalance_credit = receiverbalance + int(self.amt_to_send)

    		query = "UPDATE Users_detail SET Account_balance = %s WHERE Account_no = %s"
    		values = (newbalance_debit, self.account_number)
    		mycursor.execute(query, values)
    		mydb.commit()

    		query1 = "UPDATE transaction_detail SET Account_balance = %s WHERE Account_no = %s"
    		values1 = (newbalance_debit, self.account_number)
    		mycursor.execute(query1, values1)
    		mydb.commit()

    		#to update the receiver
    		query2 = "UPDATE Users_detail SET Account_balance = %s WHERE Account_no = %s"
    		values2 = (newbalance_credit, self.account_to_receive)
    		mycursor.execute(query2, values2)
    		mydb.commit()

    		query3 = "UPDATE transaction_detail SET Account_balance = %s WHERE Account_no = %s"
    		values3 = (newbalance_credit, self.account_to_receive)
    		mycursor.execute(query3, values3)
    		mydb.commit()
    		showinfo('Message', 'Dear customer, Your Fund has been tranferred successfully')

    	else:
    		showinfo('Message', 'Invalid Detail')
    	mydb.close()

#****************************************************************************FOR BALANCE CHECKER FUNCTION********************************************************
    def balanceChecker(self):
    	mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'bankingAPP_db' )
    	mycursor = mydb.cursor()
    	query = "SELECT Account_balance FROM Users_detail WHERE Account_no = "+str(self.account_number)
    	mycursor.execute(query)
    	mybal = mycursor.fetchone()
    	print(mybal)
    	showinfo('Account Balance', 'Dear customer, your account balance is N'+ str(mybal[0]))	
    	mydb.close()


    


    

    

    


    


    


    	






       
    	

    	
    	
    	
    	
    	

    	
    		

    	
    		





    	
        

Bk = Banking()


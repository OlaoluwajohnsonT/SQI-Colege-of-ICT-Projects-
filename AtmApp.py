from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import random
import sys
import mysql.connector
from playsound import playsound



class AtmApp:
    def __init__(self):
        self.root = Tk()
        self.root.title('Mobile Banking')
        self.root.geometry('500x400')
        self.root.config(bg = 'black')
        self.frameb = Frame(self.root, width = 500, height= 400)
        self.account_number = ""
        self.epinreal = ""
        self.amount_deposit = StringVar()
        self.amount_withdraw = StringVar()
        self.amount_sent = DoubleVar()
        self.Beneficiary_acctno =""
        self.Beneficiary_balance = ""

        self.mainPage()


        self.root.mainloop()


    def mainPage(self):
        self.frameb.destroy()
        self.frameb = Frame(self.root)
        self.frameb.config(bg = 'blue')
        self.mplbn = Label(self.frameb, font = ('OptimusPrinceps', 12, 'bold'), fg = 'black', text = 'Welcome to OLAHINDY Bank')
        self.mplbn.grid( columnspan= 7)  
        self.rgr = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd= 2, text = 'Registration', command=self.regPage)
        self.rgr.grid(row =2 , column = 1)
        self.lgn = Button(self.frameb, font = ('arial', 10, 'bold'),  bg = 'red',fg = 'white', bd = 2, text = 'Login', command= self.loginPage)
        self.lgn.grid(row = 3, column= 1)
        self.gethelp = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = 'Get Help', command = self.gethelp)
        self.gethelp.grid(row = 2, column= 5)
        self.exit = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = 'Exit', command= self.exitPage)
        self.exit.grid(row = 3, column= 5) 
        self.frameb.pack()
#****************************************************************************FOR REG PAGE ANDF FUNCTION*******************************************************
    def regPage(self):
        playsound('beep-02.mp3')
        self.frameb.destroy()
        self.frameb = Frame(self.root, height = 700, width = 500)
        self.frameb.config(bg = 'blue')
        self.reglbn1 = Label(self.frameb, font = ('OptimusPrinceps', 20, 'bold'),  bg = 'blue', fg = 'black', bd = 10,  text = 'Please Kindly Create Your Account With Us')
        self.reglbn1.grid(columnspan = 7)
        self.regtitle = Label(self.frameb, font = ('arial', 6, 'bold'), bg = 'red', fg = 'white', text = 'Title').grid(row =1 , column = 0)
        self.regfname = Label(self.frameb, font = ('arial', 6, 'bold'), bg = 'red', fg = 'white',   text = 'First Name').grid(row =2 , column = 0)
        self.regname = Label(self.frameb, font = ('arial', 6, 'bold'), bg = 'red', fg = 'white',   text = 'Others Name').grid(row =3 , column = 0)
        self.gen = Label(self.frameb, font = ('arial', 6, 'bold'), bg = 'red', fg = 'white',  text = 'Gender').grid(row =4 , column = 0)
        self.Marstatus = Label(self.frameb, font = ('arial', 6, 'bold'), bg = 'red', fg = 'white',  text = 'Marital Status').grid(row =5 , column = 0)

        self.Marstatus_entry = StringVar()
        self.married = Radiobutton(self.frameb, text = 'Married', variable = self.Marstatus_entry, value = 'Married').grid(row =5 , column = 1)
        self.single = Radiobutton(self.frameb, text = 'Single', variable =self.Marstatus_entry, value = 'Single').grid(row =5 , column = 2)
        self.divorce = Radiobutton(self.frameb, text = 'Divorce', variable =self.Marstatus_entry, value = 'Divorce').grid(row =5 , column = 3) 
        
        self.country = Label(self.frameb, font = ('arial', 6, 'bold'), bg = 'red', fg = 'white', text = 'Country').grid(row =6 , column = 0)
        self.purpose = Label(self.frameb, font = ('arial', 6, 'bold'), bg = 'red', fg = 'white',text = 'Purpose of Account').grid(row =7 , column = 0)
        
        self.purpose_entry = StringVar()

        self.savings = Radiobutton(self.frameb, text = 'Savings', variable = self.purpose_entry, value = 'Saving').grid(row =7 , column = 1)
        self.currrent = Radiobutton(self.frameb, text = 'Current', variable =self.purpose_entry, value = 'Current').grid(row =7 , column = 2)
        self.fixed = Radiobutton(self.frameb, text = 'Fixed', variable =self.purpose_entry, value = 'Fixed').grid(row =7 , column = 3) 
        self.phn = Label(self.frameb, font = ('arial', 6, 'bold'),  bg = 'red', fg = 'white',   text = 'Phone Number').grid(row =8 , column = 0)
        self.eml = Label(self.frameb, font = ('arial', 6, 'bold'),  bg = 'red', fg = 'white',  text = 'Email').grid(row =9 , column = 0)
        self.cty = Label(self.frameb, font = ('arial', 6, 'bold'),  bg = 'red', fg = 'white',  text = 'City/Town').grid(row =10 , column = 0)
        self.pin = Label(self.frameb, font = ('arial', 6, 'bold'),  bg = 'red', fg = 'white',  text = 'Four Digit PIN').grid(row =11 , column =0)
      #ENTRY FOR ALL THE REG DATA
        self.regtitle_entry = Entry(self.frameb, font =('arial', 8), bd= 5, insertwidth = 2, bg = 'white' )
        self.regtitle_entry.grid(row = 1, column = 2)
        self.regfname_entry = Entry(self.frameb, font =('arial', 8), bd= 5, insertwidth = 2, bg = 'white' )
        self.regfname_entry.grid(row = 2, column = 2)
        self.regname_entry = Entry(self.frameb, font =('arial', 8), bd= 5, insertwidth = 2, bg = 'white')
        self.regname_entry.grid(row = 3, column = 2)
        self.gen_entry = Entry(self.frameb, font =('arial', 8), bd= 5, insertwidth = 2, bg = 'white')
        self.gen_entry.grid(row = 4, column = 2)
        self.country_entry = Entry(self.frameb, font =('arial', 8), bd= 5, insertwidth = 2, bg = 'white')
        self.country_entry.grid(row = 6, column = 2)
        self.phn_entry = Entry(self.frameb, font =('arial', 8), bd= 5, insertwidth = 2, bg = 'white')
        self.phn_entry.grid(row = 8, column = 2)
        self.eml_entry = Entry(self.frameb, font =('arial', 8), bd= 5,  insertwidth = 2, bg = 'white')
        self.eml_entry.grid(row = 9, column = 2)
        self.cty_entry = Entry(self.frameb, font =('arial', 8), bd= 5, insertwidth = 2, bg = 'white')
        self.cty_entry.grid(row = 10, column = 2)
        self.pin_entry = Entry(self.frameb, font =('arial', 8), bd= 5, insertwidth = 2, bg = 'white')
        self.pin_entry.grid(row = 11, column = 2)

        self.regbtn = Button(self.frameb, font = ('arial', 15, 'bold'), bg = 'red', fg = 'white', bd= 2, text= 'Submit', command= self.reg_function)
        self.regbtn.grid(row =12, column = 2)
        #for mainpage and login button
        self.mainP = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd= 2, text = 'Main Page', command = self.mainPage)
        self.mainP.grid(row =12 , column = 0)
        self.lgn = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd = 2, text = 'Login', command = self.loginPage)
        self.lgn.grid(row = 12 , column= 1)
        self.frameb.pack()

    def reg_function(self):
        playsound('beep-02.mp3')
        mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'atmAPP')
        mycursor = mydb.cursor()
        self.account_no = random.randrange(1, 30000000000)
        self.regtitle_en = self.regtitle_entry.get()
        self.purpose_en =self.purpose_entry.get()
        self.Marstatus_en = self.Marstatus_entry.get()
        self.regfname_en =  self.regfname_entry.get()
        self.regname_en = self.regname_entry.get()
        self.gen_en = self.gen_entry.get()
        self.country_en = self.country_entry.get()
        self.phn_en = self.phn_entry.get()
        self.eml_en = self.eml_entry.get() 
        self.cty_en = self.cty_entry.get()
        self.pin_en = self.pin_entry.get()

        myquery = ("INSERT INTO customer_detail(Title, Account_no,Ful_name, Other_names, Phone, ePIN, Gender,Marital_status, Country, Account_purpose, Email, City)  VALUES('%s',\
         '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(self.regtitle_en, self.account_no , self.regfname_en,self.regname_en,self.phn_en, self.pin_en, self.gen_en,
            self.Marstatus_en,self.country_en,self.purpose_en ,self.eml_en , self.cty_en ))
        mycursor.execute(myquery)
        mydb.commit()
        if mycursor.rowcount ==1:
            self.deposit_page()
            showinfo('Message', 'Succesfullly! Kindly deposit to perform a Transaction')

        else:
            showinfo('Message', 'Your account Registration failed')

#****************************************************************************FOR login PAGE ANDF FUNCTION***********************************************
    def loginPage(self):
        playsound('beep-02.mp3')
        self.frameb.destroy()
        self.frameb = Frame(self.root)
        self.frameb.config(bg = 'blue')
        self.loginlbn1 = Label(self.frameb, font = ('OptimusPrinceps', 20, 'bold'), fg = 'black', bd = 10,  text = 'Enter Your Info to login')
        self.loginlbn1.grid(columnspan  =7)
        self.accountlbn = Label(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', text = 'Account No')
        self.accountlbn.grid(row= 3, column = 3)
        self.Epin = Label(self.frameb, font = ('arial', 10, 'bold'),bg = 'red', fg = 'white', text = 'E-pin')
        self.Epin.grid(row= 4, column = 3)

        self.account_entry = Entry(self.frameb, font =('arial', 8), bd= 5,  insertwidth = 2, bg = 'white')
        self.account_entry.grid(row = 3, column = 4)
        self.epin_entry = Entry(self.frameb, font =('arial', 8), bd= 5,  insertwidth = 2, bg = 'white')
        self.epin_entry.grid(row = 4, column = 4)
        self.loginbtn = Button(self.frameb, font = ('arial', 8, 'bold'), bg = 'red', fg = 'white', bd= 10, text = 'Login', command= self.login_Function )
        self.loginbtn.grid(row =5 , column = 4)
        self.forgetEpin = Button(self.frameb, font = ('arial', 8, 'bold'), bg = 'red', fg = 'white', bd= 1, text = 'forget ePIN')
        self.forgetEpin.grid(row =6 , column =4 )
        self.mainP = Button(self.frameb, font = ('arial', 6, 'bold'), bg = 'red', fg = 'white', bd= 10, text = 'Home', command = self.mainPage)
        self.mainP.grid(row =6 , column = 0)
        self.frameb.pack()

    def login_Function(self):
        playsound('beep-02.mp3')
        mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'atmAPP')
        mycursor = mydb.cursor()
        account_no = self.account_entry.get()
        ePIN  = self.epin_entry.get()
        query = "SELECT Account_no, ePIN FROM customer_detail WHERE Account_no = %s and ePIN = %s"
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

    def exitPage(self):
        playsound('beep-02.mp3')
        self.root.destroy()
#****************************************************************************FOR USER PROFILE PAGE ANDF FUNCTION***********************************************
    def profilePage(self):
        playsound('beep-02.mp3')
        self.frameb.destroy()
        self.frameb = Frame(self.root)
        self.frameb.config(bg = 'blue')
        self.plbn = Label(self.frameb, fg= 'black', bd = 10, text = 'Hi! Welcome to your Account Profile \n Please Kindly Choose a Transaction to Perform')
        self.plbn.grid(columnspan = 9)
        self.depbtn = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd= 2, text = 'Deposit', command  =self.deposit_page )
        self.depbtn.grid(row =2 , column = 0)
        self.balbtn = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd= 2, text = 'Balance', command = self.balanceChecker)
        self.balbtn.grid(row =3 , column = 0)
        self.withdrawbtn = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd= 2, text = 'Withdraw', command =self.withdraw_Page)
        self.withdrawbtn.grid(row =4 , column = 0)
        self.pin_change = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd= 2, text = 'Change Pin', command = self.PinPage)
        self.pin_change.grid(row =3 , column = 8)
        self.sendmoney = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd= 2, text = 'Send Money', command = self.sendmoney_Page)
        self.sendmoney.grid(row =2 , column = 8)
        self.quit = Button(self.frameb, font = ('arial', 10, 'bold'),bg = 'red', fg = 'white',bd= 2, text = 'Exit', command  = self.mainPage)
        self.quit.grid(row =4 , column = 8)
        self.frameb.pack()

#****************************************************************************FOR DEPOSIT PAGE ANDF FUNCTION********************************************************
    def deposit_page(self):
        playsound('beep-02.mp3')
        self.frameb.destroy()
        self.frameb = Frame(self.root)
        self.frameb.config(bg = 'blue')
        self.depositlbn = Label(self.frameb, font = ('arial', 10, 'bold'), fg = 'black', bd = 10, text = 'Please Enter the amount')
        self.depositlbn.grid(columnspan = 7)
        self.amount_dbtn = Label(self.frameb, font = ('arial', 8, 'bold'), fg = 'black', text = 'Amount').grid(row =2 , column = 1)
        self.amountd = StringVar()
        self.amount_entry = ttk.Combobox(self.frameb, textvariable = self.amountd, values =[5000,10000,50000,100000] )
        self.amount_entry.grid(row = 2, column = 2)
        self.nextbtn = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd= 10, text = 'Next', command = self.dep_Function1).grid(row =3 , column = 2)
        self.PP = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd= 10, text = 'Profile', command = self.profilePage)
        self.PP.grid(row= 3, column= 0)
        self.frameb.pack()

    def dep_Function1(self):
        playsound('beep-02.mp3')
        mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'atmAPP')
        mycursor = mydb.cursor()
        self.amount_deposit = self.amountd.get()
        query = "SELECT Account_balance FROM customer_detail WHERE Account_no =%s and ePIN = %s"
        values= (self.account_number, self.epinreal)
        mycursor.execute(query, values)
        bal = mycursor.fetchone()
        mybal = bal[0]
        if self.amount_deposit !=None:
            self.dep_Next()
        else:
            showinfo('alert', 'Wrong')

    def dep_Next(self):
        playsound('beep-02.mp3')
        self.frameb.destroy()
        self.frameb = Frame(self.root)
        self.frameb.config(bg = 'blue')
        self.depositlbn = Label(self.frameb, font = ('arial', 10, 'bold'), fg = 'black', bd = 10, text = 'Please Enter Your ePIN')
        self.depositlbn.grid(columnspan = 7)
        self.amount_dbtn = Label(self.frameb, font = ('arial', 8, 'bold'), fg = 'black', text = 'ePIN').grid(row =2 , column = 1)
        self.ePIN = Entry(self.frameb, font =('arial', 8), bd= 5,  insertwidth = 2, bg = 'white')
        self.ePIN.grid(row=2, column = 2)
        self.depositbtn = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd= 10, text = 'Deposit', command = self.dep_Function2).grid(row =3 , column = 2)
        self.PP = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd= 10, text = 'Profile', command = self.profilePage)
        self.PP.grid(row= 3, column= 0)
        self.frameb.pack()

    def dep_Function2(self):
        playsound('beep-02.mp3')
        mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'atmAPP')
        mycursor = mydb.cursor()
        ePIN = self.ePIN.get()
        query = "SELECT Account_balance FROM customer_detail WHERE Account_no =%s and ePIN = %s"
        values= (self.account_number, self.epinreal)
        mycursor.execute(query, values)
        bal = mycursor.fetchone()
        self.Account_balance = bal[0]
        print(bal)
        if bal !=None:
            new_bal = (int(self.amount_deposit) + int(bal[0]))
            query1 = 'UPDATE customer_detail SET Account_balance = %s WHERE account_no = %s'
            values1 = (new_bal, self.account_number)
            mycursor.execute(query1, values1)
            mydb.commit()
            playsound('atmsound.mp3')
            showinfo('Message', 'Your money has been deposited')
        else:
            showinfo('Message','Invalid detail')
        mydb.close()
        
#****************************************************************************FOR WITHDRAW PAGE ANDF FUNCTION********************************************************
    def withdraw_Page(self):
        playsound('beep-02.mp3')
        self.frameb.destroy()
        self.frameb = Frame(self.root)
        self.frameb.config(bg = 'blue')
        self.withdraw_lbn = Label(self.frameb, font = ('arial', 10, 'bold'), fg = 'black', bd = 10, text = 'Account Type')
        self.withdraw_lbn.grid(columnspan = 7)
        self.acct_type = StringVar()
        self.account_type = ttk.Combobox(self.frameb, textvariable = self.acct_type, values =['Saving','Current','Fixed'] )
        self.account_type.grid(row = 2, column= 2)
        self.next1 = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd= 10, text = 'Next', command = self.withdraw_F1).grid(row =3 , column = 2)
        self.PP = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd= 10, text = 'Profile', command = self.profilePage)
        self.PP.grid(row= 3, column= 0)
        self.frameb.pack()

    def withdraw_F1(self):
        playsound('beep-02.mp3')
        mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'atmAPP')
        mycursor = mydb.cursor()
        purpose_of_Acct = self.acct_type.get()
        query = "SELECT Account_purpose FROM customer_detail WHERE Account_no =%s and ePIN = %s"
        values= (self.account_number, self.epinreal)
        mycursor.execute(query, values)
        purpose = mycursor.fetchone()
        account_p = purpose[0]
        if account_p.lower() == purpose_of_Acct.lower():
            self.amountPage()
        else:
            pass
        mydb.close()

    def amountPage(self):
        playsound('beep-02.mp3')
        self.frameb.destroy()
        self.frameb = Frame(self.root)
        self.frameb.config(bg = 'blue')
        self.withdraw_lbn = Label(self.frameb, font = ('arial', 10, 'bold'), fg = 'black', bd = 10, text = 'Enter Amount')
        self.withdraw_lbn.grid(columnspan = 5)
        self.amountw = StringVar()
        self.amount_entry = ttk.Combobox(self.frameb, textvariable = self.amountw, values =[5000,10000,50000,100000])
        self.amount_entry.grid(row = 2, column = 2)
        self.next2 = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd= 10, text = 'Next', command = self.withdraw_F2).grid(row =3 , column = 2)
        self.PP = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd= 10, text = 'Profile', command = self.profilePage)
        self.PP.grid(row= 3, column= 0)
        self.frameb.pack()

    def withdraw_F2(self):
        playsound('beep-02.mp3')
        mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'atmAPP')
        mycursor = mydb.cursor()
        self.amount_withdraw = self.amountw.get()
        query1 = "SELECT Account_balance FROM customer_detail WHERE Account_no =%s and ePIN = %s"
        values1= (self.account_number, self.epinreal)
        mycursor.execute(query1, values1)
        bal = mycursor.fetchone()
        self.Account_balance = bal[0]
        if bal!=None:
            self.finalpin_Page()
        else:
            pass
        mydb.close()


    def finalpin_Page(self):
        playsound('beep-02.mp3')
        self.frameb.destroy()
        self.frameb = Frame(self.root)
        self.frameb.config(bg = 'blue')
        self.withdraw_lbn = Label(self.frameb, font = ('arial', 10, 'bold'), fg = 'black', bd = 10, text = 'Enter ePIN')
        self.withdraw_lbn.grid(columnspan = 5)
        self.ePIN = Entry(self.frameb, font =('arial', 8), bd= 5,  insertwidth = 2, bg = 'white')
        self.ePIN.grid(row=2, column = 2)
        self.next2 = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd= 10, text = 'Withdraw', command = self.withdraw_F3).grid(row =3 , column = 2)
        self.PP = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd= 10, text = 'Profile', command = self.profilePage)
        self.PP.grid(row= 3, column= 0)
        self.frameb.pack()

    def withdraw_F3(self):
        playsound('beep-02.mp3')
        mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'atmAPP')
        mycursor = mydb.cursor()
        ePIN = self.ePIN.get()
        query2 = "SELECT Account_balance FROM customer_detail WHERE Account_no =%s and ePIN = %s"
        values2= (self.account_number, self.epinreal)
        mycursor.execute(query2, values2)
        bal = mycursor.fetchone()
        self.Account_balance = bal[0]
        if bal[0] > int(self.amount_withdraw) and ePIN ==self.epinreal:
            new_bal = int(self.Account_balance) - int(self.amount_withdraw)
            query4 = 'UPDATE customer_detail SET Account_balance = %s WHERE account_no = %s'
            values4 = (new_bal, self.account_number)
            mycursor.execute(query4, values4)
            mydb.commit()
            playsound('atmsound.mp3')
            showinfo('Message', 'Please Kindly Take Your Cash')
        else:
            showinfo('Message','Invalid detail')
        mydb.close()





#****************************************************************************FOR SEND MONEY PAGE AND FUNCTION********************************************************
    def sendmoney_Page(self):
        playsound('beep-02.mp3')
        self.frameb.destroy()
        self.frameb = Frame(self.root)
        self.frameb.config(bg = 'blue')
        self.sm_lbn = Label(self.frameb, font = ('arial', 10, 'bold'),bg = 'blue', fg = 'black', bd = 10, text = 'Enter the Beneficiary Account NO')
        self.sm_lbn.grid(columnspan = 5)
        self.bacct_entry = Entry(self.frameb, font =('arial', 8), bd= 5,  insertwidth = 2, bg = 'white')
        self.bacct_entry.grid(row=1, column = 3)
        self.nextacct_no = Button(self.frameb, font = ('arial', 8, 'bold'), bg = 'red', fg = 'white', bd= 5, text = 'Next', command = self.sendmoney_F1).grid(row =2 , column = 3)
        self.PP = Button(self.frameb, font = ('arial', 8, 'bold'), bg = 'red', fg = 'white', bd= 5, text = 'Profile', command = self.profilePage)
        self.PP.grid(row= 2, column= 0)
        self.frameb.pack()

    def sendmoney_F1(self):
        playsound('beep-02.mp3')
        mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'atmAPP')
        mycursor = mydb.cursor()
        self.Beneficiary_acctno = self.bacct_entry.get()
        query1 = "SELECT Account_balance FROM customer_detail WHERE Account_no = "+(self.Beneficiary_acctno)
        mycursor.execute(query1)
        bal = mycursor.fetchone()
        print(bal)
        self.Beneficiary_balance = bal[0]
        if bal!=None:
            self.sm_Next()
        else:
            pass
        mydb.close()


    def sm_Next(self):
        playsound('beep-02.mp3')
        self.frameb.destroy()
        self.frameb = Frame(self.root)
        self.frameb.config(bg = 'blue')
        self.sm_lbn = Label(self.frameb, font = ('arial', 10, 'bold'), bg = 'blue',fg = 'black', bd = 10, text = 'Enter Amount to Send')
        self.sm_lbn.grid(columnspan = 5)
        self.amount_entry = ttk.Combobox(self.frameb, textvariable = self.amount_sent, values =[5000,10000,50000,100000] )
        self.amount_entry.grid(row = 1, column = 3)
        self.nextammount= Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd= 5, text = 'Next', command=self.sm_Final).grid(row =2 , column = 3)
        self.PP = Button(self.frameb, font = ('arial', 10, 'bold'), bg = 'red', fg = 'white', bd= 5, text = 'Profile', command = self.profilePage)
        self.PP.grid(row= 2, column= 0)
        self.frameb.pack()

    def sendmoney_F2(self):
        playsound('beep-02.mp3')
        mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'atmAPP')
        mycursor = mydb.cursor()
        query2 = "SELECT Account_balance FROM customer_detail WHERE Account_no =%s and ePIN = %s"
        values2= (self.account_number, self.epinreal)
        mycursor.execute(query2, values2)
        bal = mycursor.fetchone()
        self.Account_balance = bal[0]
        if int(self.Account_balance) > int(self.amount_sent.get()):
            self.sm_Final()
        else:
            pass
        mydb.close()

    def sm_Final(self):
        playsound('beep-02.mp3')
        self.frameb.destroy()
        self.frameb = Frame(self.root)
        self.frameb.config(bg = 'blue')
        self.sm_lbn = Label(self.frameb, font = ('arial', 10, 'bold'), bg = 'blue', fg = 'black', bd = 10, text = 'Enter Your ePIN')
        self.sm_lbn.grid(columnspan = 5)
        self.ePIN_entry = Entry(self.frameb, font =('arial', 8), bd= 5,  insertwidth = 2, bg = 'white')
        self.ePIN_entry.grid(row=1, column = 3)
        self.nextamount= Button(self.frameb, font = ('arial', 8, 'bold'), bg = 'red', fg = 'white', bd= 5, text = 'Send Money', command =self.sendmoney_F3).grid(row =2 , column = 3)
        self.PP = Button(self.frameb, font = ('arial', 8, 'bold'), bg = 'red', fg = 'white', bd= 5, text = 'Profile', command = self.profilePage)
        self.PP.grid(row= 2, column= 0)
        self.frameb.pack()

    def sendmoney_F3(self):
        playsound('beep-02.mp3')
        mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'atmAPP')
        mycursor = mydb.cursor()
        ePIN = self.ePIN_entry.get()
        query2 = "SELECT Account_balance FROM customer_detail WHERE Account_no =%s and ePIN = %s"
        values2= (self.account_number, ePIN )
        mycursor.execute(query2, values2)
        bal = mycursor.fetchone()
        self.Account_balance = bal[0]
        print(self.amount_sent.get())
        if (self.Account_balance) > int(self.amount_sent.get()) and ePIN == self.epinreal:
            new_bal = int(self.Account_balance) - int(self.amount_sent.get())
            Beneficiary_newbal = int(self.Beneficiary_balance) + int(self.amount_sent.get())
            query4 = 'UPDATE customer_detail SET Account_balance = %s WHERE account_no = %s'
            values4 = (new_bal, self.account_number)
            mycursor.execute(query4, values4)
            mydb.commit()

            query3 = "UPDATE customer_detail SET Account_balance = %s WHERE Account_no = %s"
            values3 = (Beneficiary_newbal, self.Beneficiary_acctno)
            mycursor.execute(query3, values3)
            mydb.commit()
            playsound('atmsound.mp3')
            showinfo('Message', 'Transferred Succesfullly')
        else:
            showinfo('Message','Invalid detail')
        mydb.close()
            

#****************************************************************************FOR PIN CHANGE PAGE AND FUNCTION********************************************

    def PinPage(self):
        playsound('beep-02.mp3')
        self.frameb.destroy()
        self.frameb = Frame(self.root)
        self.frameb.config(bg = 'blue')
        self.pin_lbn = Label(self.frameb, font = ('arial', 10, 'bold'), bg = 'blue', fg = 'black', bd = 10, text = 'Enter Your Current ePIN')
        self.pin_lbn.grid(columnspan = 5)
        self.ePIN_entry = Entry(self.frameb, font =('arial', 8), bd= 5,  insertwidth = 2, bg = 'white')
        self.ePIN_entry.grid(row=1, column = 3)
        self.pin_next= Button(self.frameb, font = ('arial', 8, 'bold'), bg = 'red', fg = 'white', bd= 5, text = 'Next', command = self.pinchange_F1).grid(row =2 , column = 3)
        self.PP = Button(self.frameb, font = ('arial', 8, 'bold'), bg = 'red', fg = 'white', bd= 5, text = 'Profile', command = self.profilePage)
        self.PP.grid(row= 2, column= 0)
        self.frameb.pack()

    def pinchange_F1(self):
        playsound('beep-02.mp3')
        mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'atmAPP')
        mycursor = mydb.cursor()
        query2 = "SELECT ePIN FROM customer_detail WHERE Account_no =%s and ePIN = %s"
        values2= (self.account_number, self.ePIN_entry.get())
        mycursor.execute(query2, values2)
        pin = mycursor.fetchone()
        self.Account_balance = pin[0]
        if pin[0] == self.ePIN_entry.get():
            self.pin_Final()
        else:
            pass
        mydb.close()


    def pin_Final(self):
        playsound('beep-02.mp3')
        self.frameb.destroy()
        self.frameb = Frame(self.root)
        self.frameb.config(bg = 'blue')
        self.pin_lbn = Label(self.frameb, font = ('arial', 10, 'bold'), bg = 'blue', fg = 'black', bd = 10, text = 'Enter Your New ePIN')
        self.pin_lbn.grid(columnspan = 5)
        self.new_ePIN_entry = Entry(self.frameb, font =('arial', 8), bd= 5,  insertwidth = 2, bg = 'white')
        self.new_ePIN_entry.grid(row=1, column = 3)
        self.pin_next= Button(self.frameb, font = ('arial', 8, 'bold'), bg = 'red', fg = 'white', bd= 5, text = 'Change ePIN', command = self.pinchange_F2).grid(row =2 , column = 3)
        self.PP = Button(self.frameb, font = ('arial', 8, 'bold'), bg = 'red', fg = 'white', bd= 5, text = 'Profile', command = self.profilePage)
        self.PP.grid(row= 2, column= 0)
        self.frameb.pack()

    def pinchange_F2(self):
        playsound('beep-02.mp3')
        mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'atmAPP')
        mycursor = mydb.cursor()
        if self.new_ePIN_entry.get() !=None:
            query = 'UPDATE customer_detail SET ePIN = %s WHERE account_no = %s'
            values = (self.new_ePIN_entry.get(), self.account_number)
            mycursor.execute(query, values)
            mydb.commit()
            playsound('atmsound.mp3')
            showinfo('Alert', 'ePIN Changed Succesfully')  
            mydb.commit()
        else:
            pass
        mydb.close()
#****************************************************************************FOR BALANCE CHECKER PAGE AND FUNCTION********************************************
    def balanceChecker(self):
        playsound('atmsound.mp3')
        mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'atmAPP' )
        mycursor = mydb.cursor()
        query = "SELECT Account_balance FROM customer_detail WHERE Account_no = "+str(self.account_number)
        mycursor.execute(query)
        mybal = mycursor.fetchone()
        print(mybal)
        showinfo('Account Balance', 'Dear customer, your account balance is N'+ str(mybal[0]))  
        mydb.close()

    def gethelp(self):
        playsound('beep-02.mp3')
        self.frameb.destroy()
        self.frameb = Frame(self.root)
        self.frameb.config(bg = 'blue')
        self.gethelp_lbn = Label(self.frameb, font = ('arial', 8, 'bold'), bg= 'red', fg = 'white', bd = 10, 
            text = 'Olahindy bank was established in 1957 and since then, we have bee \nproviding a reliable service to every customers banking with us. \nWhat set us apart from our competitor is a good personality and objectives \nto serve our customer with prompt response and realibility. \nPlease Kindly Vist OLAHINDY.com to know how to operate our BankingApp' )
        self.gethelp_lbn.grid(row = 0, column = 0)
        self.frameb.pack()












        


atm = AtmApp()

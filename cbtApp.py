from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import random
import sys
import mysql.connector

# for the excel
from pymysql import* 
import xlwt 
import pandas.io.sql as sql



class CbtApp:
	def __init__(self):
		self.root = Tk()
		self.root.title('TojMark CBT Application')
		self.root.config(bg = '#57163d')
		self.root.geometry("800x400")
		self.user_name = ''
		self.password_real = ''
		self.matric_no = ""
		self.adm_id = ""
		self.frameb = Frame(self.root, width = 800, height= 400, bg = '#57163d')
		self.loginPage()
		self.number = 1
		self.count = self.score = self.percentage = 0
		self.user_ver=''
 
		self.root.mainloop()
#****************************************************************************FOR USER LOGIN PAGE ANDF FUNCTION********************************************************************************
	def loginPage(self):
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.username_lbn = Label(self.frameb, text = 'Username').grid(row = 0,column = 0)
		self.password_lbn = Label(self.frameb, text ='Password').grid(row = 1,column = 0)
		self.username_entry = Entry(self.frameb)
		self.username_entry.grid(row = 0,column = 1)
		self.password_entry = Entry(self.frameb, show = '*')
		self.password_entry.grid(row = 1,column = 1)

		self.position = StringVar()

		self.student = Radiobutton(self.frameb, text = 'Student', variable = self.position, 
			value = 'Student', tristatevalue = 0).grid(row =2 , column = 0)
		self.admin = Radiobutton(self.frameb, text = 'Administrator', variable =self.position, 
			value = 'Administrator', tristatevalue = 0).grid(row =2 , column = 1)

		self.login_btn = Button(self.frameb, text = 'Login', bd = 5, font = ('arial', 10, 'bold'),
			bg ='#57163d', fg = 'white' ,activebackground = '#de1d3d', command = self.loginFunction).grid(row = 3,column = 1)
		self.login_btn = Button(self.frameb, text = 'Register', bd = 5, font = ('arial', 10, 'bold'),
			bg= '#57163d', fg='white',activebackground = '#de1d3d', command = self.registerPage).grid(row = 3,column = 0)
		self.frameb.pack()

	def loginFunction(self):
		# self.quizFunction()
		mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'CBTApp_db')
		mycursor = mydb.cursor()
		self.username = self.username_entry.get()
		password = self.password_entry.get()
		position = self.position.get()

		if position == 'Administrator':
			query = "SELECT adm_id, Username, password FROM admin_portal WHERE Username = %s and Password = %s"
			values = (self.username, password)
			mycursor.execute(query, values)
			mylogin = mycursor.fetchone()
			self.adm_id = mylogin[0]
			self.user_name = mylogin[1]
			self.password_real = mylogin[2]
			if mylogin !=None:
				print('succesfully')
				self.adminPanel() 
			else:
				showinfo('Message', 'Invalid Login Detail')         
		elif position == 'Student':
			query = "SELECT Username, password, Matric_id FROM std_portal WHERE Username = %s and Password = %s"
			values = (self.username, password)
			mycursor.execute(query, values)
			mylogin = mycursor.fetchone()
			self.user_name = mylogin[0]
			self.password_real = mylogin[1]
			self.matric_no = mylogin[2]
			if mylogin !=None:
				print('succesfully')
				self.quizPage()
			else:
				showinfo('Message', 'Invalid Login Detail')		            

		else:
			pass

#****************************************************************************FOR USER REGISTRATION PAGE ANDF FUNCTION******************************************************************
	def registerPage(self):
		self.frameb.destroy()
		self.frameb = Frame(self.root)
		self.fullname_lbn = Label(self.frameb, text = 'Full Name').grid(row = 0,column = 0)
		self.username_lbn = Label(self.frameb, text = 'Username').grid(row = 1,column = 0)
		self.age_lbn = Label(self.frameb, text = 'Age').grid(row = 2,column = 0)
		self.password_lbn = Label(self.frameb, text = 'Password').grid(row = 3,column = 0)
		self.reg_choice = StringVar()
		student = Radiobutton(self.frameb, text = 'Student', variable = self.reg_choice, 
			value = 'Student', tristatevalue = 0).grid(row =4 , column = 0)
		admin = Radiobutton(self.frameb, text = 'Administrator', variable =self.reg_choice, 
			value = 'Administrator', tristatevalue = 0).grid(row =4 , column = 1)

		self.fullname_entry = Entry(self.frameb)
		self.fullname_entry.grid(row = 0,column = 1)
		self.regusername_entry = Entry(self.frameb)
		self.regusername_entry.grid(row = 1,column = 1)
		self.age_entry = Entry(self.frameb)
		self.age_entry.grid(row = 2,column = 1)
		self.regpassword_entry = Entry(self.frameb, show = '*')
		self.regpassword_entry.grid(row = 3,column = 1)

		self.login_btn = Button(self.frameb, text = 'Login', bd = 5, font = ('arial', 8, 'bold'),
			bg ='#57163d', fg = 'white' ,activebackground = '#de1d3d', command=self.loginPage).grid(row = 5,column = 0)
		self.login_btn = Button(self.frameb, text = 'Register', bd = 5, font = ('arial', 10, 'bold'),
			bg= '#57163d', fg='white',activebackground = '#de1d3d', command = self.regFunction).grid(row = 5,column = 1)
		self.frameb.pack()

	def regFunction(self):
		mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'CBTApp_db')
		mycursor = mydb.cursor()
		matric_no = random.randrange(2, 201234)
		fullname = self.fullname_entry.get()
		username = self.regusername_entry.get()
		age = self.age_entry.get()
		password = self.regpassword_entry.get()
		status = self.reg_choice.get()
		if status == 'Administrator':
			myquery = ("INSERT INTO admin_portal(Ful_name, Username, Age,  Password, Status)  VALUES('%s',\
	         '%s', '%s', '%s', '%s')" %(fullname,  username, age, password, status))
			mycursor.execute(myquery)
			mydb.commit()
			if mycursor.rowcount ==1:
				self.adminPanel()
				showinfo('Message', 'Registered Succesfully!')
			else:
				showinfo('Message', 'Registration failed')
		if status == 'Student':
			myquery = ("INSERT INTO std_portal(Matric_id, Ful_name,Age, Username,  Password, Status)  VALUES('%s', '%s',\
	         '%s', '%s', '%s', '%s')" %(matric_no, fullname, age, username,  password, status))
			mycursor.execute(myquery)
			mydb.commit()
			if mycursor.rowcount ==1:
				self.quizPage()
				showinfo('Message', 'Registered Succesfully!')
			else:
				showinfo('Message', 'Registration failed')
		else:
			pass

#****************************************************************************FOR ADMNISTRATOR PAGE ANDF FUNCTION************************************************************************
	def adminPanel(self):
		self.frameb.destroy()
		self.frameb= Frame(self.root, width = 200, height = 200)

		self.first_lbn = Label(self.frameb, text = 'Hey! '+self.user_name +''+'  Welcome To Your Panel', 
			font = ('arial', 12, 'bold')).grid(columnspan = 2)

		self.admins_btn = Button(self.frameb, text = 'Administrators', bd = 5, font = ('arial', 8, 'bold'),
			bg= '#57163d', fg='white',activebackground = '#de1d3d', command = self.admprofileFunction).grid(row = 1,column = 0)
		self.students_btn = Button(self.frameb, text = 'Export Students', bd = 5, font = ('arial', 8, 'bold'),
			bg= '#57163d', fg='white',activebackground = '#de1d3d', command = self.getStudent).grid(row = 1,column =1 )
		self.questions_btn = Button(self.frameb, text = 'Update Questions', bd = 5, font = ('arial', 8, 'bold'),
			bg ='#57163d', fg = 'white' ,activebackground = '#de1d3d', command = self.questionPage).grid(row = 2,column = 0)
		self.register_btn = Button(self.frameb, text = 'Register Student', bd = 5, font = ('arial', 8, 'bold'),
			bg ='#57163d', fg = 'white' ,activebackground = '#de1d3d', command = self.registerPage).grid(row = 2,column = 1)
		self.studentresult_btn = Button(self.frameb, text = 'Students Result', bd = 5, font = ('arial', 8, 'bold'),
			bg= '#57163d', fg='white',activebackground = '#de1d3d', command = self.studentPage).grid(row = 3,column = 0)
		self.homo_btn = Button(self.frameb, text = 'Log Out', bd = 5, font = ('arial', 8, 'bold'),
			bg= '#57163d', fg='white',activebackground = '#de1d3d', command = self.loginPage).grid(row = 3,column = 1)
		self.frameb.pack()

	def admprofileFunction(self):
		mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'CBTApp_db')
		mycursor = mydb.cursor()

		query5 = "SELECT *  FROM admin_portal WHERE Username = %s and adm_id = %s"
		value = (self.user_name, self.adm_id)
		mycursor.execute(query5, value)
		adm_detail= mycursor.fetchone()
		name= adm_detail[1]
		username  = adm_detail[2]
		age = adm_detail[3]
		password = adm_detail[4]


		self.frameb.destroy()
		self.frameb= Frame(self.root)
		self.first_lbn = Label(self.frameb, text = 'Administrator Profile', 
		font = ('arial', 12, 'bold')).grid(columnspan = 3)
		self.first_lbn = Label(self.frameb, text = 'Name = '+name, 
		font = ('arial', 12, 'bold')).grid(row = 1, column = 0)

		self.second_lbn = Label(self.frameb, text = 'Username = '+username, 
		font = ('arial', 12, 'bold')).grid(row = 2, column = 0)

		self.thrid_lbn = Label(self.frameb, text = 'Age = '+age, 
		font = ('arial', 12, 'bold')).grid(row = 3, column = 0)

		self.fourth_lbn = Label(self.frameb, text = 'password = '+password, 
		font = ('arial', 12, 'bold')).grid(row = 4, column = 0)
		self.frameb.pack()

		self.adminpanel_btn = Button(self.frameb, text = 'Admin Panel', bd = 5, font = ('arial', 8, 'bold'),
			bg= '#57163d', fg='white',activebackground = '#de1d3d', command=self.adminPanel).grid(row = 5,column = 0)
		self.frameb.pack()
	
	def studentPage(self):
		self.frameb.destroy()
		self.frameb= Frame(self.root, width = 200, height = 200)

		self.first_lbn = Label(self.frameb, text = 'Enter Student Detail' ,
			font = ('arial', 12, 'bold')).grid(columnspan = 2)

		self.second_lbn = Label(self.frameb, text = 'Username' ,
			font = ('arial', 12, 'bold')).grid(row=1,column= 0)

		self.third_lbn = Label(self.frameb, text = 'Matric No' ,
			font = ('arial', 12, 'bold')).grid(row=2,column= 0)

		self.stdU_En = Entry(self.frameb)
		self.stdU_En.grid(row=1,column= 1)

		self.stdM_En = Entry(self.frameb)
		self.stdM_En.grid(row=2,column= 1)

		self.homo_btn = Button(self.frameb, text = 'Search', bd = 5, font = ('arial', 8, 'bold'),
			bg= '#57163d', fg='white',activebackground = '#de1d3d', command = self.stdFunction).grid(row = 3,column = 1)
		self.frameb.pack()

		self.adminpanel_btn = Button(self.frameb, text = 'Admin Panel', bd = 5, font = ('arial', 8, 'bold'),
			bg= '#57163d', fg='white',activebackground = '#de1d3d', command=self.adminPanel).grid(row = 4,column = 0)
		self.frameb.pack()

	def stdFunction(self):
		std = self.stdU_En.get()
		matric = self.stdM_En.get()

		mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'CBTApp_db')
		mycursor = mydb.cursor()

		query5 = "SELECT Score, Percentage FROM student_results WHERE Username = %s and Matric_id = %s"
		val = (std, matric)
		mycursor.execute(query5, val)
		std_detail= mycursor.fetchone()
		score = std_detail[0]
		per= std_detail[1]
		print(per)

		self.frameb.destroy()
		self.frameb= Frame(self.root)
		self.first_lbn = Label(self.frameb, text = 'The Score = '+score, 
		font = ('arial', 12, 'bold')).grid(columnspan = 3)
		self.first_lbn = Label(self.frameb, text = 'Overall percentage = '+per+'%', 
		font = ('arial', 12, 'bold')).grid(columnspan = 3)
		self.frameb.pack()

	def getStudent(self):
		mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'CBTApp_db')
		mycursor = mydb.cursor()

		query = "SELECT * FROM std_portal" 
		std=sql.read_sql(query, mydb)
		# mycursor.execute(query)
		# student_detail = mycursor.fetchall()
		print(std)
		std.to_excel('Tojmark student files.xls')



		







#****************************************************************************FOR QUESTION UPDATE PAGE ANDF FUNCTION**************************************************************************

	def questionPage(self):
		self.frameb.destroy()
		self.frameb= Frame(self.root)
		self.questions_lbn = Label(self.frameb, text = 'Questions').grid(row = 0,column = 0)
		self.optionA_lbn = Label(self.frameb, text = 'Option A').grid(row = 1,column = 0)
		self.optionB_lbn = Label(self.frameb, text = 'Option B').grid(row = 2,column = 0)
		self.optionC_lbn= Label(self.frameb, text = 'Option C').grid(row = 3,column = 0)
		self.optionD_lbn = Label(self.frameb, text = 'Option D').grid(row = 4,column = 0)
		self.ans_lbn= Label(self.frameb, text = 'Answer').grid(row = 5,column = 0)
		
		self.que_entry = Text(self.frameb, width  = 20, height  = 2)
		self.que_entry.grid(row = 0, column = 1)
		self.optionA_entry = Entry(self.frameb)
		self.optionA_entry.grid(row = 1,column = 1)
		self.optionB_entry = Entry(self.frameb)
		self.optionB_entry.grid(row = 2,column = 1)
		self.optionC_entry = Entry(self.frameb)
		self.optionC_entry.grid(row = 3,column = 1)
		self.optionD_entry = Entry(self.frameb)
		self.optionD_entry.grid(row = 4,column = 1)
		self.ans_entry = Entry(self.frameb)
		self.ans_entry.grid(row = 5,column = 1)

		self.update_btn = Button(self.frameb, text = 'Update', bd = 5, font = ('arial', 8, 'bold'),
			bg= '#57163d', fg='white',activebackground = '#de1d3d', command = self.updateQuestion).grid(row = 6,column = 1)
		self.adminpanel_btn = Button(self.frameb, text = 'Admin Panel', bd = 5, font = ('arial', 8, 'bold'),
			bg= '#57163d', fg='white',activebackground = '#de1d3d', command=self.adminPanel).grid(row = 6,column = 0)
		self.frameb.pack()

	def updateQuestion(self):
		mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'CBTApp_db')
		mycursor = mydb.cursor()
		question = self.que_entry.get(1.0, "end")
		opt_a = self.optionA_entry.get()
		opt_b = self.optionB_entry.get()
		opt_c = self.optionC_entry.get()
		opt_d = self.optionD_entry.get()
		ans = self.ans_entry.get()

		myquery = ("INSERT INTO Questions(Questions, Option_A, Option_B, Option_C, Option_D, Answers)  VALUES('%s',\
	         '%s', '%s', '%s', '%s', '%s')" %(question, opt_a, opt_b, opt_c, opt_d, ans))
		mycursor.execute(myquery)
		mydb.commit()
		if mycursor.rowcount ==1:
			showinfo('Message', 'Uploaded Succesfully!')
		else:
			showinfo('Message', 'Uploading failed')




#****************************************************************************FOR QUIZ PAGE ANDF FUNCTION****************************************************************************
	def quizPage(self):
		self.frameb.destroy()
		self.frameb= Frame(self.root)
		self.first_lbn = Label(self.frameb, text = 'Hey! '+self.user_name +''+'  Welcome To Your Panel', 
			font = ('arial', 12, 'bold')).grid(columnspan = 3)
		self.confirm_lbn = Label(self.frameb, font = ('arial', 10, 'bold'), text = 'Once You Click On Start Now, \nThere Is No Going Back').grid(columnspan = 3)
		self.startnow_btn = Button(self.frameb, text = 'Start Now', bd = 5, font = ('arial', 8, 'bold'),
			bg= '#57163d', fg='white',activebackground = '#de1d3d', command = self.quizFunction).grid(row = 2,column = 1)
		self.frameb.pack()
		self.checkscore_btn = Button(self.frameb, text = 'Check Score', bd = 5, font = ('arial', 8, 'bold'),
			bg= '#57163d', fg='white',activebackground = '#de1d3d', command = self.checkScore).grid(row = 3,column = 1)
		self.frameb.pack()
		self.logout_btn = Button(self.frameb, text = 'Log out', bd = 5, font = ('arial', 8, 'bold'),
			bg= '#57163d', fg='white',activebackground = '#de1d3d', command=self.loginPage).grid(row = 4,column = 1)
		self.frameb.pack()

	def quizFunction(self):
		mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'CBTApp_db')
		mycursor = mydb.cursor()
		myquery = "SELECT * FROM Questions"
		mycursor.execute(myquery)
		self.question =  mycursor.fetchall()
		self.que1 = self.question[0]
		self.que2 = self.question[1]
		self.que3 = self.question[2]
		self.que4 = self.question[3]
		self.que5 = self.question[4]
		self.question1()
			
			
			


	def question1(self):
		self.frameb.destroy()
		self.frameb= Frame(self.root)
		self.q_lbn = Label(self.frameb, text = '1.' +str(self.que1[1]), 
			font = ('arial', 12, 'bold')).grid(columnspan = 3)
		self.que1_anwser= StringVar()

		A = Radiobutton(self.frameb, text = 'A.'+str(self.que1[2]), variable = self.que1_anwser, value = str(self.que1[2]),  tristatevalue = 0).grid(row =2 , column = 1)
		B = Radiobutton(self.frameb, text = 'B.'+str(self.que1[3]), variable =self.que1_anwser,value = str(self.que1[3]), tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C.'+str(self.que1[4]), variable =self.que1_anwser, value = str(self.que1[4]), tristatevalue = 0).grid(row =4 , column = 1)
		D = Radiobutton(self.frameb, text = 'D.'+str(self.que1[5]), variable = self.que1_anwser,  value = str(self.que1[5]),tristatevalue = 0).grid(row =5 , column = 1)
		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = '#57163d', fg = 'white', bd = 2, text = '>>>', command  = self.question2)
		self.start_now.grid(row = 5, column= 3)

		self.frameb.pack()

	def question2(self):
		self.ans1 = self.que1_anwser.get()
		self.frameb.destroy()
		self.frameb= Frame(self.root)
		self.q_lbn = Label(self.frameb, text = '2.' +str(self.que2[1]), 
			font = ('arial', 12, 'bold')).grid(columnspan = 3)
		self.que2_anwser= StringVar()

		A = Radiobutton(self.frameb, text = 'A.'+str(self.que2[2]), variable = self.que1_anwser, value = str(self.que2[2]),  tristatevalue = 0).grid(row =2 , column = 1)
		B = Radiobutton(self.frameb, text = 'B.'+str(self.que2[3]), variable =self.que1_anwser,value = str(self.que2[3]), tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C.'+str(self.que2[4]), variable =self.que1_anwser, value = str(self.que2[4]), tristatevalue = 0).grid(row =4 , column = 1)
		D = Radiobutton(self.frameb, text = 'D.'+str(self.que2[5]), variable = self.que1_anwser,  value = str(self.que2[5]),tristatevalue = 0).grid(row =5 , column = 1)
		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = '#57163d', fg = 'white', bd = 2, text = '>>>', command =self.question3)
		self.start_now.grid(row = 5, column= 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = '#57163d', fg = 'white', bd = 2, text = '<<<', command =self.question1)
		self.start_now.grid(row = 5, column= 0)
		self.frameb.pack()

	def question3(self):
		self.ans2 =self.que2_anwser.get()
		self.frameb.destroy()
		self.frameb= Frame(self.root)
		self.q_lbn = Label(self.frameb, text ='3.' +str(self.que3[1]), 
			font = ('arial', 12, 'bold')).grid(columnspan = 3)
		self.que3_anwser= StringVar()

		A = Radiobutton(self.frameb, text = 'A.'+str(self.que3[2]), variable = self.que1_anwser, value = str(self.que3[2]),  tristatevalue = 0).grid(row =2 , column = 1)
		B = Radiobutton(self.frameb, text = 'B.'+str(self.que3[3]), variable =self.que1_anwser,value = str(self.que3[3]), tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C.'+str(self.que3[4]), variable =self.que1_anwser, value = str(self.que3[4]), tristatevalue = 0).grid(row =4 , column = 1)
		D = Radiobutton(self.frameb, text = 'D.'+str(self.que3[5]), variable = self.que1_anwser,  value = str(self.que3[5]),tristatevalue = 0).grid(row =5 , column = 1)
		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = '#57163d', fg = 'white', bd = 2, text = '>>>', command =self.question4)
		self.start_now.grid(row = 5, column= 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = '#57163d', fg = 'white', bd = 2, text = '<<<',command= self.question2)
		self.start_now.grid(row = 5, column= 0)
		self.frameb.pack()

	def question4(self):
		self.ans3 = self.que3_anwser.get()
		self.frameb.destroy()
		self.frameb= Frame(self.root)
		self.q_lbn = Label(self.frameb, text ='4.' +str(self.que4[1]), 
			font = ('arial', 12, 'bold')).grid(columnspan = 3)
		self.que4_anwser= StringVar()

		A = Radiobutton(self.frameb, text = 'A.'+str(self.que4[2]), variable = self.que1_anwser, value = str(self.que4[2]),  tristatevalue = 0).grid(row =2 , column = 1)
		B = Radiobutton(self.frameb, text = 'B.'+str(self.que4[3]), variable =self.que1_anwser,value = str(self.que4[3]), tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C.'+str(self.que4[4]), variable =self.que1_anwser, value = str(self.que4[4]), tristatevalue = 0).grid(row =4 , column = 1)
		D = Radiobutton(self.frameb, text = 'D.'+str(self.que4[5]), variable = self.que1_anwser,  value = str(self.que4[5]),tristatevalue = 0).grid(row =5 , column = 1)
		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = '#57163d', fg = 'white', bd = 2, text = '>>>', command =self.question5)
		self.start_now.grid(row = 5, column= 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = '#57163d', fg = 'white', bd = 2, text = '<<<',command =self.question3)
		self.start_now.grid(row = 5, column= 0)
		self.frameb.pack()

	def question5(self):
		self.ans4 = self.que4_anwser.get()
		self.frameb.destroy()
		self.frameb= Frame(self.root)
		self.q_lbn = Label(self.frameb, text ='5.' +str(self.que5[1]), 
			font = ('arial', 12, 'bold')).grid(columnspan = 3)
		self.que5_anwser= StringVar()

		A = Radiobutton(self.frameb, text = 'A.'+str(self.que5[2]), variable = self.que1_anwser, value = str(self.que5[2]),  tristatevalue = 0).grid(row =2 , column = 1)
		B = Radiobutton(self.frameb, text = 'B.'+str(self.que5[3]), variable =self.que1_anwser,value = str(self.que5[3]), tristatevalue = 0).grid(row =3 , column = 1)
		C= Radiobutton(self.frameb, text = 'C.'+str(self.que5[4]), variable =self.que1_anwser, value = str(self.que5[4]), tristatevalue = 0).grid(row =4 , column = 1)
		D = Radiobutton(self.frameb, text = 'D.'+str(self.que5[5]), variable = self.que1_anwser,  value = str(self.que5[5]),tristatevalue = 0).grid(row =5 , column = 1)
		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = '#57163d', fg = 'white', bd = 2, text = '>>>', command =self.finalScore)
		self.start_now.grid(row = 5, column= 3)

		self.start_now = Button(self.frameb, font = ('arial', 10, 'bold'), bg = '#57163d', fg = 'white', bd = 2, text = '<<<',command= self.question4)
		self.start_now.grid(row = 5, column= 0)
		self.frameb.pack()

	def finalScore(self):
		self.ans5 = self.que5_anwser.get()
		mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'CBTApp_db')
		mycursor = mydb.cursor()
		self.frameb.destroy()
		self.frameb= Frame(self.root)

		answer = [self.ans1, self.ans2, self.ans3,self.ans4, self.ans5]
		real_answers =[self.que1[6], self.que2[6], self.que3[6], self.que4[6], self.que5[6]]
		5

		for a in answer:
			if real_answers[0] == answer[0]:
				self.score += 1
				self.percentage +=20
			elif real_answers[1] == answer[1]:
				self.score += 1
				self.percentage +=20
			elif real_answers[2] == answer[2]:
				self.score += 1
				self.percentage +=20
			elif real_answers[3] == answer[3]:
				self.score += 1
				self.percentage +=20
			elif real_answers[4] == answer[4]:
				self.score += 1
				self.percentage +=20
			else:
				pass

		#to sore into the database
		if self.user_name== self.user_ver:
			print('You already particpated in this exam')
			
		else:
			myquery = ("INSERT INTO student_results(Username, Matric_id, Score , Percentage)  VALUES('%s', '%s',\
		         '%s', '%s')" %(self.user_name, self.matric_no, self.score, self.percentage))
			mycursor.execute(myquery)
			mydb.commit()
			if mycursor.rowcount ==1:
				print('uploaded succesfully')
				self.checkScore()
			else:
				print('Message', 'Uploading failed')

		self.frameb.pack()

	def checkScore(self):
		mydb = mysql.connector.connect(host ="localhost", user ='root', passwd ='', database = 'CBTApp_db')
		mycursor = mydb.cursor()

		query5 = "SELECT Username, Score , Percentage FROM student_results WHERE Username = %s and Matric_id = %s"
		value = (self.user_name, self.matric_no)
		mycursor.execute(query5, value)
		std_score= mycursor.fetchone()
		print(std_score[1])
		self.user_ver = std_score[0]
		self.score1 = std_score[1]
		self.percentage1 = std_score[2]
		print(self.user_ver)

		self.frameb.destroy()
		self.frameb= Frame(self.root)
		self.first_lbn = Label(self.frameb, text = 'Hey! '+self.user_name +''+'Your Score '+str(self.score1), 
		font = ('arial', 12, 'bold')).grid(columnspan = 3)
		self.first_lbn = Label(self.frameb, text = 'your Overall percentage is '+str(self.percentage1)+'%', 
		font = ('arial', 12, 'bold')).grid(columnspan = 3)

		self.studenPanel_btn = Button(self.frameb, text = 'Student Panel', bd = 5, font = ('arial', 8, 'bold'),
			bg= '#57163d', fg='white',activebackground = '#de1d3d', command=self.quizPage).grid(row = 4,column = 0)
		self.frameb.pack()


app = CbtApp()
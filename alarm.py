from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from datetime import datetime
import datetime as dt
from playsound import playsound
import os
import time
from datetime import date

class Myalarm:
	def __init__(self):
		self.root = Tk()
		self.root.geometry('300x300')
		self.root.title('Alarm Clock Timer')
		self.root.config(bg = '#283145')

		self.firstlable = Label(self.root, font = ( 'Times New Roman', 14,'bold' ), fg= 'white',bg = '#283145', text = 'Please Kindly Set Your ALARM Now!')
		self.firstlable.grid(columnspan = 7)
	
		self.hours = Label(self.root, font = ( 'arial', 14 ), fg= 'white',bg = '#283145',  text = 'Hours')
		self.hours.grid(row = 1, column = 0)
		self.hour_en = StringVar()
		val1 = [1,2,3,4,5,6,7,8,9,10,12,13]
		self.alarm_hour = ttk.Combobox(self.root, font = (  'arial',8, 'bold' ), textvariable = self.hour_en, values = val1)
		self.alarm_hour.grid(row = 1, column = 2)
		
		self.minutes = Label(self.root, font = ( 'arial', 14 ),bg = '#283145',fg= 'white', text = 'Minutes')
		self.minutes.grid(row = 2, column = 0)
		self.min_en = StringVar()
		val2 = [1,2,3,4,5,6,7,8,9,10,15,20,25,30,35,40,45,50,55,60]
		self.alarm_min = ttk.Combobox(self.root, font = (  'arial',8, 'bold' ), textvariable = self.min_en, values = val2)
		self.alarm_min.grid(row = 2, column = 2)

		self.sec = Label(self.root, font = ( 'arial', 14 ), fg= 'white',bg = '#283145', text = 'Seconds')
		self.sec.grid(row = 3, column = 0)
		self.sec_en  = StringVar()
		val3 = [1,2,3,4,5,6,7,8,9,10,15,20,25,30,35,40,45,50,55,60]
		self.alarm_sec = ttk.Combobox(self.root, font = (  'arial',8, 'bold' ), textvariable = self.sec_en, values = val3)
		self.alarm_sec.grid(row = 3, column = 2)


		self.ampm = Label(self.root, font = ( 'arial', 14 ), fg= 'white',bg = '#283145', text = 'Med')
		self.ampm.grid(row = 4, column = 0)
		self.ampm_en  = StringVar()
		self.alarm_ampm = ttk.Combobox(self.root, font = (  'arial',8, 'bold' ), textvariable = self.ampm_en, values = ['am', 'pm'])
		self.alarm_ampm.grid(row = 4, column = 2)


		self.Time_set = Button(self.root, font = (  'arial', 8, 'bold' ), bg = 'black', fg= 'white',  pady = 5, bd = 5, text = 'Set Alarm', command = self.setting)
		self.Time_set.grid(row = 5, column = 2)

		self.display = Text(self.root, height = 5, width = 30, font = (  'arial',8, 'bold' ), bg = 'pink')
		self.display.grid(row = 6, column = 2)
		self.root.mainloop()


	def setting(self):
		hour = self.hour_en.get()
		minute = self.min_en.get()
		second = self.sec_en.get()
		ampm = self.ampm_en.get()

		if (hour.isnumeric() and minute.isnumeric() and second.isnumeric() and ((ampm == 'am') or (ampm =='pm')) ==True):
			showinfo('Message', 'Set Successfully')
			if ampm == 'pm':
				hour = int(hour) + 12
			
			hour = int(hour)
			minute = int(minute)
			second = int(second)

			present_time = datetime.now()
			today  = date.today()
			today = str(today)
			real_today = today.split('-')
			year = int(real_today[0])
			month= int(real_today[1])
			day = int(real_today[2])

			alarm_Set = datetime(year,month,day,hour, minute, second)
			timediff = alarm_Set - present_time
			showinfo('Time left', timediff)
			print(alarm_Set)

			second_left = dt.timedelta.total_seconds(timediff)
			showinfo('the seconds left', second_left)

			while (present_time + timediff) == datetime.now():
				playsound('atmsound.mp3')
				self.display.insert('1.0', 'I want to get my bath')
				
			else:
				pass
				

Alarm_clock = Myalarm()
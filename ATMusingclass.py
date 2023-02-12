import random
import sys
class Machine:
	def __init__(self):
		self.accountnumber = random.randrange(2342651676, 8797656765)
		self.account_name = input('Enter your account name>>>')
		self.phone_num = input('Enter your phone number>>>')
		self.home_address = ('Enter your account address')
		self.Email = input('Please enter your email address')
		self.account_pin = input('Please create your four digit PIN to complete your account creation')
		self.confirm_pin = input('please confirm your pin>>')
		if self.account_pin == self.confirm_pin:
		    print('You have succesfully created an account with OVB and your account number is' +' ' + str(self.accountnumber))
		print('Dear', self.account_name, 'Thank you for creating account with us' )
		print('You have to deposit before you can perform any transactionwith OVB BANK ')
		self.deposit_ammount = input('Enter your deposit ammount>>>')
		print('you have succesfully deposit ', self.deposit_ammount )

	def login(self):
		print('Welcome,', self.account_name, 'Please enter your four digit Pin to login')
		self.login = input('>>>>')
		if self.login == self.confirm_pin:
			print('Welcome!! Please kindly choose your transaction')
			print('1. Balance enquiry\n2. Withdraw money\n3. Change your PIN\n4. Send money\n5. quit\n')

	def account_balance(self):
		print('Do you want to check you Account balance?')
		print('1. Yes\n2. No\n')
		self.bal_check = input('>>')
		if self.bal_check == '1':
			print('Your account balance is', (self.deposit_ammount))
			print('Thanks for banking with us')

	def withdraw(self):
		print('Select your account type')
		print('1. Saving account')
		print('2. Current account')
		self.acct_type = input('>>>')
		if self.acct_type == '2' or '1':
			print('Select the amount you want to withdraw')
			print('1000\n5000\n10,000\n20,000\n')
			self.with_money = (input('>>>'))
			if int(self.with_money) < int(self.deposit_ammount):
				self.new_balance = int(self.deposit_ammount) - int(self.with_money)
				print('Wait to take your cash!!')
				print('Your new balance is' +' '+ str(self.new_balance))
				print('Thanks for banking with us')	
			else:
				print('You have enter invalid amount \nthe problem might arise due to the insufficient balance' )

	def Pin_change(self):
		print('Enter your current PIN')
		self.old_pin = input('>>>')
		if self.old_pin == self.account_pin:
			print('Confirm!! Enter your new PIN')
			self.new_pin = input('>>>')
			if self.new_pin <= str(9999):
				print('Confirm your new PIN')
				self.confirm_pin = input('>>>')
				if self.confirm_pin == self.new_pin:
					print('YOUR PIN HAS BEEN CHANGE SUCCESFULLY')
					print('Thank for banking with us')
				else:
					print('PIN dont match')
					print('Please try AGAIN')

	def send_money(self):
		print('Enter the Beneficiary account number:')
		self.tran_acct = input('>>>')
		print('Enter amount')
		self.tran_amount = input('>>>')
		if int(self.tran_amount) <= (100000):
			print('Please kindly choose the Beneficiary bank: 1. GTB\n 2.First bank\n3. Wema Bank\n4. FCMB\n5. Polariz Bank\n')
			self.tran_bank = input('>>>')
			self.Bankname = [1,2,3,4,5]
			if self.tran_bank in str(self.Bankname):
				print('The Beneficiary account name is XXXXXXXXXXXX')
				print('Please kindly enter your PIN to send:')
				self.tran_pin = input('>>>')
				if self.tran_pin == self.account_pin:
					self.Update_bal = int(self.deposit_ammount) - int(self.tran_amount)
					print('The transaction has been sent completely, \nYour New Account balance is'+' '+  str(self.Update_bal))
					print('Thanks for banking with us')	
				else:
					print('Invalid PIN')
			else:
				print('Invalid! Please try again')       
		else:
			print('Invalid! Please try again')


	def quit(self):
		print('1. Yes\n2. No\n')
		self.quit_1 = input('Press Yes to quit>>>')
		if self.quit_1 == '1':
			print('Quit!!')
			sys.exit()
		else:
			print('Choose any transaction please>>')



def trans_page():
		print('\t\t\t\t\t\tPlease kindly login to perform transaction' )
		Atm.login()
		print('Please Kindly choose your transaction choice')
		transaction = input('>>>')
		if transaction == '1':
			Atm.account_balance()
		elif transaction == '2':
			Atm.withdraw()
		elif transaction == '3':
			Atm.Pin_change()
		elif transaction == '4':
			Atm.send_money()
		elif transaction == '5':
			Atm.quit()
		trans_page()


print('\t\t\t\t\t\tWELCOME TO OLAHINDY VETO BANK(OVB)')
print('1. Register\n 2. login\n')
choice = input('>>>>')
if choice == '1':
	Atm = Machine()
	trans_page()
if choice == '2':
	try:
		trans_page()
	except:
		print('Please kindy Register first')
		Atm = Machine()
		trans_page()






	
	

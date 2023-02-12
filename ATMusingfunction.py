import random
import sys
accountnumber = random.randrange(2342651676, 8797656765)
print('WELCOME TO OLAHINDY VETO BANK(OVB)')
print('1. Register\n 2. login\n 3. Quit\n')
balance = 100000
pin = '1234'


#all funntion declaration
def login():
	print('Choose your transaction')
	print('1. Balance enquiry\n2. Withdraw money\n3. Change your PIN\n4. Send money\n5. quit\n')



def acctbalance():
	print('Do you want to check you Account balance?')
	print('1. Yes\n2. No\n')
	bal_check = input()
	if bal_check == '1':
		print('Your account balance is' + ' '+ str(balance))
		print('Thanks for banking with us')

	trans_page()


def withdraw():
	print('Select your account type')
	print('1. Saving account')
	print('2. Current account')
	acct_type = input('>>>')
	if acct_type == '2' or '1':
		print('Select the amount you want to withdraw')
		print('1000\n5000\n10,000\n20,000\n')
		With_money = (input('>>>'))
		if int(With_money) < balance:
			newbalance = (balance) - int(With_money)
			print('Wait to take your cash!!')
			print('Your new balance is' +' '+ str(newbalance))
			print('Thanks for banking with us')	
		else:
			print('You have enter invalid amount \nthe problem might arise due to the insufficient balance' )
	trans_page()
	

def PIN_change():
	print('Enter your current PIN')
	old_pin = input('>>>')
	if old_pin == str(pin):
		print('Confirm!! Enter your new PIN')
		new_pin = input('>>>')
		if new_pin <= str(9999):
			print('Confirm your new PIN')
			confirm_pin = input('>>>')
			if confirm_pin == new_pin:
				print('YOUR PIN HAS BEEN CHANGE SUCCESFULLY')
				print('Thank for banking with us')
			else:
				print('PIN dont match')
				print('Please try AGAIN')
	trans_page()

def sendmoney():
	print('Enter the Beneficiary account number:')
	tran_acct = input('>>>')
	print('Enter amount')
	tran_amount = input('>>>')
	if int(tran_amount) <= (100000):
		print('Please kindly choose the Beneficiary bank: 1. GTB\n 2.First bank\n3. Wema Bank\n4. FCMB\n5. Polariz Bank\n')
		tran_bank = input('>>>')
		Bankname = [1,2,3,4,5]
		if tran_bank in str(Bankname):
			print('The Beneficiary account name is TAIWO, Olaoluwa Johnson, GTB.')
			print('Please kindly enter your PIN to send:')
			tran_pin = input('>>>')
			if tran_pin == str(pin):
				Update_bal = int(balance) - int(tran_amount)
				print('The transaction has been sent completely, \nYour New Account balance is'+' '+  str(Update_bal))
				print('Thanks for banking with us')	
			else:
				print('Invalid PIN')
		else:
			print('Invalid! Please try again')       
	else:
		print('Invalid! Please try again')
		
	trans_page()


def quit():
	print('1. Yes\n2. No\n')
	quit_1 = input('Press Yes to quit>>>')
	if quit_1 == 'Yes':
		print('Quit!!')
		sys.exit()
	else:
		print('Choose any transaction please>>')
	      

def trans_page():
	print('\t\t\t\t\t\tPlease kindly login to perform transaction' )
	users = input('Enter your PIN:>>>')
	if users == str(1234):
		login()
		transaction = input('>>>>')
		if transaction == '1':
			acctbalance()
		elif transaction == '2':
			withdraw()
		elif transaction == '3':
			PIN_change()
		elif transaction == '4':
			sendmoney()
		elif transaction == '5':
			quit()
		else:
			print('Please kindly login to have another another transaction')
			trans_page()

User = input('Enter your choice')
if User == '1':
	Account_name = input('Enter your account name>>>')
	phone_num = input('Enter your phone number>>>')
	home_address = ('Enter your account address')
	Email = input('Please enter your email address')
	Account_pin = input('Please create your four digit PIN to complete your account creation')
	confirm_pin = input('please confirm your pin>>')
	if Account_pin == confirm_pin:
	    print('You have succesfully creat an account with OVB and your account number is' +' ' + str(accountnumber))
	    trans_page()

elif User == '2':
	trans_page()
elif User == '3':
	quit()
    







		

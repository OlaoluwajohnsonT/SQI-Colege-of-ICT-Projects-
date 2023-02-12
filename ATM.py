pin = 1234
balance = 50000
accountnumber = '0169193044'
print('\t\t\t\t\tMOBILE BANKING SYSTEM')
print('\t\t\tWelcome to Gurantee Trust Bank')
print('Print enter your PIN to Continue')


def login():
	Users = input('>>>')
	if Users == str(pin):
		print('Choose your transaction')
		print('1. Balance enquiry\n2. Withdraw money\n3. Change your PIN\n4. Send money\n5. quit\n')

	else:
		print('Invalid Pin!! Please insert your PIN again')
		login()

def balance_enquiry():
	if transaction == '1':
		print('Do you want to check you Account balance?')
		print('1. Yes\n2. No\n')
		bal_check = input()
		if bal_check == '1':
			print('Your account balance is' + ' '+ str(balance))
			print('Thanks for banking with us')
		else:
			print('Please kindly login to have another another transaction')
	login() 

def withdraw_money():
	if transaction == '2':
		print('Select your account type')
		print('1. Saving account')
		print('2. Current account')
		acct_type = input('>>>')
		if acct_type == '2' or '1':
			print('Select the amount you want to withdraw')
			print('1000\n5000\n10,000\n20,000\n')
			With_money = input('>>>')
			amount = [1000 , 5000, 10000, 20000]
			if With_money in str(amount):
				withdrawermoney = With_money
				newbalance = balance - int(withdrawermoney)
				print('Wait to take your cash!!')
				print('Your new balance is' +' '+ str(newbalance))
				print('Thanks for banking with us')	
			else:
				print('You enter Invalid amount')
				print('Please kindly login to have another another transaction')		
	login()
			
		    
								
				

def pin_change():
	if transaction == '3':
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
					print('Please kindly login to have another another transaction')
	login()

def sendmoney():
	if transaction == '4':
		print('Enter the Beneficiary account number:')
		tran_acct = input('>>>')
		if tran_acct == accountnumber:
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
					if tran_pin <= str(PIN):
						print('The transaction has been sent completely')
						print('Thanks for banking with us')	
						login()
					else:
						print('Invalid PIN')
						login()
				else:
					print('Invalid! Please try again')       
		else:
			print('Invalid! Please try again')
	login()
			

def quit():
	if tran == "5":
		print('1. Yes\n2. No\n')
		quit_1 = input('Press Yes to quit>>>')
		if quit_1 == 'Yes':
			print('Quit!!')
		else:
		    print('Choose any transaction please>>')
	login()	
		 

login()
transaction = input('>>>>')
if transaction == '1':
	balance_enquiry()
elif transaction == '2':
	withdraw_money()
elif transaction == '3':
	pin_change()
elif transaction == '4':
	sendmoney()
elif transaction == '5':
	quit()
else:
	print('Invalid Input!! Please kindly login again to perform another transaction')
	login()











''''transaction = ['1. Balance enquiry','2. Withdraw money','3. Deposit','4. Change your PIN','5. Send money','6. quit']
Amount = 100000
balance = '100000'
PIN = 1111
newpin = 9999
accountnumber = '0169193044'
print('\t\t\t\t\tMOBILE BANKING SYSTEM')
print('\t\t\tWelcome to Gurantee Trust Bank')
print('Print enter your PIN to Continue')
Users = input('>>>>')
if Users == str(PIN):
	print('Choose your transaction')
	print('1. Balance enquiry\n2. Withdraw money\n3. Change your PIN\n4. Send money\n5. quit\n')
	tran = input('>>>>')
	if tran == 'Balance enquiry':
		print('Do you want to check you Account balance?')
		print('Yes\nNo\n')
		bal_check = input()
		if bal_check == 'Yes':
			print('Your account balance is' + ' '+ balance)
		else:
			print('Your request has been cancelled')
	elif tran == 'Withdraw money':
		print('Select your account type')
		print('1. Saving account')
		print('2. Current account')
		acct_type = input('>>>')
		if acct_type == 'Saving account' or 'Current account':
			print('1000\n5000\n10,000\n20,000\n')
			With_money = input('>>>')
			if with_money == '1000' or '5000' or '10,000' or '20,000':
				print('Wait to take your cash!!')
				print('Thanks for banking with us')
			else:
				print('You cant withdraw above 20,000')
	elif tran == 'Change your PIN':
		print('Enter your current PIN')
		old_pin = input('>>>')
		if old_pin == str(PIN):
			print('Confirm!! Enter your new PIN')
			new_pin = input('>>>')
			if new_pin <= str(newpin):
				print('Confirm your new PIN')
				confirm_pin = input('>>>')
				if confirm_pin == new_pin:
					print('YOUR PIN HAS BEEN CHANGE SUCCESFULLY')
					print('Thank for banking with us')
				else:
					print('PIN dont match')	
		else:
			print('Wrong PIN! Enter again')
	elif tran == 'Send money':
		print('Enter the Beneficiary account number:')
		tran_acct = input('>>>')
		if tran_acct == accountnumber:
			print('Enter amount')
			tran_amount = input('>>>')
			if int(tran_amount) <= int(Amount):
				print('Please kindly choose the Beneficiary bank:     1. GTB\n2. First bank\n3. Wema Bank\n4. FCMB\n5. Polariz Bank\n')
				tran_bank = input('>>>')
				if tran_bank == 'GTB' or 'First bank' or 'Wema Bank' or 'FCMB' or 'Polariz Bank':
					print('The Beneficiary account name is TAIWO, Olaoluwa Johnson, GTB.')
					print('Please kindly enter your PIN to send:')
					tran_pin = input('>>>')
					if tran_pin <= str(PIN):
						print('The transaction has been sent completely')
						print('Thanks for banking with us')	
					else:
						print('Invalid PIN')
	elif tran == "Quit":
			quit_1 = input('Press Yes to quit>>>')
			if quit_1 == 'Yes':
				print('Quit!!')
			else:
				print('Choose any transaction please>>')
	else:
		print('Please kindly take your Card')'''


	    	

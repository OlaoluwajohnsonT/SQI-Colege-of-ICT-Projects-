Questions = ['1. list of the following is a country?', '2. list of the following is a football club?', '3. list of the following is girl name', '4. list of the following is nageria state',
'5. list of the following is use for fitness?', '6. which of the follwing is an aphabeth?', '7. whats the name of arsenal coach?', '8. whats the name of jesus mother', '9. jesus died at what?',
'10. example of the name of a house is?'
]
Options = list(('A. osun B. oyo C. ibadan D. Nigeria', 'A. Messi B. Arsenal C. Grizman D. omolola club', 'A. kunle B. BODE C. YEMI D. james',
	'A. Brazil state B. oyo state C. Europe state D. Ibadan state', 'A. Razor B. treadmill C. blade D. none of the above',
	'A. & B. $ c. B D. ^', 'A. monreal B. Arteta C. Ebening D. olaoluwa', 'A. sola B. ade C. Mary D. yemi', 'A. 40 B. 87 C. 33 D. 1200',
     'A. drug B. guy C. bungalow D. none'))
Answers = ['D', 'B', 'C', 'B' , 'B', 'C', 'B', 'C', 'C', 'C']
ind = 0
score = 0
final =''
for que in Questions:
	print(que)
	print(Options[ind])
	users = input('Your Answers:')
	if Answers[ind].lower() == users.lower():
		score += 5
		print('You pass')
	else:
		print('Miss')
	ind += 1
else:
	print('You score'' '+ str(score))
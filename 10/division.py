while 0:
	first_number = raw_input('input first number: ')
	if first_number == 'q':
		break
	second_numer = raw_input('input second number: ')
	if second_numer == 'q':
		break
	try:
		answer = int(first_number) / int(second_numer)
	except ZeroDivisionError:
		print 'you can not divide by 0'
	else:
		print 'answer: '+ str(answer)
		
		
file_name = 'alice.txt'

def count_words(file_name):
	try:
		with open(file_name) as file_object:
			content = file_object.read()
	except IOError:
		print 'can not find file'
	else:
		#print content
		words = content.split()
		num_words = len(words)
		return num_words

print count_words(file_name)

file_names = ['alice.txt','pi_digits.txt','test.txt','fdf']

for file_name in file_names:
	print count_words(file_name)

from name_function import get_formatted_name

print 'enter "q" at any time to quit.'

while True:
	first = raw_input('please give me a first name: ')
	if first == 'q':
		break
	last = raw_input('please input the last name: ')
	if last == 'q':
		break
	
	formatted_name = get_formatted_name(first, last)
	print 'neatly formatted name: ' + formatted_name + '!'
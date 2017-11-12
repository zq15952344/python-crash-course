print 'input number, then i will show you it is even or odd'
print 'input q for quit'

'''while 1:
	count = raw_input()
	if count == 'q' or count == '':
		break
	elif int(count) % 2 == 0:
		print str(count) + ' ' + 'is even'
	else:
		print str(count) + ' ' + 'is odd'
'''


def user():
	usesr = {}
	while 1:
		first_name = raw_input('input first name: ')
		last_name = raw_input('input last name: ')
		
		if first_name == 'q' or last_name == '':
			break
		else:
			usesr[first_name] = last_name
	
	print usesr


def prize_order():
	order_all = {}
	active_table = True
	active_order = True
	while active_table:
		table_no = raw_input('input table nubmer: ')
		orders = []
		active_order = True
		if table_no == 'q':
			active_table = False
		else:
			while active_order and active_table:
				order = raw_input('input order: ')
				
				if order == 'e':
					active_order = False
				else:
					orders.append(order)
					order_all[table_no] = orders
	
	print order_all


def make_shirt(size='big', sentence='hello world'):
	print 'the t shirt size is: ' + size
	print 'the print sentence is: ' + sentence
	make_shirt('big', 'hello world')
	make_shirt()


def format_name(first_name, middle_name='', last_name=''):
	if middle_name == '':
		full_name = first_name + ' ' + last_name
	else:
		full_name = first_name + '   ' + middle_name + ' ' + last_name
	return full_name.title()


full_name = format_name('tom', 'fr', 'cat')
print full_name



def make_pizza(size,*toppings):
	print(toppings)
	print 'make ' + str(size) + 'inch pizze and topping as below:'
	for topping in toppings:
		print topping
make_pizza(12,'aa','b','c')
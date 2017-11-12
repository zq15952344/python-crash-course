def confrim_func(unconfirmed_users, confirmed_users):
	while unconfirmed_users:
		current_user = unconfirmed_users.pop()
		confirmed_users.append(current_user)
	print unconfirmed_users
	print confirmed_users

unconfirmed_users = ['tom', 'jack', 'james']
confirmed_users = []
print unconfirmed_users
print confirmed_users
confrim_func(unconfirmed_users, confirmed_users)
print unconfirmed_users
print confirmed_users

def add(a,b):
	print a + b
	a=0
	b=0

a = 1
b = 1
add(a,b)
print a
print b
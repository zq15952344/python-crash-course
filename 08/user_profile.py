#!/usr/bin/python
# -*- coding: UTF-8 -*-

#import sandwich
from sandwich import make_sandwich
def user_profile(first_name, last_name, address):
	user = {}
	user['first_name'] = first_name
	user['last_name'] = last_name
	user['address'] = address
	return user

myself = user_profile('tom', 'cat', 'address')
print myself

make_sandwich('aa', 'bb')
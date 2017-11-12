#!/usr/bin/python
# -*- coding: UTF-8 -*-

users = {
	'tom': {
		'first':'tom',
		'last': 'aaa',
		'location': 'princetion'
	},
	'hank': {
		'first': 'hank',
		'last': 'bbb',
		'location': 'pairs'
	}
}
print users
for user in users:
	print users[user]
#!/usr/bin/python
# -*- coding: UTF-8 -*-
aliens = []
alien_0 = {'name': 'alien_0', 'color': 'green', 'point': 5, 'speed': 'slow'}
print alien_0['color']
print alien_0['point']

alien_0['color'] = 'red'
print alien_0
aliens.append(alien_0)
print aliens

alien_1 = {'name': 'alien_1',
           'color': 'green',
           'point': 10,
           'speed': 'medium',
           'x_position': 1,
           'y_position': 1}
aliens.append(alien_1)
print aliens
print alien_0.keys()
print alien_0.values()
alien_0['x_position'] = 0
alien_0['y_position'] = 0
print aliens
print alien_0
alien_2 = {'name': 'alien_2',
           'color': 'green',
           'point': 15,
           'speed': 'fast',
           'x_position': 2,
           'y_position': 2}
aliens.append(alien_2)
print 'aliens'

for alien in aliens:
	inscrement = 0
	if alien['speed'] == 'slow':
		inscrement = 1
		alien['x_position'] = alien['x_position'] + inscrement
		alien['y_position'] = alien['y_position'] + inscrement
	elif alien['speed'] == 'medium':
		inscrement = 2
		alien['x_position'] = alien['x_position'] + inscrement
		alien['y_position'] = alien['y_position'] + inscrement
	elif alien['speed'] == 'fast':
		inscrement = 3
		alien['x_position'] = alien['x_position'] + inscrement
		alien['y_position'] = alien['y_position'] + inscrement
	else:
		inscrement = 0
		alien['x_position'] = alien['x_position'] + inscrement
		alien['y_position'] = alien['y_position'] + inscrement
	print alien

del alien_0['point']
print alien_0

for key1, value1 in alien_0.items():
	print key1.title() + ' : ' + str(value1).title()

new_aliens = []
for count in range(30):
	new_alien = {
		'color': 'green',
		'name': 'alien_' + str(count)
	}
	new_aliens.append(new_alien)
print new_aliens[:5]
print len(new_aliens)

favorite_languages = {
	'jen': ['python', 'c', 'oc'],
	'tom': 'python',
	'jack': 'python'
}

for name in sorted(favorite_languages.keys()):
	print name

for value in favorite_languages.values():
	print value
print 'set'

friends = ['tom', 'jack', 'jen']
print favorite_languages

for name in favorite_languages.keys():
	print name
	
	if name in friends:
		print 'Hi {0}, i see your favorite language is {1}!'.format(name.title(), favorite_languages[name])
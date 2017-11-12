from collections import OrderedDict
from random import  randint
favorite_language = OrderedDict()

favorite_language['tom'] = 'python'
favorite_language['jack'] = 'c'
favorite_language['alice'] = 'js'

for name,language in favorite_language.items():
	print name
	print language
	
count = 0
while count <5:
	x = randint(1,6)
	print x
	count = count + 1
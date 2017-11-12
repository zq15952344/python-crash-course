class Dog():
	'''adfasdfas'''
	def __init__(self, name, age):
		'''init'''
		self.name = name
		self.age = age
	
	def sit(self):
		''''''
		print self.name.title() + ' is now sitting'
	
	def roll_over(self):
		''''''
		print self.name.title() + ' rolled over'

my_dog = Dog('nn',5)

print my_dog.name
print my_dog.age
my_dog.sit()
my_dog.roll_over()
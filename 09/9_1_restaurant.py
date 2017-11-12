class restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
	
	def open_restaurant(self):
		print 'restaurant is openning'
		
	def describe_restaurant(self):
		print 'this is ' + self.restaurant_name
		print 'it is ' + self.cuisine_type
	
	def update_number_served(self,number):
		self.number_served = number
	
	def increment_severed(self,number):
		self.number_served = self.number_served + number
		
new_restaurant = restaurant('nnn','mmm')

new_restaurant.open_restaurant()
new_restaurant.describe_restaurant()
new_restaurant.update_number_served(30)
print new_restaurant.number_served

new_restaurant.increment_severed(10)
print new_restaurant.number_served

new1_restaurant = restaurant('dd','ee')
new1_restaurant.open_restaurant()
new1_restaurant.describe_restaurant()
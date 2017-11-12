class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.model + ' ' + self.make
		return long_name
	
	def get_odometer_reading(self):
		return str(self.odometer_reading)
	
	def update_odometer_reading(self, new_odometer_reading):
		self.odometer_reading = new_odometer_reading
	
	def fill_gas_tank(self):
		print 'fill gas'


class Battery():
	def __init__(self, size):
		self.size = size
	
	def describe_battery(self):
		print 'battery size is ' + str(self.size)


class ElectricCar(Car, object):
	def __init__(self, make, model, year):
		super(ElectricCar, self).__init__(make, model, year)
		self.battery_size = 70
		self.battery = Battery(70)
	
	def describe_battery(self):
		print 'battery size: ' + str(self.battery_size)
	
	def fill_gas_tank(self):
		print 'no need gas'

'''
my_car = Car('audi', 'a4', 2016)
print my_car.get_descriptive_name()
print my_car.get_odometer_reading()
my_car.odometer_reading = 23
my_car.update_odometer_reading(24)
print my_car.get_odometer_reading()
print my_car.fill_gas_tank()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print my_tesla.get_descriptive_name()
print my_tesla.describe_battery()
print my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
'''
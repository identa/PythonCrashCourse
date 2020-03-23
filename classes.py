## create and use a class
# create the Dog class

class Dog:
	"""docstring for Dog"""
	def __init__(self, name, age): # self params: required, must come first
		self.name = name
		self.age = age

	def sit(self):
		print(f"{self.name} is now sitting")

	def roll_over(self):
		print(f"{self.age}")

my_dog = Dog('Wille', 6)
print(f"{my_dog.name} and {my_dog.age}") 
my_dog.sit()
my_dog.roll_over()

# create multiple instances
your_dog = Dog('Lucy', 3)
your_dog.sit()

## work with classes and instances
class Car:
	"""docstring for Car"""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year

	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

# set a default value for an attribute
class Car_2:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")

new_car = Car_2('audi', 'a4', 2019)
new_car.read_odometer()

## modify attribute values
# modify an attribute 's value directly
new_car.odometer_reading = 23
new_car.read_odometer()
# modify an attribute 's value through a method (pending)

# increment an attribute's value through a method (pending)

## inheritance
# the init() method for a child class
class Electric(Car):
	"""docstring for Electric"""
	def __init__(self, make, model, year):
		super().__init__(make, model, year)

my_tesla = Electric('tesla', 'model', 2019)
print(my_tesla.get_descriptive_name())		

# define attributes and methods for the child class
class ElectricCar(Car):
	"""docstring for ElectricCar"""
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery_size = 75

	def describe_battery(self):
		print(f"This car has a {self.battery_size}-kWh")

my_tesla = ElectricCar('tesla', 'model', 2020)
print(my_tesla.get_descriptive_name())
		
# override methods from the parent class
# instances as attributes
class Battery:
	"""docstring for ClassName"""
	def __init__(self, battery_size = 75):
		self.battery_size = battery_size

	def describe_battery(self):
		print(f"This car has a {self.battery_size}-kWh")

class ECar(Car):
	"""docstring for ECar"""
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()
	
my_tesla = ECar('tesla', 'model', 2021)
my_tesla.battery.describe_battery()

## import classes (pending)
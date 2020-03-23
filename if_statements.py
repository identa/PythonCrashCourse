# simple example
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())


## check multiple conditions
# use 'and' to check multiple conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

# use 'or' to check multiple conditions
print(age_0 >= 21 or age_1 >= 21)

# check whether a value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
	print(f"{user.title()} is not in the list")

# check that a list is not empty
requested_toppings = []
if requested_toppings:
	for topping in requested_toppings:
		print(f"{topping}")
else:
	print("Empty")


# use multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple']
requested_toppings = ['mushrooms', 'olives', 'green peppers']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("OK det")
	else:
		print("Nope")
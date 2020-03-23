## define a function
def greet_user():
	print("Hello!")

greet_user()

# pass information to a function
def greet_user_2(username):
	print(f"Hello, {username.title()}")

greet_user_2("jesse")

# positional arguments
def describe_pet(animal_type, pet_name):
	print(f"I have a {animal_type} named {pet_name.title()}")

# keyword arguments
describe_pet(animal_type = 'hamster', pet_name = 'harry')
describe_pet(pet_name = 'harry', animal_type = 'hamster')

# default values
def describe_pet_2(pet_name, animal_type = 'dog'):
	print(f"I have a {animal_type} named {pet_name.title()}")

describe_pet_2(pet_name = 'wille')
describe_pet_2('wille') # simplest way
describe_pet_2(pet_name = 'harry', animal_type = 'hamster')

## return values

# return a simple value
def get_name(first_name, last_name):
	full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_name('jimi', 'hendrix')
print(musician)

# make an argument optional
def get_formatted_name(first_name, last_name, middle_name = ''):
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"

	return full_name.title()

musician_2 = get_formatted_name('jimi', 'hendrik')
print(musician_2)

musician_2 = get_formatted_name('jimi', 'hooker', 'hendrik')
print(musician_2)

## pass a list
# modify a list in a function
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# while unprinted_designs:
# 	current_designs = unprinted_designs.pop()
# 	print(f"Printing model: {current_designs}")
# 	completed_models.append(current_designs)

# for completed_model in completed_models:
# 	print(completed_model)

def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_designs = unprinted_designs.pop()
		print(f"Printing model: {current_designs}")
		completed_models.append(current_designs)

def show_completed_models(completed_models):
	for completed_model in completed_models:
		print(completed_model)

# prevent a function from modifying a list
print_models(unprinted_designs[:], completed_models)
print(unprinted_designs)

## pass an arbitrary number of arguments
def make_pizza(*toppings):
	print(toppings)

make_pizza('mushrooms', 'green peppers', 'extra cheese')

# mix positional and arbitrary arguments
def make_pizza(size, *toppings):
	print(f"Make a {size}-inch pizza")

	for topping in toppings:
		print(topping)

make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')

# use arbitrary keyword arguments ( quite important)
def build_profile(first, last, **user_info):
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')
print(user_profile)

## store your functions in modules (pending)
## a simple dictionary
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

## work with dictionaries
## a dictionary is a collection of key-value pairs

# access values in a dictionary
new_points = alien_0['points']
print(new_points)

# add new key-value pairs
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# start with an empty dictionary
alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)


# modify values in a dictionary
aline_2 = {'color': 'green'}
print(f"{aline_2['color']}")

aline_2['color'] = 'yellow'
print(f"{aline_2['color']}")

# move the alien to the right
# detemine how far to move the alien based on its current speed
alien_3 = {'x_position': 0, 'y_position': 5, 'speed': 'medium'}
if alien_3['x_position'] == 'slow':
	x_position = 1
elif alien_3['x_position'] == 'medium':
	x_position = 2
else:
	x_position = 3


alien_3['x_position'] = alien_3['x_position'] + x_position
print(alien_3['x_position'])

# remove key-vaue pairs
del alien_3['x_position']
print(alien_3)

# a dictionary of similar objects
favourite_langs = {
	'jen' : 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

# use get() to acces values
alien_4 = {'color': 'green', 'speed': 'slow'}
# print(alien_4['points']) # error
point_value = alien_4.get('points', 'No value')
print(point_value)

## loop through a dictionary

# loop through all key-value pairs
user_0 = {
	'username':'efermi',
	'first': 'enrico',
	'last': 'fermi'
}

for key, value in user_0.items(): # alternative: for k, v in user_0.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")

# loop through all the keys in a dictionary
for key in user_0.keys():
	print(f"\nKey: {key}")

friends = ['phil', 'sarah']
for name in favourite_langs.keys():
	print(name.title())

	if name in friends:
		language = favourite_langs[name].title()
		print(f"\t{name.title()}, I see you love {language}")

# loop through all values in a dictionary
for lang in favourite_langs.values():
	print(f"\nValue: {lang}")

# use set() for duplicate values
for lang in set(favourite_langs.values()):
	print(lang.title())


## Nesting
# a list of dictionaries
dic_1 = {'color': 'green', 'points': 5}
dic_2 = {'color': 'yellow', 'points': 10}
dic_3 = {'color': 'red', 'points': 15}

dics = [dic_1, dic_2, dic_3]

for dic in dics:
	print(dic)

aliens = []
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

print(len(aliens))

# a list in a dictionary
pizza = {
	'crust' : 'thick',
	'toppings': ['mushrooms', 'extra cheese']
}

for top in pizza['toppings']:
	print(top)

favourite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell']
}

for name, langs in favourite_languages.items():
	for lang in langs:
		print(lang.title())

# a dictionary in a dictionary
users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton'
	},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris'
	}
}

for username, user_info in users.items():
	print(f"{username}")
	full_name = f"{user_info['first']} and {user_info['last']}"
	location = user_info['location']

	print(full_name)
	print(location)


## use a while loopwith lists and dictionaries
# move items from one list to another
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print(f"Verifying user: {current_user.title()}")
	confirmed_users.append(current_user)

# remove all instances of specific values from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)
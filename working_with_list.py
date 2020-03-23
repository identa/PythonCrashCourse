# loop through an entire list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
	# do more work within a for loop
	print(f"{magician.title()}, that was a great trick")

# do something after a for loop
print("Finished!")

## avoid indentation errors
# forget to indent
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print('a')
# indent error
#print(magician)


## make numerical lists
# use the range() func
for value in range(1,5):
	print(value)


# use range() to make a list of numbers
numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1,11):
	square = value ** 2
	squares.append(square)

print(squares)

# simple statistics with a list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(digits))
print(max(digits))
print(sum(digits))

# list comprehensions
squares_2 = [value**2 for value in range(1, 11)]
print(squares_2)

# slice a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# loop through a slice
for player in players[:3]:
	print(player.title())

# copy a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

# rename a list
my_foods_2 = ['pizza', 'falafel', 'carrot cake']
friend_foods_2 = my_foods_2
print(my_foods_2)
print(friend_foods_2)
my_foods_2.append('cannoli')
friend_foods_2.append('ice cream')
print(my_foods_2)
print(friend_foods_2)

# tuples
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 250 # error because tuples are immutable

my_t = (3,) # tuple with one element
print(my_t[0])

# loop through all values in a tuple
for dimension in dimensions:
	print(dimension)


# write over a tuple
dimensions = (400, 100)
for dimension in dimensions:
	print(dimension)
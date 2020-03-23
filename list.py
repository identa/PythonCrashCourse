bicycles = ['trek', 'cannondale', 'redline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[-1]) # access the last item

bicycles.append('star')
print(bicycles)

motocycle = []
motocycle.append('honda')
motocycle.append('yamaha')
print(motocycle)
motocycle.insert(0, 'ducati')
print(motocycle)

del motocycle[1]
print(motocycle)

pop_motocycle = motocycle.pop()
print(pop_motocycle)
print(motocycle)

first_owned = motocycle.pop(0)
print(first_owned)

# remove an item by value
motos = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motos)
motos.remove('ducati')
print(motos)

too_expensive = 'honda'
motos.remove(too_expensive)
print(motos)

## organizing a list

# sorting a list permanently
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse = True)
print(cars)

# sort a list temporarily
original_cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(original_cars))

# print a list in reverse order
original_cars.reverse()
print(original_cars)

# find the length of the list
print(len(original_cars))


## Avoid index error when working with lists

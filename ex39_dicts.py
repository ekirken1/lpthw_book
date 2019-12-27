things = ['a', 'b', 'c', 'd']
print(things[1])

things[1] = 'z'
print(things[1])

print(things)

stuff = {'name': 'Evee', 'age': 39, 'height': 5*12 + 5}
print(stuff['name'])
print(stuff['age'])
stuff['state'] = 'OH'
print(stuff['state'])

stuff[1] = 'woww'
print(stuff)

del stuff[1]

print(stuff)

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Fran',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'NYC'
cities['OR'] = 'Portland'

print('-' * 10)

print("NY State has: ", cities['NY'])
print("OR state has: ", cities['OR'])

print("-" * 10)
print("Michigan's abbrev is: ", states['Michigan'])

print("-" * 10)
print("Michigan has: ", cities[states['Michigan']])

print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}.")

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}.")

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev},")
    print(f"and has the city of {cities[abbrev]}!")

print('-' * 10)
state = states.get('Texas')

if not state:
    print("Sorry, no Texas here (thank goodness...).")

city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is: {city}.")
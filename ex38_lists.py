ten_things = "Apples oranges crows telephone light sugar"

print("Wait, there are not 10 things in that list... Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ['day', 'night', 'song', 'frisbee', 'corn', 'banana', 'girl', 'boy']

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("\nAdding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items in stuff now. ")

print(f"\nThere we go, now there's {len(stuff)} items in stuff: ", stuff)

print("\nLet's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(''.join(stuff))
print(''.join(stuff[3:5]))
from sys import argv

# arguments in the terminal call
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit ctrl+c.")
print("If you do want that, hit return.")

input("What say you?: ")

print(f"Opening {filename}...")
# open file with the write option
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now please write a haiku! ")

line1 = input("5 syllables for line 1: ")
line2 = input("7 syllables for line 2: ")
line3 = input("5 syllables for line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print(f"And finally, we close {filename}.")
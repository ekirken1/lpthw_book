print("hello!")
# comments
# + - / * % < > <= >=
# variables, strings, formats
cow = "cow"
two = 2
print("A ", cow, " says 'moo.'")
print(f"A {cow} says 'moo.'")
three = 3

five = two + three

hilarious = False
joke_eval = "isn't that joke so funny? {}"
print(joke_eval.format(hilarious))

thank = "thank "
you = "you!"
print(thank + you)

formatter = "{} {} {}"
print(formatter.format(3, 9, 3))
print(formatter.format(formatter, formatter, formatter))
print(formatter.format("oh hey", "you're kinda cool", thank))

# \\ \' \a \b \f \n \N{name} \r \t \uxxxx \v \000 \xhh

print("how are you?")
how = input()

from sys import argv
script, hello = argv

print("well, hello, ", hello, "!")

file_again = input("> ")
print(file_again.read())

file.close()
target = open(filename, 'w')
target.truncate()
target.write("\n")

def wazzup(day = ""):
    print("What day is it?")
    day = input()
    return day

wazzup()
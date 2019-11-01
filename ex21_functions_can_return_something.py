def add(a, b):
    print(f"adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"multiplying {a} * {b}")
    return a * b
def divide(a, b):
    print(f"dividing {a} / {b}")
    return a/b

print("let's do some math functions!")

age = add(30, 5)
height = subtract(65, 4)
weight = multiply(30, 6)
iq = divide(360, 2)

print(f"Age: {age}; height: {height}; weight: {weight}; iq: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a riddle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, ". Can you do that by hand?")
# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}; arg2: {arg2}.")

# okay, that *args is actually pointless, we can just do this:
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}; arg2: {arg2}.")

# this just takes one arg
def print_one(arg1):
    print(f"arg1: {arg1}")

# this fn takes no arg
def print_none():
    print("I got nothing...")

print_two("Eve", "Kirk")
print_two_again("Nervous", "Dog")
print_one("happiness")
print_none()
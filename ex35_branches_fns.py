from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take? ")

    choice = input("> ")
    if range(0, 10) in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy. You win!")
        exit(0)
    else:
        dead("You greedy bastard!")
    
def bear_room():
    print("There is a bear here!")
    print("She has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if "honey" in choice:
            dead("The bear looks at you, and then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through the door now.")
            bear_moved = True
        elif "bear" in choice and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I have no idea what that means...")
            print("Try again.")

def cthulhu_room():
    print("Here, you see the great evil Cthulhu.")
    print("He, it, whatever, stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well, that was tasty.")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left...")
    print("Which one do you open?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        print("You stumble around the room until you starve.")

start()
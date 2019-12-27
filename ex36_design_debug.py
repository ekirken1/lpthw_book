from sys import exit

def upstairs():
    sword = False
    again = False
    move = 0

    print("")
    print("As you climb the stairs, you notice smoke pouring from the top of the stairs.")
    print("There's a sword hung up next to the door, which is glowing erratically...")
    print("What's your next move, hero?")

    while sword == False:
        choice = input("> ")

        if "sword" in choice:
            print("\nYou grab the sword!!")
            again = True
            sword = True
        elif "open" in choice and move == 0:
            print("\nYou open the door...to see a witch brewing a glowing soup!!")
            print("You pull out your gun, but she notices you before you can pull the trigger!")
            print("'I'm impervious to bullets - act wisely!'")
            print("")
            print("Nice job, genius - what's your next move?")
            move += 1
        else:
            print("\nPoor decision! The dark energy of the house pushes you out of the house.")
            print("Try again...if you dare!!!")
            exit(0)

    print("The sword calms your nerves...")
    if again:
        print("Confidently, you re-enter the room... The witch jumps back!")
    else:
        print("You open the door... to see a witch brewing a glowing soup!!")
    print("The witch yells, 'EEEE not the sword!!!'")
    print("\nYou throw it at her, and it slices her wrist.")
    print("Poof! She's gone. Congratulations, hero!! You vanquished the poodlenapper.")
        
def downstairs():
    print("\nHmmmm....\nNothing downstairs, so you return to the main floor.")
    start()

def start():
    print("\nYou hear a noise - do you investigate upstairs or downstairs?")

    choice = input("> ")

    if "upstairs" in choice:
        print("\nYou've chosen to go upstairs...best of luck.")
        upstairs()
    elif "downstairs" in choice:
        downstairs()
    else:
        print("Your indecisiveness makes you weak...")
        print("The evil energy of the house pushes you out!!")
        print("........")
        print("Try again if you dare...")

print("You're investigating the mysterious disappearances of poodles...")
print("You enter the abandoned house, believed to be where a suspect squats.")
start()
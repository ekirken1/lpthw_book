# Steps to build something in Python - top down approach
## 1. write/draw the problem
## 2. extract key concepts. idea: write out all the verbs and nouns, and write how they're related. 
## 3. create a class hierarchy and object map for the concepts. 
## 4. code the classes and a test to run them. 
## 5. repeat and refine. 

from sys import exit
from random import randint
from textwrap import dedent

class scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("finished")

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class death(scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a loser.",
        "I have small puppy that's better at this.",
        "You're worse than your dad's jokes."
    ]

    def enter(self):
        print(death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(scene):

    def enter(self):
        print(dedent("""
        The Gothons have invaded your ship and destroyed your entire crew. 
        You are the last surviving member and your last mission is to get
        the neutron destruct bomb from the Weapons Armory, put it in the 
        bridge, and blow the ship up after getting into an escape pod.

        You're running down the central corridor to the Weapons Armory 
        when a Gothon jumps out, red scaly skin, dark grimy teeth, and 
        evil clown costume flowing around his hate-filled body. He's 
        blocking the door to the Armory and about to pull a weapon to blast
        you. What will you do - shoot them, dodge them, or tell them a joke? 
        """))

        action = input("> ")

        if action == "shoot":
            print(dedent("""
                Quick on the draw, you yank out your blaster and fire. 
                ... you miss entirely. But, you've pissed him off more. 
                He blasts you repeatedly. Then eats you. 
                """))
            return "death"

        elif action == "dodge":
            print(dedent("""
                You try to dodge, but you slip and fall...
                right into the Gothon's open mouth!!!
                """))
            return "death"

        elif "joke" in action:
            print(dedent("""
                You tell the Gothon a joke you know. 
                He finds it hilarious. 
                Can't stop laughing. 
                You take the opportunity to shoot him in the head. 
                And you run into the Weapon Armory. 
                """))
            return "laser_weapon_armory"

        else:
            print("DOES NOT COMPUTE!!")
            return "central_corridor"

class LaserWeaponArmory(scene):

    def enter(self):
        print(dedent("""
            Dive rolling into the Armory, you scan the room for more Gothons. 
            You run over to the neutron bomb, and it has a keypad lock on the box. 
            You need the code to get the bomb out, but if you get the code wrong 10x,
            then the lock closes forever. The code is 3 digits. 
            """))

        code = f"{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}"
        guess = input("[keypad] > ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDD!")
            guesses += 1
            guess = input("[keypad] > ")

        if guess == code:
            print(dedent("""
                The container clicks open, and you grab the 
                neutron bomb. You run to the bridge where you must 
                place it in the right spot. 
                """))
            return "the_bridge"

        else:
            print(dedent("""
                The lock buzzes once more, and the mechanism fuses together.
                The Gothons are able to blow up the ship, and

                you die.
                """))
            return "death"

class TheBridge(scene):

    def enter(self):
        print(dedent("""
            Bursting onto the bridge with the bomb, you surprise
            5 Gothons trying to take control of the ship. They
            haven't pulled their weapons out yet because you have
            the bomb. 
            Will you throw or place it? 
            """))

        action = input("> ")

        if "throw" in action:
            print(dedent("""
                You throw the bomb and try to run, but they shoot you
                before you see it go off...
                """))
            return "death"

        elif "place" in action:
                print(dedent("""
                    You slowly place the bomb and run towards an escape pod.
                    """))
                return "escape_pod"
            
        else:
            print("DOES NOT COMPUTE!!")
            return "central_corridor"

class EscapePod(scene):

    def enter(self):
        print(dedent("""
        You're at the escape pods! You need to pick
        which one to take. Some look damaged... 
        Which of the 5 pods do you choose?
        """))

        good_pod = randint(1, 5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
                You jump into Pod {guess} and hit the eject button. 
                The pod escapes then implodes, crushing you to death.
                """))
            return "death"
        else:
            print(dedent("""
                You jump into Pod {guess} and hit the eject button. 
                The pod slides out into space just as the ship 
                explodes! You return back to your home planet - you've won! 
                """))

            return "finished"

class finished(scene):
    
    def enter(self):
        print("You won! Good job!")
        return "finished"

class map(object):

    scenes = {
        "central_corridor": CentralCorridor(),
        "laser_weapon_armory": LaserWeaponArmory(),
        "the_bridge": TheBridge(),
        "escape_pod": EscapePod(),
        "death": death(),
        "finished": finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = map("central_corridor")
a_game = engine(a_map)
a_game.play()

# Programming Process for more advanced users: Bottom Up approach
## 1. hack at a small piece of the problem and barely get it to run
## 2. refine code into more formal class struture with tests
## 3. extract key concepts
## 4. describe in writing what's really going on
## 5. refine code, possibly throw it out
## 6. repeat, move onto another piece of the problem


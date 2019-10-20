def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man, that's enough for a party!")
    print("A party of one...get a blanket. \n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 15)

print("OR, we can use these variables from our script:")
cheeses = 38
cracker_boxes = 61

cheese_and_crackers(cheeses, cracker_boxes)

print("We can even do math inside too:")
cheese_and_crackers(12+23, 71-45)

print("And we can combine the two, variables and math!")
cheese_and_crackers(cheeses +3, cracker_boxes + 100)
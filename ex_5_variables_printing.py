name = 'Captain Kirk'
age = 25
height = 65
height_cm = height * 2.54 # in centimeters = 165.1 cm
print(height_cm)
weight = 140
weight_kg = weight * 0.45 # 63 kg
print(weight_kg)
eyes = 'blue'
teeth = 'white-ish'
hair = 'blonde'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} and {hair}.")
print(f"His teeth are usually {teeth}, depending on what wine he's drinking.")

#this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight}, I get {total}.")
name = 'Zed A. Shaw'
age = 35
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Lets talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# inches to centimeters multiply the length value by 2.54
# pounds to kilograms multiply the given lbs value by 0.45359237

cm = height * 2.54
kg = weight * 0.45359237

print(f"In metric the height is {cm} and the weight is {kg}")

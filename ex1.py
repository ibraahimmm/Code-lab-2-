# Prompting user to input name and age
name = input("Hello, user!\nWhat is your name?\n").title()
age = int(input("What is your age?\n"))

# Printing user details
print(f"It is good to meet you, {name}")
print("The length of your name is:")
print(len(name))
print(f"You will be {age + 1} in a year.")

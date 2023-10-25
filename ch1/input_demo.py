# Input Demo
name = input("Please enter your name: ")
print(f"Hello {name}!")

year = int(input("Please enter the year of your birth: "))

if (year > 2000):
    print(f"{name}, you're too young to be here")
else:
    print(f"Damn, {name}, you're old, bro")

height = float(input("Please enter your heightin cm: "))
print(f"You are {height / 100} meters tall")
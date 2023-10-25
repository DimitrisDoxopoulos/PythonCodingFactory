# bool demo 02 (logical op.)

username = "Bob"

# If the first one is truthy, return it, else return the second one
valid_user = username or "User"

# Checks both for truthy. If both are truthy, return the second one. Else, return the truthy one
valid_user = "User" and username

print("Hello, ", valid_user)
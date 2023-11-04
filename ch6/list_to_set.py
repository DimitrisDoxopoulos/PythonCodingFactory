my_list = [1, 2, 3, 4, 5, 1, 1, 2, 1, 4]

# give me a list of diff elements (each eleent once}

unique_list = []

for item in my_list:
    if not item in unique_list:
        unique_list.append(item)

print(unique_list)

# sets do not have dublicates, so turning the
# list to a set removes them
# we need to present a list, so we turn the
# set to a list again
unique_pythonian_list = list(set(my_list))

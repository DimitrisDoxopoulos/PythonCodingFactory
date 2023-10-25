def name_spacing(number_of_spaces):
    name = input('Please give a name')

    for char in name:
        print(char, end=" " * number_of_spaces)


name_spacing(3)

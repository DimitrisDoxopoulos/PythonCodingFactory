# Crud functions in list - part 2
grades = [1, 4, 8, 3, 9]

# Append
grades.append(10)

# Update
# update takes an index as an arguement
grades[0] = 5

# delete
# Remove takes a value as an arguement
if (4 in grades):
    grades.remove(4)

for grade in grades:
    print(grade, end=': ')
    if (grade < 5): 
        print('Not yet')
    else:
        print('Passed')

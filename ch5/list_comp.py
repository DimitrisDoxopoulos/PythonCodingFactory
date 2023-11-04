grades = [7, 5, 9, 10, 3]

# Map (Transforms teh data of the list)
# upscaled_grades = [grade + 1 for grade in grades]
upscaled_grades = [grade + 1 if grade <= 9 else grade for grade in grades]
print("Final grades:", upscaled_grades)

# Using map()
upscaled_grades2 = list(map(lambda grade: grade + 1 if grade <= 9 else grade, grades))
print("Final grades map():", upscaled_grades2)

# Filter (it is based on Predicate)
passed_grades = [grade for grade in grades if grade >= 5]
# passed_grades = [grade for grade in upscaled_grades if grade >= 5]
print("Passed:", passed_grades)

# Using filter()
passed_grades2 = list(filter(lambda grade: grade >= 5, grades))
print("Passed filter():", passed_grades2)

def enroll_students(*students, min_grade = 50, department = "Computer Science", **kwargs):
  print(f"Min grade: {min_grade}")
  print(f"Department: {department}")
  
  print("\nEnrolled Students")
  for student in students:
    print(f" - {student}")
    
  print("\nAdditional Information")
  for key, value in kwargs.items():
    print(f"{key} : {value}")
  print(" - - - End of Enrollment.")
  
# Enroll Alice and Bob in default department (Computer Science) with min grade
enroll_students("Alice", "Bob")

# Enroll Helen, Carol, Nick with additional keywords arguments
enroll_students("Helen", "Carol", "Nick", academic_year = 2023, semester = "Fall")

# Enroll Dalton with overriden default values for min_grade and department
enroll_students("Dalton", min_grade= 40, department="Theater")

# Enroll Students John and Dave with both overriden defaults and addtion keywargs
enroll_students("John", "Dave", min_grade= 70, department="Maths", academic_year = 2023, 
                semester= "Spring")
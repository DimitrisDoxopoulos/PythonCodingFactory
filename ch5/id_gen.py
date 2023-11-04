def department_id_generator(department):
  """Generate Unique Ids for Students based on department

  Args:
      department (_type_): _description_
  """
  last_id = 0
  
  def generate_id():
    nonlocal last_id
    last_id += 1
    return(f"{department} - {last_id}", last_id)
  
  return generate_id
  
python_id_gen = department_id_generator("Python")
android_id_gen = department_id_generator("Android")

print(python_id_gen()) # Python - 1
print(python_id_gen()) # Python - 2
print(python_id_gen()) # Python - 3
print(python_id_gen()) # Python - 4
print(android_id_gen()) # Android - 1
print(python_id_gen()) # Python - 5
print(android_id_gen()) # Android - 2
print(python_id_gen()) # Python - 6
print(android_id_gen()) # Android - 3
print(android_id_gen()) # Android - 4
print(python_id_gen()) # Python - 7
print(python_id_gen()) # Python - 8
print(android_id_gen()) # Android - 5
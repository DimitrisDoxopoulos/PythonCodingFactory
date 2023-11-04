# Lists

# empty_list = []
# my_list = [1, 2, 3]

# empty_list2 = list()

# my_list2 = list()

# my_list3 = list(x for _ in range(10))

def get_reversed(arr):
  """Prints reversed string

  Args:
      arr (_type_): _description_
  """
  if arr == None:
    return []
  return arr[::-1]

print(f'{get_reversed("Coding Factory")}')
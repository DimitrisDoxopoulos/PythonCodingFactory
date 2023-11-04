def test_args_func(pos_arg1, pos_arg2, opt_arg1 = None, opt_arg2 = None, *args, **kwargs):
  """_summa

  Args:
    positional arguments: pos_arg1, pos_arg2
    option arguments: opt_arg1, opt_arg2
    additional positional arguments (*args)\
    additional keyword arguments (**kwargs)
  """
  
  print("Pos arg1: ", pos_arg1)
  print("Pos arg2: ", pos_arg2)
  print("Opt arg1: ", opt_arg1)
  print("Opt arg2: ", opt_arg2)
  
  # print additional positional arguments
  if args:
    print("Additional Positional Arguments: ")
    for arg in args:
      print(arg)
      
  if kwargs:
    print("Additional Keywords Arguments: ")
    for key, value in kwargs.items():
      print(f"{key} : {value}")


test_args_func("Hello", "CF", opt_arg1= 10, opt_arg2= 100)
print("_________-_________")
test_args_func("Hello", "CF", opt_arg1= 10, keyw_arg1= "Python", keyw_arg2="Android")

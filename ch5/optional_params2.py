def avg(*args):
  # if not args: return 0
  # return sum(args / len(args))
  return sum(args) / len(args) if args else 0

my_ints = [10, 5, 9]
print(avg(*my_ints))
def some_func(count):
  if count >0:
    some_func(count-1)
  print(count)
some_func(5)             

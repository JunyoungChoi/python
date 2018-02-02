def factorial(n):
  if n ==0:
    return 1
  elif n>0:
    return factorial(n-1)*n

print('factorial(5) =',factorial(5))
print('factorial(10) =',factorial(10))

print("계단식")
x=int(input("몇줄? "))
for i in range(0,x):
  for j in range(-1,i):
    if i>=j:
      print("*",end="")
  print("")

print("\n역계단식")
x=int(input("몇줄? "))
for i in range(0,x):
  for j in range(i,x):
    if x>=j:
      print("*",end="")
  print("")

print("\n반 다이아")
x=int(input("몇줄? "))
for i in range(0,x):
  for j in range(0,2*x):
    if ((j-i)<=x-1) and (i+j>=x-1):
      print("*",end="")
    else :
      print(" ",end="")
  print("")

print("\n다이아")
x=int(input("몇줄?(홀수만) "))
for i in range(0,x):
  for j in range(0,x):
    if ((j-i)<=x>>2-1) and (i+j>=x>>2-1) and ((i-j)<=x>>2-1) and ((i+j)<=(x/2)*3-1):
      print("*",end="")
    else :
      print(" ",end="")
  print("")

print("\n빈다이아")
x=int(input("몇줄?(홀수만) "))
for i in range(0,x):
  for j in range(0,x):
    if ((j-i)<=x>>2-1) and (i+j>=x>>2-1) and ((i-j)<=x>>2-1) and ((i+j)<=(x/2)*3-1):
      print(" ",end="")
    else :
      print("*",end="")
  print("")

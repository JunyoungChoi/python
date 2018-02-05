for i in range(0,9):
  for j in range(0,9):
    if ((j-i)<=5-1) and (i+j>=5-1) and ((i-j)<=5-1) and ((i+j)<=4*3):
      print("*",end="")
    else :
      print(" ",end="")
  print("")

f=open("C:\\test.txt",'r')
foods = f.readlines()
for food in foods :
  print(food)
f.close()

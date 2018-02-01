i,k,guguline=0,0,''
for i in range(2,10):
  print("%7s" %("#"+str(i)+"단 #"), end='')

print(guguline)

for i in range(1,10):
  guguline =''
  for j in range(2,10):
    guguline+=str("%2dX%2d=%2d" %(j,i,j*i))
  print("%10s"%guguline)

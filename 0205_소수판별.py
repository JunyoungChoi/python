num=int(input('Enter the number : '))
count=0
for a in range(1,num+1):
  if num %a ==0:
    count+=1
if count == 2:
  print("%d은 소수 입니다." %num)
else:
  print("%d은 소수가 아닙니다." %num)

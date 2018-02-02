def print_readable_bin(a):
  b=[]
  while True:
    b.append(a%2)
    a=a//2
    if a==0 :
      break
  print(b)
  for a in range(len(b)-1,-1,-1):
    if a%4==3:
      print('_',end='')
    print(b[a],end='')
    

num = int(input('숫자를 입력하세요 : '))

print_readable_bin(num)

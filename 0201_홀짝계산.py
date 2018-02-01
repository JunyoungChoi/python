a=int(input("정수를 입력하세요 : "))
if a%2 ==0:
  if(a<100):
    print("100보다 작은 짝수를 입력했군요.")
  elif a==100 : 
    print("100을 입력했군요.")
  else:
    print("100보다 큰 짝수를 입력했군요.")
else:
  if(a<100):
    print("100보다 작은 홀수를 입력했군요.")
  else:
    print("100보다 큰 홀수를 입력했군요.")
  
  

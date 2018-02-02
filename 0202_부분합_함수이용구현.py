def _eval () :
    numStr = input(" *** 수식을 입력하세요 : ")
    answer = eval(numStr)
    print("%s결과는 %5.1f 입니다." %(numStr, answer))

def _plus ():
  answer=0
  num1=int(input("*** 첫번째 숫자를 입력하세요 : "))
  num2=int(input("*** 두번째 숫자를 입력하세요 : "))
  if num1<num2:
    for i in range(num1, num2+1):
      answer+=i
    print("%d+...+%d는 %d입니다." %(num1,num2,answer))
  else :
    for i in range(num1,num2-1,-1):
      answer+=i
    print("%d+...+%d는 %d입니다." %(num1,num2,answer))
    

while 1 :
  select = int(input("1. 수식계산기 2. 두 수 사이 합계 0. 종료 : "))
  if select ==1:
    _eval()
  elif select ==2:
    _plus()
  elif select ==0 :
    print('종료합니다')
    break
  else:
    print("0또는 1 또는 2만 입력해야합니다.")

def calc(v1,op,v2):
  result = 0
  if op == '+':
    result =v1+v2
  elif op == '-':
    result = v1-v2
  elif op == '*' :
    result = v1*v2
  elif op == '/' :
    if v2 == 0:
      return ('나눌 수 없습니다.')
    result = v1/v2
  elif op == '**':
    result = v1**v2
  else :
    print('잘못 입력하셨습니다.')
  return result

print(calc (1,'-',2))
print(calc (1,'/',2))
print(calc (1,'/',0))

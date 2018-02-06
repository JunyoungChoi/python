_진수=int(input('진수(2/8/10/16)를 선택 : '))
num1=list((input('첫번째 수를 입력 : ')))
num2=list((input('두번째 수를 입력 : ')))
oper=input('연산자를 선택해주세요 (&/|/^) : ')
c_num1=0
c_num2=0
b=1
num1.reverse()
num2.reverse()
if _진수 ==2 :
  for a in num1:
    c_num1+=int(a)*b
    b*=2
  b=1
  for a in num2  :
    c_num2+=int(a)*b
    b*=2
elif _진수 ==8:
  for a in num1:
    c_num1+=int(a)*b
    b*=8
  b=1
  for a in num2  :
    c_num2+=int(a)*b
    b*=8
elif _진수 == 16 :
  for a in num1:
    c_num1+=int(a)*b
    b*=16
  b=1
  for a in num2  :
    c_num2+=int(a)*b
    b*=16
elif _진수 != 10:
  print('진수를 제대로 입력하세요')

if oper =='&' : 
  print('두 수의 & 연산 결과')
  print('16진수 => %s' %hex(c_num1&c_num2))
  print('8진수 => %s' %oct(c_num1&c_num2))
  print('10진수 => %d' %(c_num1&c_num2))
  print('2진수 => %s\n' %bin(c_num1&c_num2))

if oper =='|':
  print('두 수의 | 연산 결과')
  print('16진수 => %s' %hex(c_num1|c_num2))
  print('8진수 => %s' %oct(c_num1|c_num2))
  print('10진수 => %d' %(c_num1|c_num2))
  print('2진수 => %s\n' %bin(c_num1|c_num2))

if oper =='^':
  print('두 수의 ^ 연산 결과')
  print('16진수 => %s' %hex(c_num1^c_num2))
  print('8진수 => %s' %oct(c_num1^c_num2))
  print('10진수 => %d' %(c_num1^c_num2))
  print('2진수 => %s\n' %bin(c_num1^c_num2))
        

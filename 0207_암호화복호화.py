import re

_암호=9876541234567

def _암호화(_주민번호):
  a=_주민번호.split('-')
  _주민번호=0
  _주민번호 = int(a[0]+a[1])
  while True:
    r=re.compile('^[a-zA-Z_].*$')
    _저장할파일이름=input('암호화된 주민번호 저장할 파일 이름 : ')
    if r.search(_저장할파일이름) == None:
      print('잘못입력')
      continue
    else:
      break
  a=open(_저장할파일이름,'w')
  str1=_주민번호^_암호
  a.write("%s" %str1)
  a.close()
  return int(_주민번호) ^ _암호

def _복호화():
  while True:
    r=re.compile('^[a-zA-Z_].*$')
    _저장된파일이름=input('암호화된 주민번호 저장된 파일 이름 : ')
    if r.search(_저장된파일이름) == None:
      print('잘못입력')
      continue
    else:
      break
  a=open(_저장된파일이름,'r')
  _주번=a.read()
  _주번=int(_주번)^_암호
  _주번=str(_주번)
  a.close()
  return _주번[:6] +'-'+_주번[6:]

while True:
  _메뉴 = int(input('1. 주민번호입력, 2. 복호화, 3. 종료 '))
  if _메뉴 ==1:
    while True:
      r=re.compile('^[0-9]{6}-[0-9]{7}$')
      str = input("주민번호입력 : ")
      if r.search(str) == None:
             print("잘못입력")
             continue
      else :
             break
    print(_암호화(str))
    continue
  elif _메뉴 ==2:
    print(_복호화())
  elif _메뉴 ==3:
    print('종료합니다')
    break
  else:
    print('제대로 입력하세요')
    continue

import re
list1=[]


while True : 
  data={'id':'','pw':'','한글이름':'','영문이름':'','phonenum':'','e-mail':'','주민번호':'','IP':'','file_name':''}
  r= re.compile('^[a-zA-Z]\w*$')##ID 정규식
  while True :
      str = input("ID입력 : ")
      if r.search(str) == None:
           print("잘못입력")
           continue
      else :
           data['id']=str
           break   

  r= re.compile('^[0-9]+$')##Password 정규식
  while True :
      str = input("Password입력 : ")
      if r.search(str) == None:
           print("잘못입력")
           continue
      else :
           data['pw']=str
           break   
 
  r= re.compile('^[가-힣]+$')##한글이름  정규식
  while True :
      str = input("한글이름입력 : ")
      if r.search(str) == None:
           print("잘못입력")
           continue
      else :
           data['한글이름']=str
           break

  r= re.compile('^[a-zA-Z]+$')##영문이름 정규식
  while True :
      str = input("영문이름입력 : ")
      if r.search(str) == None:
           print("잘못입력")
           continue
      else :
           data['영문이름']=str
           break
  
  r= re.compile('^\d{2,3}-\d{3,4}-\d{4}$')##일반전화번호 정규식  
  while True :
      str = input("일반전화번호입력 : ")
      if r.search(str) == None:
           print("잘못입력")
           continue
      else :
           data['phonenum']=str
           break
  
  r= re.compile('^[a-zA-Z]\w*@\w+$')##e-mail 정규식
  while True :
      str = input("E-mail입력 : ")
      if r.search(str) == None:
           print("잘못입력")
           continue
      else :
           data['e-mail']=str
           break
        
  r= re.compile('^\d{6}-[1-4]\d{6}$')##주민번호 정규식
  while True :
      str = input("주민번호입력 : ")
      if r.search(str) == None:
           print("잘못입력")
           continue
      else :
           data['주민번호']=str
           break

  r= re.compile('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')##ip주소 정규식
  while True :
      str = input("ip주소입력 : ")
      if r.search(str) == None:
           print("잘못입력")
           continue
      else :
           data['IP']=str
           break
          
          
  r= re.compile('\.([:alpha:]*)$')##자기소개서 파일 정규식
  while True :
      str = input("자기소개서 파일입력 : ")
      if r.search(str) == 'txt' or r.search(str) == 'pdf' or r.search(str) == 'hwp' or r.search(str) == 'xls':
           print("잘못입력")
           continue
      else :
           data['file_name']=str
           break
  list1.append(data)
  x=input('그만하려면 N를 누르세요 아니면 아무키나 누르세요 : ')
  if x=='N':
    break
for a in range (0,len(list1)):
  print('--------------------------------------------------------------')
  for c in list(list1[a].keys()):
    print(c,':',list1[a][c])
        
          
          
          
      

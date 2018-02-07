import re
f=open("저장저장.txt",'w')

while True : 
  data={'이름':'','학번':'','주소':'','생년월일':''}
  r= re.compile('^[가-힣]{1,5}$')##이름
  while True :
      str = input("이름 : ")
      if r.search(str) == None:
           print("잘못입력")
           continue
      else :
           data['이름']=str
           break   

  r= re.compile('^[0-9]{9}$')##학번
  while True :
      str = input("학번 : ")
      if r.search(str) == None:
           print("잘못입력")
           continue
      else :
           if int(str[0:4])>=1990 and int(str[0:4])<=2017 and int(str[6:9])!=0:
             data['학번']=str
             break
           print("잘못입력")
           continue
 
  r= re.compile('^[가-힣].*[가-힣]$')##주소
  while True :
      str = input("주소 : ")
      if r.search(str) == None:
           print("잘못입력")
           continue
      else :
           if str[0:2] =='서울' or str[0:2] =='대전' or str[0:2] =='대구' or str[0:2] =='부산' or str[0:2] =='광주' or str[0:2] =='인천' or str[0:2] =='울산' or str[0:2] =='경북' or str[0:2] =='경남' or str[0:2] =='충북' or str[0:2] =='충남' or str[0:2] =='제주' or str[0:2] =='강원' or str[0:2] =='전북' or str[0:2] =='전남' and len(str)<=20:  
             data['주소']=str
             break
           print("잘못입력")
           continue

  r= re.compile('^[0-9]{6}$')##생년월일
  while True :
      str = input("생년월일 : ")
      if r.search(str) == None:
           print("잘못입력")
           continue
      else :
           data['생년월일']=str
           break
  _그만=input('그만하려면 q를 누르세요')
  if _그만 =='q':
    break
f.write('%s, %s ,%s ,%s\n' %(data['이름'],data['학번'],data['주소'],data['생년월일']))
f.close()

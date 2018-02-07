import re
html="""
<html>
	<head>
		<title> test web </title>
	</head>
	<body>
		<p align="center"> text contents 1 </p>
		<p align="right"> text contents 2 </p>
	      	<p align="left"> text contents 3 </p>
		<img src="c:Koala.jpg" width = "500" height = "300">
	</body>
</html>
"""
from bs4 import BeautifulSoup
bs=BeautifulSoup(html)
print(bs.prettify())
print(bs.find("p",align='right'))
print(bs.find_all("p"))
head_tag=bs.find('head')
print(head_tag.find('title'))  # 중첩개념으로 계속 걸러냄

body_tag=bs.find('body')  #body안에를 전부 부름
list1=body_tag.find_all(['p','img'])    # 그 body태그 안에서 p랑 img 태그 가져옴
for tag in list1: 
  print(tag)


tags = bs.find_all(re.compile("^p"))  # 정규식사용가능
print(tags)

print(bs.find_all(align="center")) # 속성값으로도 부를수 있음

print(bs.find_all(text=re.compile('text +')))  # 정규식이용해서찾기

  
tags = bs.find_all(re.compile("^p"),limit=2)  # 2개만 갖고오기
print(tags)

print(body_tag.get_text())  # 태그외에 값을 전부 가져옴
print(body_tag.get_text(strip = True ))  # 태그에있는 데이터값을 가져옴

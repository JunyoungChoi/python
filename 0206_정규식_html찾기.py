import re
_문제="""aaa.html
bbb.html
ccc.xml
ddd.html
1.html
b.hhtml
hihihi.java
itpangpang.txt
ab123456a.js
Good.css
itit.html
ititkkk.htmlggg
hahaha.htmlmlml
cabd_a.html"""

a = re.compile(r"\S*\.html\b")
print(a.findall(_문제))

import re
a=re.compile('\?(.*)')
c=re.compile('https?:[^?]+')
b='http://www.daum.net/abc/top?a=b&c=d'
print(a.findall(b))
print(c.findall(b))

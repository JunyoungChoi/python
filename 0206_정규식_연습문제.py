import re
_문제="""
A : 홍길동은 살아있다.
B : 아냐, 그는 죽었어.

전화번호 : 011-000-0000
전화번호 : 017-111-1111
전화번호 : 010-9999-9999


날짜 : 95년 2월 1일
"""

a=re.compile("\d{3}-\d{3,4}-\d{3,4}")
b=re.compile(r"\b\d{,4}년\s\d{,2}월\s\d{,2}일\b")
c=re.compile(r"\b.*홍길동.*\.")
print(a.findall(_문제))
print(b.findall(_문제))
print(c.findall(_문제))

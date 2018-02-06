import re
_문제 = "홍길동은 파이썬을 매우 잘하고 홍길동은 동에번쩍 서에번쩍하는홍길동은 만능인 홍길동의키는190이며 홍길동나이는&%$$##이다."

r=re.compile("\S*홍길동\S*")
print(r.findall(_문제))
r=re.compile(r"\b\S*홍길동[가-힣]*[0-9]+\S*\b")
print(r.findall(_문제))
r=re.compile(r"\b\S*홍길동[가-힣]*[^ ^0-9^가-힣]+\S*")
print(r.findall(_문제))

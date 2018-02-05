_높이=int(input('높이를 입력하세요(m) : '))
count=0
while _높이>0.00001 :
  _높이/=2
  count+=1
print('공이 튀긴 횟수는',count-1,'회 입니다.')

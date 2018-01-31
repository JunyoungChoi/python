singer = {}

singer['이름'] = '아이오아이'
singer['구성원수']=11
singer['데뷰']='프로듀스101'
singer['대표곡']='픽미픽미픽미업'
for k in list(singer.keys()):
  print('%s --> %s ' %(k,singer[k]))
c=set(singer)
print(c,type(c))

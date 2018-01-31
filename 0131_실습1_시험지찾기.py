list_ex1 = ['risk','issue','test','maintenance','maturity']
list_ex2 = ['security','plan','design','systematic','safety']
list_ex3 = ['maintenance','verification','validation']
test=[list_ex1,list_ex2,list_ex3,'list_ex1','list_ex2','list_ex3']

for a in range (0,3):
  if 'maintenance' in test[a] and len(test[a])>=5:
     print(test[a+3],"사용 가능합니다.")
     answer =a

if a>3 :
  print("사용가능한 시험지가 없습니다.")

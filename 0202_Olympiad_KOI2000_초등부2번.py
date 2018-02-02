import random
_스위치개수 = int(input('스위치 개수 : '))
_스위치번호 = [0 for a in range(0,_스위치개수)]
_스위치상태 = [0 for a in range(0,_스위치개수)]
_학생숫자 = int(input('학생 숫자 : '))
_학생성별 = [0 for a in range(0,_학생숫자)]
for a in range (1,_스위치개수+1):
  _스위치번호[a-1]=a
  _스위치상태[a-1]=random.choice([0,1])
for a in range (1,_학생숫자+1):
  _학생숫자[a-1]=random.choice([1,2])

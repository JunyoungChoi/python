_키=int(input('키 : '))/100
_몸무게=int(input('몸무게 : '))
BMI=_몸무게/_키**2
if BMI <20:
  print('저체중')
elif BMI <=24:
  print('정상체중')
elif BMI <=30:
  print('경도비만')
else:
  print('비만')

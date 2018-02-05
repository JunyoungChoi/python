while True:
  try:
    num=int(input('숫자를 입력하세요 : '))
    if num == 24:
      raise ValueError
  except ValueError:
    print('숫자가 아닙니다')
  else :
    break

while True:
  test = input('정수로 변환할 숫자 입력 : ')
  for i in test:
    if i not in '0123456789':
      raise ValueError('숫자를 입력해"')
  print(int(test))

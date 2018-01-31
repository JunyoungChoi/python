ss=input("아무 글자나 입력해주세요 : ")
if ss.isalnum():
  if ss.isalpha():
    print("입력한 값은 글자입니다.")
  elif ss.isdigit():
    print("입력한 값은 숫자입니다.")
  else:
    print("입력한 값은 글,숫자입니다.")
else:
 print("모르겠습니다.")

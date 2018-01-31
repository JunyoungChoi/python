_입력정수 =input("정수를 입력해주세요 : ")
sum=0
print(len(_입력정수))
for a in range(0,len(_입력정수)):
  sum+=int(_입력정수[a])
print("각 자리수의 합은 %d입니다."%sum)

def my_upper(a):
  for b in range(0,len(a)):
    if ord(a[b]) >= ord('a') and ord(a[b]) <= ord('z'):
      print(chr(ord(a[b])-32),end='')
    else :
      print(a[b],end='')
_소문자모임=input('알파벳을 적어주세요 : ')
my_upper(_소문자모임)

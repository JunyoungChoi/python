money, _500,_100, _50, _10 = 0, 0, 0, 0, 0
money = int(input("교환할 돈 : "))
_500=money//500
money-=_500*500
print("500원짜리 : %d" %(_500))
_100=money//100
money-=_100*100
print("100원짜리 : %d" %(_100))
_50=money//50
money-=_50*50
print("50원짜리 : %d" %(_50))
_10=money//10
money-=_10*10
print("10원짜리 : %d" %(_10))
print("바꾸지못한 돈 : %d" %money)

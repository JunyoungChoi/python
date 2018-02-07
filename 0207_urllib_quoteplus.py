import urllib.parse
def input_query1(): #quoteplus 사용안함
  q=str(input("검색어 입력하세요 : "))
  return "&query=" +q
def input_query2(): #quoteplus 사용
  q=urllib.parse.quote_plus(str(input("검색어 입력하세요 : ")))
  return "&query=" +q

print(input_query1())
print(input_query2())

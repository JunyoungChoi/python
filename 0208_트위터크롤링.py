import tweepy
Consumer_Key='MjXAl85qlUSyVEIxpRSUy0acV'
Consumer_Secret='4Vohtuf4Jde2eebGUL7PS0Odx0yAbUxsgG3ZO9JlX8BzcOasOQ'
Access_Token='961421195584221184-RTXAoM653qRDYCaL69SIGoFepFVHmbY'
Access_Token_Secret='s25Gp1M3wUHi2tXVt6MXrdBRtjUvaCQrdWi5VGX7cU4ge'

auth = tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)

auth.set_access_token(Access_Token,Access_Token_Secret)
api=tweepy.API(auth)

keyword=input('검색어 : ')
result=[]

for i in range(1,3): 
  tweets=api.search(keyword)   # 검색어로 트위터에 검색을 해서 나온 결과값 저장
  for tweet in tweets:
    result.append(tweet)        # 리스트형식으로 result에 저장
print(len(result))
print(type(result[0]))

f=open('tweet.txt','w')               # 쓰기형식으로 파일 오픈
for i in range(0,len(result)):        # result 변수에 저장되있는 keyword에 대한 검색 내용을 파일에 복사, 인코딩 에러가 나면 에러표시
  try:
    f.write(str(result[i])+'\n')
  except UnicodeEncodeError:    # 인코딩에러 날 시 반복문 건너뜀
    print("인코딩 에러입니다.")
    continue
f.close()

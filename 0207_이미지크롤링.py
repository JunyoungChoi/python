import urllib.parse
import urllib.request
import re

def bind_url():
  default_url='https://openapi.naver.com/v1/search/image.xml?'  #이미지형식을 불러옴
  start = '&start=1'            #처음부터 보여줌
  sort = '&sort=sim'    # 관련성으로 정렬
  display = '&display=10'   # 10개를 가져옴
  query='&query='+urllib.parse.quote_plus(str(input('검색어를 입력하세요 : ')))   #한글을 그대로 전송하면 인코딩 오류가 나기때문에 quote_plus로 변환해줌
  full_url=default_url + sort + start + display + query   # url을 만듦
  return full_url

def fetch_contents_from_url():
  url = bind_url()   # bind_ulr함수를 불러옴
  headers={    # 필요한 정보들을 딕셔너리형태로 저
  'Host':'openapi.naver.com',
  'User-Agent':'curl/7.43.0',
  'Accept' : '*/*',
  'Content-Type':'application/xml',
  'X-Naver-Client-Id' : 'Dcztd46KqhdlHN5eQbPX',
  'X-Naver-Client-Secret':'kqqsX6zdfp',
  }
  r=urllib.request.Request(url,headers=headers)  #내 정보를 가지고 네이버로가서 정보를 가져가도되냐고 요청
  m=urllib.request.urlopen(r)  
  html=m.read()   # 읽은 정보를 html에 저장
  return html

def extract_text_in_tags(tags,tagname='title'):
  txt=[]   # 리스트형식으로 선언
  reg="[^<"+tagname+">][^>]+"   # 태그만잘라냄
  #print(reg)
  for tag in tags :
    txt.append(re.search(reg,tag).group())   # txt에 태그값들을 넘겨줌
  return txt

def get_contents_from_html():
  html = fetch_contents_from_url()  #html에 읽어온 정보들을 저장
  title_tags = re.findall("<title>[^<]+</title>",html.decode('utf-8'))  # title 태그들을 전부 찾음
  #print(title_tags)
  link_tags = re.findall("<link>[^<]+</link>",html.decode('utf-8'))  # link 태그들을 전부 찾음
  #print(link_tags)
  titles = extract_text_in_tags(title_tags,tagname='title')  # 읽어온 title 태그 정보중 태그를 제외하고 데이터값만 저
  links = extract_text_in_tags(link_tags,tagname='link')  # 읽어온 link 태그 정보중 태그를 제외하고 데이터값만 저
  f=open("image.html",'w')  # image.html로 파일 쓰기
  f.write('<html><body>')  # image.html파일에 html태그와 body태그를 넣어줌
  for i in range(1,len(titles)):
    f.write('<p>'+titles[i]+'</p>')   # p태그를 이용해 title 태그안에있던 값을 출력
    f.write('<img src='+links[i]+'/>')  # img 태그를 이용해 읽어온 link값을 대입해서 이미지 출력
  f.write('</body></html>')  # image.html파일에 닫는 body태그와 html 태그 추가
  f.close()  # 파일 닫음
  
get_contents_from_html()  #크롤링 시

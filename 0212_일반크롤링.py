import os
import urllib.parse
import urllib.request
import re
import time
import random

from bs4 import BeautifulSoup
#http://movie.naver.com/movie/bi/mi/point.nhn?code=151728

url1 = 'http://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=' #우리가 고른 영화 페이지
url2 = '&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=' #우리가 고른 영화 페이지의 평점이 있는 부분

hdr={  #헤더
    'User-Agent':'Mozilla/5.0(Windows NT 6.3;WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
    'Host':'movie.naver.com',
    'Connection' : 'keep-alive',
    'referer':'http://m.naver.com'
    }

def split_url():
    url = input('url을 입력하세요: ') #url을 입력받는 부분
    code_str = re.search('code=[0-9]*', url).group() #'code=영화번호' 추출
    code = re.search('[0-9]+', code_str).group() #영화번호만 추출

    return code

def fetch_score_result(URL):
    print(URL)
    result = {}
    result_list =[]

    res = urllib.request.Request(URL, headers=hdr) #요청 부분
    response = urllib.request.urlopen(res) #요청 허가가 나면 데이터를 받아오는 부분

    html = response.read() #응답받은 정보를 html에 넣는 부분

    soup = BeautifulSoup(html, 'html.parser') 

    score_result = soup.find('div', class_='score_result').find('ul') #"div class=score_result"인 것을 찾아서 그 안에서 ul태그 찾기
    lis = score_result.find_all('li') #ul 코드 안에 있는 li코드를 모두 찾아라

    for li in lis:
        score = li.find('div', class_='star_score').find('em').get_text() #"div class=star_score"인 것을 찾아서 그 안에서 em태그 찾기(별 개수)

        spectator = li.find('div', class_='score_reple').find('span').get_text() #"div class=score_reple"인 것을 찾아서 그 안에서 span태그 찾기(관람객)
        review = li.find('div', class_='score_reple').find('p').get_text() #"div class=score_reple"인 것을 찾아서 그 안에서 p태그 찾기(평점내용)

        if spectator == '관람객': #spectator가 관람객이면 베스트(BEST)뒤에 '관람객' 글씨 붙이기
            review = review[3: ]

        result['score'] = score #result 딕셔너리 안에 key가 score인 곳에 score(별 개수) 값 넣기
        result['review'] = review #result 딕셔너리 안에 review가 score인 곳에 reviwe(평점내용) 값 넣기

        result_list.append({ #result_list 라는 리스트 안에 별개수, 평점내용 추가
            'score' : score,
            'review': review
            })
    return result_list

def input_save_path(): #파일 저장 경로 입력 
    save_path = str(input("input save path: ")) 
    save_path = save_path.replace('\\','/')
    if not os.path.isdir(os.path.split(save_path)[0]): #입력한 경로가 존재하는지 하지 않는지 판별
        os.mkdir(os.path.split(save_path)[0]) #경로가 없으면 새로 만듬 
    return save_path

def fetch_reviews():
    code = split_url()
    f = open(input_save_path(), 'w', encoding='utf-8') #파일 저장 경로 입력
    page = 1
    while True:
        count = int(input('게시물의 검색 개수를 입력하세요(10단위): ')) #검색 개수 정하기
        if count %10 ==0: #검색 개수의 단위가 10단위인지 확인하는 부분
            break
    l_count = 1
    isLoop = True
    while isLoop:
        URL = url1+code+url2+str(page)  #우리가 고른 영화 페이지 속 네티즌 평점 부분의 페이지 url 
        result_list = fetch_score_result(URL)

        for r in result_list:
            f.write('=='*40+'\n') #영화 평점과 리뷰 내용을 파일에 저장
            f.write('영화 평점: '+r['score']+'\n')
            f.write('리뷰 내용: '+r['review']+'\n')
            f.write('=='*40+'\n')
            l_count +=1  #입력받은 검색개수만큼 반복하여 영화 평점과 리뷰 내용을 불러옴. 
            if l_count > count: #반복횟수가 입력받은 검색개수를 초과하면 break
                isLoop=False
                break
        page +=1 #다음 평점 페이지 불러오기
        if not isLoop or l_count == count: #내가 원하는 개수만큼 불러오면, 더이상 while문이 반복되지 않음
            isLoop = False
            break
        sleepTime = random.randint(4,10)
        time.sleep(sleepTime)
        print(str(sleepTime)+'초 기다렸습니다. ')
    f.close()
fetch_reviews()

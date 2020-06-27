import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('http://www.themood.co.kr/index.html',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

#anchorBoxId_10511
# select를 이용해서, tr들을 불러오기
#anchorBoxId_10549 > div > div.thumbnail > div > a > img
#anchorBoxId_10550 > div > div.thumbnail > div > a
clothes = soup.select('ul.prdList > li')
print(len(clothes))
num = 1 
# movies (tr들) 의 반복문을 돌리기
for clothe in clothes:
    # movie 안에 a 가 있으면,
    #anchorBoxId_10549 > div > div.thumbnail > div > a > img
    a_tag = clothe.select_one('div > div.thumbnail > div > a > img')
    print(a_tag)
    num = num + 1 
    # if a_tag is not None:
    #     # a의 text를 찍어본다.
    #     print (num)
    #     # print (a_tag.text)
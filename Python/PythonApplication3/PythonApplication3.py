# BeautifulSoup은 HTML 과 XML 파일로부터 데이터를 수집하는 라이브러리
# pip install bs4
# pip install requests
# pip install fake-useragent
 
import requests
import re
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import csv
 
# 파싱할 대상 Web URL
url = "https://search.shopping.naver.com/best100v2/detail.nhn?catId=50004603"
# 크롬브라우저가 실행하는 것처럼 속이기
headers = { 'User-Agent': UserAgent().chrome }
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.content,'html.parser')
# print(soup)
 
# 스크래핑하고자 하는 전체 데이터를 선택
# items = soup.find_all("li", attrs={"class":re.compile("^^_itemSection")})
items = soup.select('#productListArea > ul > li')
# print(items)
 
shopItemList = [] # 리스트 생성
for item in items:
    temp = []
    # name = item.find('a')['title']#제품명
    name = item.select_one('#productListArea > ul > li > div.thumb_area > a')['title']
    # price = item.find('span', attrs = {'class':'num'}).get_text() + '원' #가격 
    price = item.select_one('#productListArea > ul > li > div.price > strong > span.num').text + '원'
    # link = item.find('div', attrs={'class':'thumb_area'}).find('a')['href'] #링크 
    link = item.select_one('#productListArea > ul > li > div.thumb_area > a')['href']
    # review_count = item.find('span',attrs = {'class':'mall'}).find('em').text #리뷰수
    review_count = item.select_one('#productListArea > ul > li > div.info > span > a.txt > em').text
    # print(review_count)
    review_count = review_count[1:-1]
    temp.append(name)
    temp.append(price)
    temp.append(review_count)
    temp.append(link)
    shopItemList.append(temp)
    #print(shopItemList)
 
with open('c:/temp/shopItemList.csv',"w", encoding="ANSI", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['품명','가격','리뷰수','링크'])
    writer.writerows(shopItemList)
    print('CSV File created!')
f.close

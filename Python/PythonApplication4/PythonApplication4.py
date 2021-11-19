# 네이버 실시간 뉴스 정보 가져오기
# BeautifulSoup은 HTML 과 XML 파일로부터 데이터를 수집하는 라이브러리
# pip install selenium
# pip install chromedriver-autoinstaller 
# pip install bs4

from selenium import webdriver 
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
 
options = Options()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('headless'); # headless는 화면이나 페이지 이동을 표시하지 않고 동작하는 모드
 
# webdirver 설정(Chrome, Firefox 등)
chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=options) # 브라우저 창 안보이기
# driver = webdriver.Chrome() # 브라우저 창 보이기
 
# 크롬 브라우저 내부 대기 (암묵적 대기)
driver.implicitly_wait(5)
 
# 브라우저 사이즈
driver.set_window_size(1920,1280)
 
# 페이지 이동(열고 싶은 URL)
baseURL = 'https://news.naver.com/'
driver.get(baseURL)
 
soup = BeautifulSoup(driver.page_source, 'html.parser')
headline_new_list = soup.select('ul.hdline_article_list > li')
 
print('-' * 55, end=' ')
print('네이버 실시간 뉴스',end=' ')
print('-' * 55)
for v in headline_new_list:
    # print(v)
    title = v.select_one('div.hdline_article_tit > a').text.strip()
    news_url = v.select_one('div.hdline_article_tit > a').get('href')
    news_url = '{}{}'.format(baseURL,news_url)
    print(title, ', ', news_url)
print('-' * 130)


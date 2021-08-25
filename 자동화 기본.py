# 자동화 기본


'''
크롤링(Crawling) : 웹 사이트에서 원하는 정보를 수집하는 기술
Parsing : 데이터 중에서 원하는 데이터를 추출하는 분석 과정


라이브러리 사용 방법

import aaa 선언 시 
aaa.함수명() 으로 사용 가능함

from aaa import bbb 선언 시 aaa 안에 있는 bbb() 함수만 선언한 것임
bbb()로 바로 사용 가능함

해당 라이브러리가 없을 경우 아래 명령어로 라이브러리 설치를 해주어야 함
pip install 라이브러리명


크롤링을 위한 주요 라이브러리
requests
bs4


'''

# https://davelee-fun.github.io/blog/crawl_test_css

'''
import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.naver.com/')
# res.content를 파이썬2 버전에서 확인 시 '응답 없음' 상태가 됨

soup = BeautifulSoup(res.content, 'html.parser')

datas = soup.select('li')

for item in datas:
    print(item.get_text())

''' 

# 위와 동일한 기능으로 모듈화 함
'''
import requests
from bs4 import BeautifulSoup

def crawlingTemplate(url, selector):
    return_data = list()

    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    datas = soup.select(selector)
    for item in datas:
        print(item.get_text())
        return_data.append(item.get_text())
    
    return return_data

link = 'https://finance.naver.com/item/main.nhn?code=005930'
returned_data = crawlingTemplate(link, 'tr td #_market_sum')
print(returned_data)
'''

'''
select 안에 들어갈 수 있는 것

'li a' -> li태그 안에 a태그
'li > a' -> li태그 안에 a태그가 연속으로 올 때만

'.abc' -> abc클래스
'li.abc.def' -> li태그 안에 abc클래스 안에 def클래스의 데이터를 추출함

'#start' -> id가 start인 경우 추출함

'''


# 테스팅
'''
import requests
from bs4 import BeautifulSoup

def crawlingTemplate(url, selector):
    return_data = list()

    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    datas = soup.select(selector)
    for item in datas:
        print(item.get_text())
        print('http://www.drapt.com/e_sale/' + item['href'])
        return_data.append(item.get_text())
    
    return return_data

link = 'http://www.drapt.com/e_sale/index.htm?page_name=cont_list&menu_key=6'
returned_data = crawlingTemplate(link, 'a.c0000000')
for i in returned_data:
    print(i)
'''


# pickle 사용방법 (리스트를 파일에 저장하고 읽기)
'''
import pickle

def readFile(savedFileName):
    try:
        with open(savedFileName, 'rb') as file1:  # with 명령어는 알아서 파일을 닫아주는 기능을 함
            data1 = pickle.load(file1)  # 파일 읽기
        print('readFile()')
    except:
        print('excepted readFile()')
        data1 = list()
        
    return data1

def writeFile(savedFileName, data1):
    try:
        with open(savedFileName, 'wb') as file1:
            pickle.dump(data1, file1)  # 파일에 저장하기
        print('writeFile()')
    except:
        print('excepted writeFile()')


writeFile('pickle_filename.txt', '1234567890')

rd = readFile('pickle_filename.txt')
print('data :' + rd + '\n')

writeFile('pickle_filename.txt', 'abdcefg')

rd = readFile('pickle_filename.txt')
print('data :' + rd + '\n')
'''



# 데이터 A와 데이터 B를 비교하여 다른 부분을 출력하는 코드
'''
dataA = [1, 2, 3, 4, 5, 6, 10, 9]  # 새로운 데이터
dataB = [1, 2, 3, 4, 5, 6]  # 기존에 저장된 데이터
return_data = list()

for itemA in dataA:
    finding = False

    for itemB in dataB:
        if itemB == itemA:
            finding = True
            break
        
    if finding == False:  # 다를 경우 실행
        return_data.append(itemA)

print(return_data)
'''


# 문자열 처리 함수
'''
data1 = '     3333333hi my 3 name is ... 33    '
print(data1)

data1 = data1.strip()  # strip() 앞뒤 공백 제거
print(data1)

data1 = data1.strip('3')  # strip() 앞뒤 특정 문자 제거
print(data1)

data1 = data1.lstrip('3')  # lstrip() 앞 특정 문자 제거
print(data1)

data1 = data1.rstrip('3')  # rstrip() 뒤 특정 문자 제거
print(data1)

data2 = data1.split()  # split() 공백을 기준으로 하여 문자열을 잘라 리스트로 만듦
print(data2)

data2 = data1.split('is')  # split() 특정문자를 기준으로 하여 문자열을 잘라 리스트로 만듦
print(data2)
'''


# 동적 웹페이지는 Selenium을 통해서 가져와야 함. selenium은 웹을 테스트하기 위한 프레임워크이다.
# 1. cmd를 열고 pip install selenium 을 통해서 설치를 한다.
# 2. 테스트 할 웹브라우저와 드라이버를 설치한다. (두 버전은 동일해야 함)
# 2-1. https://chromedriver.chromium.org/home
# 2-2. os에 맞게 다운로드 한다. 윈도우라면 이것.. chromedriver_win32.zip
# 2-3. 압축 해제 후 실행 할 파이썬파일과 동일한 곳으로 이동한다.
# 3. 할 일 끝난 후 꼭 driver.quit()로 종료한다.
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # 이름이 길어서 EC로 대체함
from selenium.webdriver.common.by import By


# 실행할 .py파일과 chromedriver.exe 파일의 위치를 다르게 할 경우 전체 경로를 적어주어야 함
driver_location = './chromedriver.exe'
driver = webdriver.Chrome(driver_location)
driver.get('https://finance.naver.com/item/main.nhn?code=005930')

time.sleep(3)  # 웹페이지가 로딩되는 시간을 고려하여 3초 쉬고 실행
#WebDriverWait(driver, 3)  # 로딩될 때까지 3초 기다리지만 로딩 완료 시 바로 실행
try:
    # 해당 태그를 찾을 때까지 10초간 기다림
    button1 = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".month3")))
    button1.click()  # 해당 태그를 찾았을 경우 클릭이 할 수도 있음
except:
    print("WebDriverWait 예외발생, 해당 태그가 있는지 확인해주세요.")

# 특정 데이터 추출, find_elements_by_css_selector()를 사용한다.
data1 = driver.find_elements_by_css_selector('td > #_market_sum')

try:
    # 무슨 데이터가 있는지 출력
    for item in data1:
        print(item.text)
except:
    print('데이터를 읽는데 문제가 발생하였습니다.')
finally:  # 예외 발생과 상관없이 무조건 실행
    driver.quit()  # 크롬 드라이버 종료

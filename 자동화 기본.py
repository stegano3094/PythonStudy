# �ڵ�ȭ �⺻


'''
ũ�Ѹ�(Crawling) : �� ����Ʈ���� ���ϴ� ������ �����ϴ� ���
Parsing : ������ �߿��� ���ϴ� �����͸� �����ϴ� �м� ����


���̺귯�� ��� ���

import aaa ���� �� 
aaa.�Լ���() ���� ��� ������

from aaa import bbb ���� �� aaa �ȿ� �ִ� bbb() �Լ��� ������ ����
bbb()�� �ٷ� ��� ������

�ش� ���̺귯���� ���� ��� �Ʒ� ��ɾ�� ���̺귯�� ��ġ�� ���־�� ��
pip install ���̺귯����


ũ�Ѹ��� ���� �ֿ� ���̺귯��
requests
bs4


'''

# https://davelee-fun.github.io/blog/crawl_test_css

'''
import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.naver.com/')
# res.content�� ���̽�2 �������� Ȯ�� �� '���� ����' ���°� ��

soup = BeautifulSoup(res.content, 'html.parser')

datas = soup.select('li')

for item in datas:
    print(item.get_text())

''' 

# ���� ������ ������� ���ȭ ��
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
select �ȿ� �� �� �ִ� ��

'li a' -> li�±� �ȿ� a�±�
'li > a' -> li�±� �ȿ� a�±װ� �������� �� ����

'.abc' -> abcŬ����
'li.abc.def' -> li�±� �ȿ� abcŬ���� �ȿ� defŬ������ �����͸� ������

'#start' -> id�� start�� ��� ������

'''


# �׽���
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


# pickle ����� (����Ʈ�� ���Ͽ� �����ϰ� �б�)
'''
import pickle

def readFile(savedFileName):
    try:
        with open(savedFileName, 'rb') as file1:  # with ��ɾ�� �˾Ƽ� ������ �ݾ��ִ� ����� ��
            data1 = pickle.load(file1)  # ���� �б�
        print('readFile()')
    except:
        print('excepted readFile()')
        data1 = list()
        
    return data1

def writeFile(savedFileName, data1):
    try:
        with open(savedFileName, 'wb') as file1:
            pickle.dump(data1, file1)  # ���Ͽ� �����ϱ�
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



# ������ A�� ������ B�� ���Ͽ� �ٸ� �κ��� ����ϴ� �ڵ�
'''
dataA = [1, 2, 3, 4, 5, 6, 10, 9]  # ���ο� ������
dataB = [1, 2, 3, 4, 5, 6]  # ������ ����� ������
return_data = list()

for itemA in dataA:
    finding = False

    for itemB in dataB:
        if itemB == itemA:
            finding = True
            break
        
    if finding == False:  # �ٸ� ��� ����
        return_data.append(itemA)

print(return_data)
'''


# ���ڿ� ó�� �Լ�
'''
data1 = '     3333333hi my 3 name is ... 33    '
print(data1)

data1 = data1.strip()  # strip() �յ� ���� ����
print(data1)

data1 = data1.strip('3')  # strip() �յ� Ư�� ���� ����
print(data1)

data1 = data1.lstrip('3')  # lstrip() �� Ư�� ���� ����
print(data1)

data1 = data1.rstrip('3')  # rstrip() �� Ư�� ���� ����
print(data1)

data2 = data1.split()  # split() ������ �������� �Ͽ� ���ڿ��� �߶� ����Ʈ�� ����
print(data2)

data2 = data1.split('is')  # split() Ư�����ڸ� �������� �Ͽ� ���ڿ��� �߶� ����Ʈ�� ����
print(data2)
'''


# ���� ���������� Selenium�� ���ؼ� �����;� ��. selenium�� ���� �׽�Ʈ�ϱ� ���� �����ӿ�ũ�̴�.
# 1. cmd�� ���� pip install selenium �� ���ؼ� ��ġ�� �Ѵ�.
# 2. �׽�Ʈ �� ���������� ����̹��� ��ġ�Ѵ�. (�� ������ �����ؾ� ��)
# 2-1. https://chromedriver.chromium.org/home
# 2-2. os�� �°� �ٿ�ε� �Ѵ�. �������� �̰�.. chromedriver_win32.zip
# 2-3. ���� ���� �� ���� �� ���̽����ϰ� ������ ������ �̵��Ѵ�.
# 3. �� �� ���� �� �� driver.quit()�� �����Ѵ�.
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # �̸��� �� EC�� ��ü��
from selenium.webdriver.common.by import By


# ������ .py���ϰ� chromedriver.exe ������ ��ġ�� �ٸ��� �� ��� ��ü ��θ� �����־�� ��
driver_location = './chromedriver.exe'
driver = webdriver.Chrome(driver_location)
driver.get('https://finance.naver.com/item/main.nhn?code=005930')

time.sleep(3)  # ���������� �ε��Ǵ� �ð��� ����Ͽ� 3�� ���� ����
#WebDriverWait(driver, 3)  # �ε��� ������ 3�� ��ٸ����� �ε� �Ϸ� �� �ٷ� ����
try:
    # �ش� �±׸� ã�� ������ 10�ʰ� ��ٸ�
    button1 = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".month3")))
    button1.click()  # �ش� �±׸� ã���� ��� Ŭ���� �� ���� ����
except:
    print("WebDriverWait ���ܹ߻�, �ش� �±װ� �ִ��� Ȯ�����ּ���.")

# Ư�� ������ ����, find_elements_by_css_selector()�� ����Ѵ�.
data1 = driver.find_elements_by_css_selector('td > #_market_sum')

try:
    # ���� �����Ͱ� �ִ��� ���
    for item in data1:
        print(item.text)
except:
    print('�����͸� �дµ� ������ �߻��Ͽ����ϴ�.')
finally:  # ���� �߻��� ������� ������ ����
    driver.quit()  # ũ�� ����̹� ����

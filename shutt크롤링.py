# https://www.shutterstock.com/ko/ 사이트 크롤링

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time 
from bs4 import BeautifulSoup 
import requests 
import math
import pymysql # mysql 라이브러리 로딩

import googletrans

translator = googletrans.Translator()
user1 = input('검색어 입력 : ')
result1 = translator.translate(user1, dest='en').text

print(result1)

path = "./drive/chromedriver.exe"

#처음시작시 브라우저를 최대한으로 키우자 
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized") 
driver = webdriver.Chrome(path, chrome_options=options)



url = 'https://www.shutterstock.com/ko/'
driver.get(url)
time.sleep(5) #문서 불러올 시간 벌어줌 3초 대기 

search_box1 = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/form/div/div/div/div[1]/div/div[2]/span/div/div/div[1]/input') # 검색창 class
search_box1.click() #마우스로 누른 상황과 같다 
search_box1.send_keys(user1)  #검색창에 글씨 쓰기
search_box1.send_keys(Keys.RETURN) #검색창에 엔터키 신호를 보내서 검색을 하도록 한다 
time.sleep(3) #2초 이상 시간을 기다린다. 창이 바뀔때까지 시간을 줌

search_box2 = driver.find_element_by_xpath('//*[@id="FilterListItem_imageTypeFilter"]/div/div/div[2]/div/button')  # 사진만(조건) 선택
search_box2.click()
time.sleep(3)

num = 1
for i in range(1,11):
    내리기전 = 0
    while True:
        driver.execute_script("scrollTo(0, document.documentElement.scrollHeight)")
        time.sleep(2)
        내린후 = driver.execute_script("return document.documentElement.scrollHeight")
        if 내린후 == 내리기전:
            break
        내리기전 = 내린후

    doc = driver.page_source
    soup = BeautifulSoup(doc,'html.parser')
    img = soup.find_all('img',class_='z_h_9d80b z_h_2f2f0')
    for i in img:
        imgs = i.get('src')
        if imgs != None:
            res = requests.get(imgs)
            f = open(f'./data/face/sad/{user1}{num}.jpg','wb')
            f.write(res.content)
            f.close()
            num += 1

    # 다음페이지 클릭
    search_box4 = driver.find_element_by_css_selector('#content > div.s_f_ff6d0 > div > div.oc_ab_e5c9b.oc_ab_46972.b_Q_f0f29.oc_ab_6c502.b_Q_7113c.oc_ab_4ae09.b_Q_045e8 > div.oc_ab_57b1b.b_Q_01b73 > main > div > div.z_b_39dd6.k_a_5828e.k_a_228d7 > div.k_a_48274.k_a_1841e.k_a_ab189.k_a_53dab > div > a')
    search_box4.click()
    time.sleep(3)
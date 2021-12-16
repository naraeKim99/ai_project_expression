# 멜론크롤링
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time 
from bs4 import BeautifulSoup 
import requests 
from pandas import DataFrame
import pandas as pd

from wcwidth import wcswidth 
def fmt(x, w, align='r'): 
    """ 동아시아문자 폭을 고려하여, 문자열 포매팅을 해 주는 함수. 
        w 는 해당 문자열과 스페이스문자가 차지하는 너비. 
        align 은 문자열의 수평방향 정렬 좌/우/중간.
    """ 
    x = str(x) 
    l = wcswidth(x) 
    s = w-l 
    if s <= 0: 
        return x 
    if align == 'l':
        return x + ' '*s 
    if align == 'c': 
        sl = s//2 
        sr = s - sl 
        return ' '*sl + x + ' '*sr 
    return ' '*s + x

def MELONmusic(i):
    url = "https://www.melon.com/dj/djfinder/djfinder_inform.htm"
    path = "./drive/chromedriver.exe"



    #처음시작시 브라우저를 최대한으로 키우자 
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized") 
    options.add_argument("headless")
    driver = webdriver.Chrome(path, chrome_options=options,options=options)

    driver.get(url)
    time.sleep(2) #문서 불러올 시간 벌어줌 3초 대기 
    search_box1 = driver.find_element_by_xpath('//*[@id="djSearchKeyword"]') # 검색창 class
    search_box1.click() #마우스로 누른 상황과 같다 
    
    if i == 'angry':
        x='화'
    elif i == 'smile':
        x='행복'
    elif i == 'wonder':
        x='진정'
    elif i == 'sad':
        x='위로'

    search_box1.send_keys(x)  #검색창에 글씨 쓰기
    search_box1.send_keys(Keys.RETURN) #검색창에 엔터키 신호를 보내서 검색을 하도록 한다 
    time.sleep(2) #2초 이상 시간을 기다린다. 창이 바뀔때까지 시간을 줌

    doc = driver.page_source
    Soup = BeautifulSoup(doc,'html.parser')
    div1 = Soup.find('div',id='djPlylstList')
    # div2 = div1.find('div',class_='service_list_play')
    ul = div1.find('ul')
    li = ul.find_all('li')
    div3 = li[0].find('div',class_='info')
    a = div3.find_all('a')
    href1 = a[1].get("href")
    pdfFileId = href1[11:-1]
    print(pdfFileId)
    driver.execute_script(f"{pdfFileId}")

    doc = driver.page_source
    soup = BeautifulSoup(doc,'html.parser')
    tbody = soup.find('tbody')
    tr = tbody.find_all("tr")
    titleList = []
    singerList = []
    cnt = 1
    for j in tr:
        td = j.find_all("td")
        for i in td:
            title = i.find("div",class_="rank01")
            act = i.find("div",class_="rank02")
            if title != None:
                singer=act.text
                singer=singer[:len(singer)//2]
                singer = singer.replace("\n","")
                title = title.text
                title = title.replace('\n',"")
                titleList.append(title)
                singerList.append(singer)
                cnt += 1
            if cnt > 10:
                break
    playList = []
    for a, b in zip(titleList, singerList):
        j = dict()
        j['song'] = a
        j['singer'] = b
        playList.append(j)
    return playList

def MELONimpassive():
    url = "https://www.melon.com/index.htm"
    path = "./drive/chromedriver.exe"

    #처음시작시 브라우저를 최대한으로 키우자 
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized") 
    options.add_argument("headless")
    driver = webdriver.Chrome(path, chrome_options=options,options=options)

    driver.get(url)
    time.sleep(2) #문서 불러올 시간 벌어줌 3초 대기 
    search_box1 = driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[1]/a/span[2]') # 검색창 class
    search_box1.click() #마우스로 누른 상황과 같다 
    time.sleep(2)
    doc = driver.page_source
    soup = BeautifulSoup(doc,'html.parser')
    tbody = soup.find('tbody')
    tr = tbody.find_all("tr",class_='lst50')
    titleList = []
    singerList = []
    cnt = 1
    for j in tr:
        td = j.find_all("td")
        for i in td:
            title = i.find("div",class_="rank01")
            act = i.find("div",class_="rank02")
            if title != None:
                singer=act.text
                singer=singer[:len(singer)//2]
                singer = singer.replace("\n","")
                title = title.text
                title = title.replace('\n',"")
                titleList.append(title)
                singerList.append(singer)
                cnt += 1
            if cnt > 10:
                break
    playList = []
    for a, b in zip(titleList, singerList):
        j = dict()
        j['song'] = a
        j['singer'] = b
        playList.append(j)
    return playList
    
if __name__ == "__main__":
    MELONmusic()
    playList = MELONimpassive()
    print(playList)
# 벅스크롤링
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time 
from bs4 import BeautifulSoup 
import requests  

# 글자수_영/한 띄어쓰기 동일하게 하도록 포매팅하는 함수
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

def BUGSmusic(x):
    url = "https://music.bugs.co.kr/musicpd?tag_id="
    path = "./drive/chromedriver.exe"

    #처음시작시 브라우저를 최대한으로 키우자 
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized") 
    options.add_argument("headless")
    driver = webdriver.Chrome(path, chrome_options=options,options=options)

    driver.get(url)
    time.sleep(2) #문서 불러올 시간 벌어줌 3초 대기 
    if x == 'angry':
        search_box1 = driver.find_element_by_xpath('//*[@id="container"]/aside/div/table/tbody/tr[1]/td[4]/ul/li[3]/a') # 검색창 class
        search_box1.click() #마우스로 누른 상황과 같다 
        time.sleep(2) #2초 이상 시간을 기다린다. 창이 바뀔때까지 시간을 줌
    elif x == 'wonder':
        search_box1 = driver.find_element_by_xpath('//*[@id="container"]/aside/div/table/tbody/tr[1]/td[4]/ul/li[6]/a') # 검색창 class
        search_box1.click() #마우스로 누른 상황과 같다 
        time.sleep(2) #2초 이상 시간을 기다린다. 창이 바뀔때까지 시간을 줌
    elif x == 'smile':
        search_box1 = driver.find_element_by_xpath('//*[@id="container"]/aside/div/table/tbody/tr[1]/td[4]/ul/li[1]/a') # 검색창 class
        search_box1.click() #마우스로 누른 상황과 같다 
        time.sleep(2) #2초 이상 시간을 기다린다. 창이 바뀔때까지 시간을 줌
    elif x == 'sad':
        search_box1 = driver.find_element_by_xpath('//*[@id="container"]/aside/div/table/tbody/tr[1]/td[4]/ul/li[11]/a') # 검색창 class
        search_box1.click() #마우스로 누른 상황과 같다 
        time.sleep(2) #2초 이상 시간을 기다린다. 창이 바뀔때까지 시간을 줌
    search_box2 = driver.find_element_by_xpath('//*[@id="container"]/section/div/header/p[2]/a[1]') # 검색창 class
    search_box2.click() #마우스로 누른 상황과 같다 
    time.sleep(2)

    doc = driver.page_source
    Soup = BeautifulSoup(doc,'html.parser')
    ul = Soup.find('ul',class_="musicPDAlbumList")
    li = ul.find_all("li")
    fig1= li[0].find("figcaption",class_="info")
    a = fig1.find('a')
    href1 = a.get("href")
    driver.get(href1)
    time.sleep(2)
    doc = driver.page_source
    Soup = BeautifulSoup(doc,'html.parser')
    track = Soup.find('table',class_='trackList')
    tbody = track.find('tbody')
    tr = tbody.find_all("tr")
    titleList = []
    singerList = []
    cnt = 1
    for j in tr:
        th = j.find("th")
        p = th.find("p",class_='title')
        title = p.find('a')

        art = j.find("p",class_="artist")
        if title != None:
            art = art.text
            art = art.replace("\n","")
            title = title.text
            titleList.append(title)
            singerList.append(art)
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


def BUGSimpassive():
    url = "https://music.bugs.co.kr/"
    path = "./drive/chromedriver.exe"

    #처음시작시 브라우저를 최대한으로 키우자 
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized") 
    options.add_argument("headless")
    driver = webdriver.Chrome(path, chrome_options=options,options=options)

    driver.get(url)
    time.sleep(2) #문서 불러올 시간 벌어줌 3초 대기 

    search_box1 = driver.find_element_by_xpath('//*[@id="gnbBody"]/div/div[1]/nav/ul/li[1]/a') # 검색창 class
    search_box1.click() #마우스로 누른 상황과 같다 
    time.sleep(2) #2초 이상 시간을 기다린다. 창이 바뀔때까지 시간을 줌

    doc = driver.page_source
    Soup = BeautifulSoup(doc,'html.parser')
    track = Soup.find('table',class_='trackList')
    tbody = track.find('tbody')
    tr = tbody.find_all("tr")
    titleList = []
    singerList = []
    cnt = 1
    for j in tr:
        th = j.find("th")
        p = th.find("p",class_='title')
        title = p.find('a')

        art = j.find("p",class_="artist")
        if title != None:
            art = art.text
            art = art.replace("\n","")
            title = title.text
            titleList.append(title)
            singerList.append(art)
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
    BUGSmusic('angry')
    BUGSimpassive()
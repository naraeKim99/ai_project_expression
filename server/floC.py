# 플로크롤링
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time 
from bs4 import BeautifulSoup 
import requests 

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

def FLOmusic(x):
    url = "https://www.music-flo.com"
    path = "./drive/chromedriver.exe"

    #처음시작시 브라우저를 최대한으로 키우자 
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized") 
    options.add_argument("headless")
    driver = webdriver.Chrome(path, chrome_options=options,options=options)

    driver.get(url)
    time.sleep(3) #문서 불러올 시간 벌어줌 3초 대기 

    search_box = driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/div/div[2]/button') # 닫기
    search_box.click() #마우스로 누른 상황과 같다 
    time.sleep(2)

    search_box1 = driver.find_element_by_xpath('//*[@id="header"]/div/nav/ul/li[1]/a') # 둘러보기
    search_box1.click() #마우스로 누른 상황과 같다 
    time.sleep(2)
#//*[@id="browseMood"]/div[2]/ul/li[3]/a/span
#//*[@id="browseMood"]/div[2]/ul/li[3]/a
    doc = driver.page_source
    Soup = BeautifulSoup(doc,'html.parser')
    sec = Soup.find('section',id='browseMood')
    ul = sec.find('ul',class_="list_thumb_category")
    li = ul.find_all("li")
    if x == 'angry':
        a = li[11].find("a") #파워풀한
    elif x == 'sad':    
        a = li[2].find("a") #위로하는
    elif x == 'smile':
        a = li[0].find("a") #신나는
    elif x == 'wonder':
        sec = Soup.find('section',id='browseSittn')
        ul = sec.find('ul',class_="list_thumb_category")
        li = ul.find_all("li")
        a = li[13].find("a") #밤,새벽
    href1 = a.get("href")
    driver.get(url  + href1)
    time.sleep(2)
    # search_box2 = driver.find_element_by_xpath('//*[@id="POPULARITY"]') # 검색창 class
    # search_box2.click() #마우스로 누른 상황과 같다 
    # time.sleep(2)

    doc = driver.page_source
    Soup = BeautifulSoup(doc,'html.parser')
    ul = Soup.find('ul',class_="thumbnail_list")
    li = ul.find_all("li")
    fig1= li[0].find("p",class_="title")
    a = fig1.find('a')
    href1 = a.get("href")
    driver.get(url + href1)
    time.sleep(2)

    doc = driver.page_source
    Soup = BeautifulSoup(doc,'html.parser')
    track = Soup.find('div',class_='chart_lst')
    tbody = track.find('tbody')
    tr = tbody.find_all("tr")
    titleList = []
    singerList = []
    cnt = 1
    for j in tr:
        td = j.find("td",class_='info')
        p = td.find("p",class_='tit')
        title = p.find('strong')

        td = j.find("td",class_="artist")
        art = td.find('span',class_='tooltip')
        if title and art != None:
            title = title.text
            art = art.text
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
    
def FLOimpassive():
    url = "https://www.music-flo.com"
    path = "./drive/chromedriver.exe"

    #처음시작시 브라우저를 최대한으로 키우자 
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized") 
    options.add_argument("headless")
    driver = webdriver.Chrome(path, chrome_options=options,options=options)

    driver.get(url)
    time.sleep(3) #문서 불러올 시간 벌어줌 3초 대기 

    search_box = driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/div/div[2]/button') # 닫기
    search_box.click() #마우스로 누른 상황과 같다 
    time.sleep(2)

    search_box1 = driver.find_element_by_xpath('//*[@id="header"]/div/nav/ul/li[1]/a') # 둘러보기
    search_box1.click() #마우스로 누른 상황과 같다 
    time.sleep(2)

    doc = driver.page_source
    Soup = BeautifulSoup(doc,'html.parser')
    track = Soup.find('div',class_='chart_lst')
    tbody = track.find('tbody')
    tr = tbody.find_all("tr")
    titleList = []
    singerList = []
    cnt = 1
    for j in tr:
        td = j.find("td",class_='info')
        p = td.find("p",class_='tit')
        title = p.find('strong')

        td = j.find("td",class_="artist")
        art = td.find('span',class_='tooltip')
        if title and art != None:
            title = title.text
            art = art.text
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
    FLOmusic()
    FLOimpassive()
# 지니크롤링
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

def GENIEmusic(x):
    url = "https://www.genie.co.kr/playlist/tags"
    path = "./drive/chromedriver.exe"

    #처음시작시 브라우저를 최대한으로 키우자 
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized") 
    options.add_argument("headless")
    driver = webdriver.Chrome(path, chrome_options=options,options=options)

    driver.get(url)
    time.sleep(2) #문서 불러올 시간 벌어줌 3초 대기 
    if x == 'angry':
        search_box1 = driver.find_element_by_xpath('//*[@id="showTagList"]/dl[4]/dd/a[21]') # 검색창 class
        search_box1.click() #마우스로 누른 상황과 같다 
        time.sleep(2) #2초 이상 시간을 기다린다. 창이 바뀔때까지 시간을 줌
    elif x == 'wonder':
        search_box1 = driver.find_element_by_xpath('//*[@id="showTagList"]/dl[4]/dd/a[11]') # 검색창 class
        search_box1.click() #마우스로 누른 상황과 같다 
        time.sleep(2) #2초 이상 시간을 기다린다. 창이 바뀔때까지 시간을 줌
    elif x == 'smile':
        search_box1 = driver.find_element_by_xpath('//*[@id="showTagList"]/dl[4]/dd/a[22]') # 검색창 class
        search_box1.click() #마우스로 누른 상황과 같다 
        time.sleep(2) #2초 이상 시간을 기다린다. 창이 바뀔때까지 시간을 줌
    elif x == 'sad':
        search_box1 = driver.find_element_by_xpath('//*[@id="showTagList"]/dl[4]/dd/a[8]') # 검색창 class
        search_box1.click() #마우스로 누른 상황과 같다 
        time.sleep(2) #2초 이상 시간을 기다린다. 창이 바뀔때까지 시간을 줌

    search_box2 = driver.find_element_by_xpath('//*[@id="showTagList"]/div[2]/span[2]/a') # 검색창 class
    search_box2.click() #마우스로 누른 상황과 같다 
    time.sleep(2)

    
    search_box3 = driver.find_element_by_xpath('//*[@id="showTagList"]/div[2]/span[2]/span/a[2]') # 검색창 class
    search_box3.click() #마우스로 누른 상황과 같다 
    time.sleep(2)

    doc = driver.page_source
    Soup = BeautifulSoup(doc,'html.parser')
    ul = Soup.find('ul',class_="md_playlist")
    li = ul.find_all("li")
    div= li[0].find("div",class_="item_info")
    a = div.find_all('a')
    onclick = a[0].get("onclick")
    pdfFileId = onclick[11:-15]
    print(pdfFileId)
    driver.execute_script(f"{pdfFileId}")
    time.sleep(2)
    doc = driver.page_source
    Soup = BeautifulSoup(doc,'html.parser')
    track = Soup.find('table',class_='list-wrap')
    tbody = track.find('tbody')
    tr = tbody.find_all("tr")
    titleList = []
    singerList = []
    cnt = 1
    for j in tr:
        td = j.find("td",class_='info')
        title = td.find("a",class_='title')
        art = td.find("a",class_="artist")
        if title != None:
            title = title.text
            title = title.replace("TITLE","")
            title = title.replace("\n","")
            title = title.split()
            title=" ".join(title)
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

def GENIEimpassive():
    url = "https://www.genie.co.kr/"
    path = "./drive/chromedriver.exe"

    #처음시작시 브라우저를 최대한으로 키우자 
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized") 
    options.add_argument("headless")
    driver = webdriver.Chrome(path, chrome_options=options,options=options)

    driver.get(url)
    time.sleep(2) #문서 불러올 시간 벌어줌 3초 대기 

    search_box1 = driver.find_element_by_xpath('//*[@id="gnb"]/ul/li[1]/a') # 검색창 class
    search_box1.click() #마우스로 누른 상황과 같다 
    time.sleep(2) #2초 이상 시간을 기다린다. 창이 바뀔때까지 시간을 줌

    doc = driver.page_source
    Soup = BeautifulSoup(doc,'html.parser')
    track = Soup.find('table',class_='list-wrap')
    tbody = track.find('tbody')
    tr = tbody.find_all("tr")
    titleList = []
    singerList = []
    cnt = 1
    for j in tr:
        td = j.find("td",class_='info')
        title = td.find("a",class_='title')
        art = td.find("a",class_="artist")
        if title != None:
            title = title.text
            title = title.replace("TITLE","")
            title = title.replace("\n","")
            title = title.split()
            title=" ".join(title)
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
    GENIEmusic()
    GENIEimpassive()
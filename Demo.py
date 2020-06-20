import urllib3
from bs4 import BeautifulSoup
import re
import time

# 获取所有的链接
# page: 页
def fetchUrls(page):
    baseurl = "http://www.chinatax.gov.cn/chinatax/whmanuscriptList/n810755?_isAgg=0&_pageSize=2000&_template=index&_channelName=%E6%9C%80%E6%96%B0%E6%96%87%E4%BB%B6&_keyWH=wenhao&"
    url = baseurl + 'page=' + str(page)
    http = urllib3.PoolManager()
    r = http.request('GET', url)

    html_doc = r.data.decode()
    s1 = BeautifulSoup(html_doc, 'html.parser')
    links = s1.find_all('a', attrs={"href": re.compile('http:\/\/www\.chinatax\.gov\.cn*')})

    hrefs = []
    for k in links:
        hrefs.append(k.get('href'))

    return hrefs

# 从url获取文本，追加写到source.txt文件
def getContent(url):
    http = urllib3.PoolManager()
    r = http.request('GET', url)

    html_doc = r.data.decode()
    s = BeautifulSoup(html_doc, 'html.parser')
    title1 = s.find(class_='lanse')
    title2 = s.find(class_='yanse')

    file = open('最新文件.txt', 'a')
    file.write('\n\n\n=============================start=================================\n\n\n')
    try:
        file.write(title1.text)
        file.write('\n')
        print(title1.text)
    except Exception: pass

    try:
        file.write(title2.text)
        file.write('\n')
        file.write('链接：'+url)
        file.write('\n')
    except Exception: pass

    try:
        content = s.find_all('p')
        for p in content:
            file.write(p.text)
            file.write('\n')

        file.write('\n\n\n=============================end===================================\n\n\n')
        file.close()
    except Exception: pass

    return

i = 1
while i <= 1:
    hrefs = fetchUrls(i)
    for url in hrefs:
        # print('start: '+url)
        getContent(url)
        time.sleep(5)

    i += 1


# getContent('http://www.chinatax.gov.cn/chinatax/n810341/n810755/c5149072/content.html')

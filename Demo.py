import urllib3
from bs4 import BeautifulSoup
import re

def fetchUrls():
    baseurl = "http://www.chinatax.gov.cn/chinatax/whmanuscriptList/n810755?_isAgg=0&_pageSize=20&_template=index&_channelName=%E6%9C%80%E6%96%B0%E6%96%87%E4%BB%B6&_keyWH=wenhao&"
    url = baseurl + 'page=1'
    http = urllib3.PoolManager()
    r = http.request('GET', url)

    html_doc = r.data.decode()
    s1 = BeautifulSoup(html_doc, 'html.parser')
    links = s1.find_all('a', attrs={"href": re.compile('http:\/\/www\.chinatax\.gov\.cn*')})

    for k in links:
        print(k.get('href'))

    return

def getContent():
    url = "http://www.chinatax.gov.cn/chinatax/n810341/n810755/c5153547/content.html"
    http = urllib3.PoolManager()
    r = http.request('GET', url)

    html_doc = r.data.decode()
    s = BeautifulSoup(html_doc, 'html.parser')
    title1 = s.find(class_='lanse')
    title2 = s.find(class_='yanse')
    print(title1.text)
    print(title2.text)
    content = s.find_all('p')
    for p in content:
        file = open('source.txt', 'a')
        file.write(p.text)
        file.close()

    return


getContent()
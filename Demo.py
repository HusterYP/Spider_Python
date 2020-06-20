import urllib3
from bs4 import BeautifulSoup
import re
import time

# 获取所有的链接
# page: 页
def fetchUrls(page):
    # baseurl = "http://www.chinatax.gov.cn/chinatax/whmanuscriptList/n810755?_isAgg=0&_pageSize=2000&_template=index&_channelName=%E6%9C%80%E6%96%B0%E6%96%87%E4%BB%B6&_keyWH=wenhao&"
    baseurl = "http://www.chinatax.gov.cn/chinatax/manuscriptList/n810760?_isAgg=0&_pageSize=1000&_template=index&_channelName=%E6%94%BF%E7%AD%96%E8%A7%A3%E8%AF%BB&_keyWH=wenhao&page=1"
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
    title1 = s.find(class_='title sv_texth1')
    title2 = s.find(class_='laiyuan laiyuan2')

    file = open('政策解读.txt', 'a')
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


hrefs = fetchUrls(1)

for url in hrefs:
    getContent(url)
    time.sleep(1)




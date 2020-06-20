import urllib3
from bs4 import BeautifulSoup
import re

# 获取所有的链接
# page: 页
def fetchUrls(page):
    baseurl = "http://www.chinatax.gov.cn/chinatax/whmanuscriptList/n810755?_isAgg=0&_pageSize=20&_template=index&_channelName=%E6%9C%80%E6%96%B0%E6%96%87%E4%BB%B6&_keyWH=wenhao&"
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
    file = open('source.txt', 'a')
    file.write('\n\n\n=============================start=================================\n\n\n')
    file.write(title1.text)
    file.write('\n')
    file.write(title2.text)
    file.write('\n')
    file.write('链接：'+url)
    file.write('\n')
    content = s.find_all('p')
    for p in content:
        file.write(p.text)
        file.write('\n')

    file.write('\n\n\n=============================end===================================\n\n\n')
    file.close()

    print("Done: "+url)
    return

hrefs = fetchUrls(1)


# for url in hrefs:
#     getContent(url)
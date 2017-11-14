#动态网站爬取

import urllib
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

csvFile = open("E:/haha.csv", 'w+')
writer = csv.writer(csvFile)

# Animation
writer.writerow(('bilibili', ' ', ' ', ' ', ' ', ' '))
writer.writerow(('paimin', 'minchen', 'bofangshu', 'danmushu', 'zonghezhishu'))
driverThree = webdriver.PhantomJS()
driverThree.get("http://www.bilibili.com/ranking#!/bangumi/0/0/7/")
time.sleep(5)
pageSourceThree = driverThree.page_source
bs0bjThree = BeautifulSoup(pageSourceThree, "html.parser")

j = bs0bjThree.findAll("div", {"class": "title"})
k = bs0bjThree.findAll("div", {"class": "pts"})
l = bs0bjThree.findAll("span", {"class": "data-box play"})
m = bs0bjThree.findAll("span", {"class": "data-box dm"})

for b in range(10):
    titleThree = j[b].get_text()
    IndexThre = k[b].get_text()
    num = len(IndexThre)
    IndexThree = IndexThre[0:num - 4]
    bofangliang = l[b].get_text()
    danmuliang = m[b].get_text()

    writer.writerow((b + 1, titleThree, bofangliang, danmuliang, IndexThree))

driverThree.close()

# Comic
writer.writerow(('tecentac', ' ', ' ', ' '))
writer.writerow(('paimin', 'minchen', 'piaoshu'))
driverFour = webdriver.PhantomJS()
driverFour.get("http://ac.qq.com/Rank/")
time.sleep(5)
pageSourceFour = driverFour.page_source
bs0bjFour = BeautifulSoup(pageSourceFour, "html.parser")

n = bs0bjFour.findAll("a", {"class": "mod-rank-name ui-left"})
o = bs0bjFour.findAll("span", {"class": "mod-rank-num ui-right"})

for c in range(10):
    titleFour = n[c].get_text()
    piaoshu = o[c].get_text()
    writer.writerow((c + 1, titleFour, piaoshu))

driverFour.close()
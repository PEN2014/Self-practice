#-*- coding:utf-8 -*-
import urllib
from bs4 import BeautifulSoup

html = urllib.urlopen("http://python-data.dr-chuck.net/comments_234022.html")
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
result = 0

for tag in tags:
	print 'TAG', tag
	print 'Contents:', int(tag.contents[0]), '\n'
	result = result + int(tag.contents[0])

print result

'''
import urllib

fhand = urllib.urlopen('https://tw.dictionary.yahoo.com')

for line in fhand:
	print line.strip()
'''


#-*- coding:utf-8 -*-
import urllib
from bs4 import BeautifulSoup

html = urllib.urlopen("https://tw.dictionary.yahoo.com")
soup = BeautifulSoup(html, "html.parser")

tags = soup('form')

print '===================='
print tags[1]
for content in tags[1].contents:
	print '**********'
	print content
	

'''
for tag in tags:
	print '----------'
	print 'TAG', tag
	# print 'Contents:', tag.contents, '\n'
	for content in tag.contents:
		print '**********'
		print 'Content', content, '\n'

'''
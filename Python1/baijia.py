#!D:\Python\python.exe
# -*- coding: UTF-8 -*-

print
import urllib
import urllib2
import re

class News:

    #init
    def __init__(self):
        self.url = "http://baijia.baidu.com/"

    #convert div to ''
    def tranTags(self, x):
        pattern = re.compile('<img.*?>')
        p = re.compile('<p.*?</p>')
        span = re.compile('<span.*?>')
        span2 = re.compile('</span>')
        b = re.compile('<b.*?</b>')
        i = re.compile('<i.*?</i>')
        em = re.compile('<em.*?</em>')
        em2= re.compile('</em>')
        res = re.sub(span2,'',re.sub(em2,'',re.sub(em,'',re.sub(i,'',re.sub(b,'',re.sub(span,'',re.sub(p,'',re.sub(pattern, '', x))))))))
        return res

    #getPage
    def getPage(self):
        url = self.url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read()

    def getTitle(self):
    	page = self.getPage()
    	pattern = re.compile('<a href="(http://.*?)".*?>(.*?)</a>',re.S)
    	content = re.findall(pattern,page)
    	for item in content:
    		print self.tranTags(item[0]),self.tranTags(item[1])



news = News()
news.getTitle()
# <div class="feeds" data-total="200">
# <a href="http://junstapo.baijia.baidu.com/article/696673" target="_blank" mon="col=13&pn=2">人工智能+医疗，未来会怎样？</a>

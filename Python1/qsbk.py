#!D:\Python\python.exe
# -*- coding: UTF-8 -*-

print
import urllib
import urllib2
import re
import thread
import time

class QSBK:

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozi;;a/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent' : self.user_agent}
        self.stories = []
        self.enable = False

    #传入某一页的索引获得页面代码
    def getPage(self, pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib2.Request(url, headers = self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接糗事百科失败,错误原因", e.reason
                return None

    #传入某一页索引,返回本页不带图片的段子列表
    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "页面加载失败..."
            return None
        pattern = re.compile('<div class="author clearfix">.*?<img src.*?title=.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?<span class="stats-vote"><i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>',re.S);
        items = re.findall(pattern, pageCode)
        pageStories = []
        for item in items:
            if '<br /> in item':
                text = re.sub('<br/>', '\n', item[1])
                like = item[2]
                comment = item[3]
                pageStories.append([item[0].strip(), text.strip(), like.strip(), comment.strip()])
        return pageStories

    #加载并提取页面的内容,加入到列表中
    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1

    #每次回车输出一个段子
    def getOneStory(self, pageStories, page):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input == "q":
                self.enable = False
                return 
            print u"第%d页\t发布人:%s\t喜欢:%s\t评论:%s\n%s" %(page,story[0],story[2],story[3],story[1])

    #开始方法
    def start(self):
        print u"正在读取糗事百科,按回车可以查看新段子,Q退出"  
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories, nowPage)




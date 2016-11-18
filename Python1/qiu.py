#!D:\Python\python.exe
# _*_ coding:utf-8 _*_

print
import urllib
import urllib2
import re
#import chardet

page = 1
url = ' http://www.qiushibaike.com/hot/page/' + str(page)
# user_agent = "Mozi;;a/4.0 (compatible; MSIE 5.5; Windows NT)"
user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0"
headers = { 'User-Agent' : user_agent}
try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    content = response.read()
    pattern = re.compile('<div class="author clearfix">.*?<img src.*?title=.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?<span class="stats-vote"><i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>',re.S)
    #pattern = re.compile('<div class="author clearfix">.*</div>',re.S)
    items = re.findall(pattern, content)
    #thischarset = chardet.detect(items)["encoding"]
    for item in items:
        print item[0], item[1], item[2], '\n'

except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason

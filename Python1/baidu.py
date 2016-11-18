#!D:\Python\python.exe
# -*- coding: UTF-8 -*-

print
import urllib
import urllib2
import re
from db import *
from curd import curd

class News:

	#init
	def __init__(self):
		self.url = "http://www.xiao.com/test/caiji/news.html"

	def getPage(self):
		url = self.url
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		return response.read()

	#convert div to ''
	def divFilter(self, x):
		pattern = re.compile('<div.*?</div>')
		res = re.sub(pattern, '', x)
		return res

	#convert span to ''
	def spanFilter(self, x):
		pattern = re.compile('<span .*?<a href="')
		img = re.compile('<img.*?>')
		res = re.sub(img,'',re.sub(pattern, '', x))
		return res

	#定位导航div .decode('utf-8')
	def getNav(self):
		getPage = self.getPage()
		pattern = re.compile('(<div id="menu".*?)<i class="slogan"></i>',re.S)
		items = re.search(pattern, getPage)
		return items.group(1)

	#获取导航信息 并入库
	def getNavInfo(self):
		getNav = self.getNav()
		pattern2 = re.compile('<a href=("http://.*?/).*?>(.*?)</a>', re.S)
		array = re.findall(pattern2,getNav)
		str1=''
		val1=''
		for val in array:
			s = self.divFilter(val[1])
			val1 = val[0]
			nurl = val1[1:]
			str = '("'+nurl+'","'+s+'"),'
			str1 += str
		navstr = str1[:-1]
		#入库
		sql = 'insert into url(url,name) values'+navstr
		try:
			# 执行sql语句
			cursor.execute(sql)
			# 提交到数据库执行
			db.commit()
		except:
			# Rollback in case there is any error
			db.rollback()

	def getBody(self):
		getPage = self.getPage()
		bodyContent = re.compile('(<div id="body".*?)<div id="footerwrapper">', re.S)
		title = re.search(bodyContent,getPage)
		return title.group(1)

	#采集标题&&url  并入库
	def getTitle(self):
		getBody = self.getBody()
		#pattern3 = re.compile('<a href="(http://.*?\.(html|shtml|htm|aspx)).*?>(.*?)</a>', re.S)
		pattern3 = re.compile('<a href="(http://.*?)".*?>(.*?)</a>', re.S)
		title = re.findall(pattern3,getBody)
		# #过滤img
		# img = re.compile('<img.*?>')
		# span = re.compile('<span .*?<a href="')
		str1=''
		for item in title:
			if item[1]!='':
				url = item[0]
				title = self.spanFilter(item[1])
				# str = '("'+url+'","'+title+'"),'
				# str1 += str[:-1]
				sql = 'insert into title(url,title) values(%s,%s)'
				parem = (url,title)
				try:
					# 执行sql语句
					cursor.execute(sql,parem)
					# 提交到数据库执行
					db.commit()
				except:
					# Rollback in case there is any error
					db.rollback()


news = News()
news.getTitle()
news.getNavInfo()









# con = str1[:-1]
# #print con
# mysql=curd()
# sql = 'insert into title(url,title) values'+con
# mysql.getrows("insert into title(url,title) values"+str1)
# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # Rollback in case there is any error
#    db.rollback()

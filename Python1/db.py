#!D:\Python\python.exe
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect(host="localhost",user="root",passwd="xiao",db="1",charset="utf8")

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

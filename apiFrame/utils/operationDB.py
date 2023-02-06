# -*-coding:utf-8 -*-
# Author:xmLi

from base.method import Requests
import pymysql
import pytest



# @pytest.fixture()
def connSQL():
	'''链接数据库'''
	db = pymysql.connect(host="192.168.18.168",port=3306,user="lixiaoman",password="lxm@123!",database="cq_rcw_new")
	return db

def cursorCre():
	'''数据库游标实例化'''
	aa = connSQL()
	cursor = aa.cursor(cursor=pymysql.cursors.DictCursor)
	return cursor

# -*-coding:utf-8 -*-
# Author:xmLi

import pytest
import requests
from TEST.Pytest import read_data
import pymysql

account = {'username':15730332499,'password':'lxm+123456'}
data = read_data.readJson()

@pytest.fixture()
def getToken():
	'''获取token'''
	r =requests.post(url='http://192.168.18.167:201/backend/login',data=account)
	token = r.json()["data"]["jwtToken"]
	return token

@pytest.fixture()
def connSQL():
	db = pymysql.connect(host="192.168.18.168",port=3306,user="lixiaoman",password="lxm@123!",database="cq_rcw_new")
	return db

# @pytest.fixture()
# def connClose(connSQL):
# 	connSQL.close()
# @pytest.fixture()
# def connClose(connSQL,test_getUser,cursorCre):
# 	'''清理测试数据，并关闭数据库链接'''
# 	sql_dels = [{'sql':'DELETE from admin_user_role where staff_id ={0}'.format(test_getUser)},{'sql':'DELETE from admin_user where id ={0}'.format(test_getUser)}]
# 	for sql in sql_dels:
# 		cursorCre.execute(sql)
# 		result = cursorCre.fetchall()
# 		print('\n执行结果\n',result)
# 	connSQL.close()

@pytest.fixture()
def cursorCre(connSQL):
	cursor = connSQL.cursor(cursor=pymysql.cursors.DictCursor)
	return cursor


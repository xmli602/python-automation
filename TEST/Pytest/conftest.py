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
# def closeSql(connSQL):
# 	connSQL.close()

@pytest.fixture()
def cursorCre(connSQL):
	cursor = connSQL.cursor(cursor=pymysql.cursors.DictCursor)
	return cursor


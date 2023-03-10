# -*-coding:utf-8 -*-
# Author:xmLi

import pytest
import requests
from TEST.Pytest import read_data
import pymysql

account = {'username':15730332499,'password':'lxm+123456'}
data = read_data.readJson()

@pytest.fixture()
def getToken_Oper():
	'''获取运营端token'''
	r =requests.post(url='http://192.168.18.167:201/backend/login',data=account)
	token = r.json()["data"]["jwtToken"]
	return token

@pytest.fixture()
def getToken_BC():
	'''获取BC端token'''
	r = requests.post(url=data['item'][0]['request']['url'],json=data['item'][0]['request']['body'])
	token = r.json()['data']['accessToken']
	return token

@pytest.fixture()
def connSQL():
	db = pymysql.connect(host="192.168.18.168",port=3306,user="lixiaoman",password="lxm@123!",database="cq_rcw_new")
	return db


@pytest.fixture()
def cursorCre(connSQL):
	cursor = connSQL.cursor(cursor=pymysql.cursors.DictCursor)
	return cursor


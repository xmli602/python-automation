# -*-coding:utf-8 -*-
# Author:xmLi

from base.method import Requests
from utils.operationExcel import OperartionExcel
from utils.operationYaml import OperationYaml
import pytest
import pymysql

obj = Requests()
yaml = OperationYaml()
excel = OperartionExcel()

@pytest.fixture()
def getToken():
	'''获取运营端token'''
	r = obj.post(url=yaml.readYaml()[1]['url'],data=yaml.readYaml()[1]['data'])
	token = r.json()['data']['jwtToken']
	return token

@pytest.fixture()
def get_BC_token():
	'''获取BC端token'''
	r = obj.post(url=yaml.readYaml()[0]['url'],json = yaml.readYaml()[0]['data'])
	token = 'bearer ' + r.json()['data']['accessToken']
	return token

@pytest.fixture()
def get_userid(get_BC_token):
	'''获取userid'''
	r = obj.get(url=yaml.readYaml()[2]['url'],headers={'Authorization':'{0}'.format(get_BC_token)})
	return r.json()['data']['userId']

# @pytest.fixture()
# def connSQL():
# 	'''链接数据库'''
# 	db = pymysql.connect(host="192.168.18.168",port=3306,user="lixiaoman",password="lxm@123!",database="cq_rcw_new")
# 	return db
#
# @pytest.fixture()
# def cursorCre(connSQL):
# 	'''数据库游标实例化'''
# 	cursor = connSQL.cursor(cursor=pymysql.cursors.DictCursor)
# 	return cursor




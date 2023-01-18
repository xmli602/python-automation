# -*-coding:utf-8 -*-
# Author:xmLi

# fixture基础-初始化和清理详解及举例
import json

import pytest
import requests
from selenium import webdriver
from TEST.Pytest import read_data
import pymysql
from requests_toolbelt.multipart.encoder import MultipartEncoder

# 执行顺序
# @pytest.fixture()
# def init():
# 	print('\n初始化数据')
# 	yield
# 	print('清理数据')
#
# def test_one(init):
# 	print('测试步骤')


# pytest-selenium插件，用于在UI自动化
# @pytest.fixture()
# def init(selenium): # 此处selenium 为webdriverd实例化后的对象
# 	selenium.maximize_window()
# 	selenium.implicitly_wait(3)
# 	selenium.get('http://www.baidu.com/')
# 	yield
# 	selenium.quit()
#
# def test_baidu_title(init,selenium):
# 	assert selenium.title == '百度一下，你就知道'


# 实例，人才网运营端新增user
data = read_data.readJson()
# @pytest.fixture()
# def connSQL():
# 	db = pymysql.connect(host="192.168.18.168",port=3306,user="lixiaoman",password="lxm@123!",database="cq_rcw_new")
# 	return db
#
# def closeSql(connSQL):
# 	connSQL.close()

def closeSql(connSQL):
	connSQL.close()

@pytest.fixture()
def init(connSQL):
	connSQL
	yield
	closeSql(connSQL)

def test_addUser(getToken,init,connSQL):
	'''添加运营端用户'''
	r = requests.post(url=data["item"][1]["request"]["url"],
	                  json=data["item"][1]["request"]["body"],
	                  headers={'Authorization':'{0}'.format(getToken)})
	cursor = connSQL.cursor()
	sql = "select * from admin_user where telephone = {0}".format(data["item"][1]["request"]["body"]["telephone"])
	cursor.execute(sql)
	result = cursor.fetchall()
	print(result)

# def test_delUser(getToken):
# 	'''将运营端账号办理离职'''
# 	r = requests.get(url='http://192.168.18.167:201/backend/system/user/manageUser?id=1452578357845467136&type=2',
# 	                 headers={'Authorization':'{0}'.format(getToken)})
# 	print(r.json())
#
#
# def test_getUser(getToken):
# 	r = requests.get(url='http://192.168.18.167:201/backend/system/user/pageUser?deptId=&name=&telephone={0}'.format(data["item"][1]["request"]["body"]["telephone"]),
# 	                 headers={'Authorization':'{0}'.format(getToken)})
# 	assert r.json()["data"]["records"][0]["telephone"] == data["item"][1]["request"]["body"]["telephone"]

if __name__ == '__main__':
    pytest.main(["-s","-v",'fun6_test.py'])

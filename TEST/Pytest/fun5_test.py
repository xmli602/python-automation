# -*-coding:utf-8 -*-
# Author:xmLi

# fixture基础

import json
import pytest
import requests
from TEST.Pytest import read_data
import json

test_data = read_data.readJson()
# @pytest.fixture()
# def data():
# 	return 'hello'
#
# def test_data(data):    # 形式参数就是data这个方法
# 	assert data == 'hello'

# 实例获取token作为参数
@pytest.fixture()
def getToken():
	'''获取token'''
	r = requests.post(url=test_data['item'][0]['request']['url'],json=test_data['item'][0]['request']['body'])
	token = r.json()['data']['accessToken']
	return token

def test_get_name(getToken):
	'''获取用户名称'''
	# print(getToken)
	r = requests.get(url='https://www.cqrc.net/account/user/baseInfo',
	                 headers={'authorization':'bearer {0}'.format(getToken)})
	print(r.json()['data']['name'])

# getToken()
if __name__ == '__main__':
    pytest.main(["-s","-v",'fun5_test.py'])

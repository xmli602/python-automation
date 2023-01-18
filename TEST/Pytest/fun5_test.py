# -*-coding:utf-8 -*-
# Author:xmLi

# fixture基础-返回值：测试用例和测试用例之间是传递参数和数据

import pytest
import requests
from TEST.Pytest import read_data

test_data = read_data.readJson()
# @pytest.fixture()
# def data():
# 	return 'hello'
#
# def test_data(data):    # 形式参数就是data这个方法
# 	assert data == 'hello'


# 引用conftest文件中被fixture装饰的获取token的方法
def test_get_name(getToken_BC):
	'''获取BC端用户名称'''
	# print(getToken)
	r = requests.get(url='https://www.cqrc.net/account/user/baseInfo',
	                 headers={'authorization':'bearer {0}'.format(getToken_BC)})
	print(r.json()['data']['name'])

# getToken()
if __name__ == '__main__':
    pytest.main(["-s","-v",'fun5_test.py'])

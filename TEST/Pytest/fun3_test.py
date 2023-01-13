# -*-coding:utf-8 -*-
# Author:xmLi


import requests
import json
import pytest

def test_login_001():
	dic1={"account": "13996365087", "password": "12345678", "loginWay": 0}
	r = requests.post(url='https://www.cqrc.net/account/user/login',json=dic1)
	# print(r.json())
	assert '密码错误' in r.json()['message']

# 预期测试用例执行失败
@pytest.mark.xfail(reason='期望返回的状态码是200.实际是508')
def test_login_002():
	dic1={"account": "13996365087", "password": "12345678", "loginWay": 0}
	r = requests.post(url='https://www.cqrc.net/account/user/login',json=dic1)
	# print(r.json()['code'])
	assert r.json()['code'] == 200



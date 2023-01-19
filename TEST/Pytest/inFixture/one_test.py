# -*-coding:utf-8 -*-
# Author:xmLi
import reprlib

import pytest
import requests


@pytest.fixture(name='token')
def test_login_BC(username,password):
	dict1 = {"account":username,"password":password,"loginWay":0}
	r = requests.post(url='http://192.168.18.167:2002/account/user/login',json=dict1)
	print('\n响应结果时间\n',r.json())
	return r.json()['data']['accessToken']


def test_get_userName(tmpdir,token):
	f = tmpdir.join('token.txt')
	f.write(token)
	r = requests.get(url='http://192.168.18.167:2002/account/user/baseInfo',headers={'Authorization':'bearer {0}'.format(f.read())})
	print('\n账号名称为\n',r.json()['data']['name'])

if __name__ == '__main__':
    pytest.main(["-s","-v",'one_test.py'])




# -*-coding:utf-8 -*-
# Author:xmLi
import reprlib

import requests

def test_login_BC(username,password):
	dict1 = {"account":username,"password":password,"loginWay":0}
	r = requests.post(url='https://www.cqrc.net/account/user/login',json=dict1)
	print('\n响应结果\n',r.json())



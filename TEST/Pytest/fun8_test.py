# -*-coding:utf-8 -*-
# Author:xmLi

# fixture参数化详解

import pytest
import json

def add(a,b):
	return a+b

def datas():
	return [[1,1,2],[2,2,4],[3,3,6],[4,4,8],[5,5,10]]

@pytest.fixture(params=datas())
def getDate(request):
	'''获取到fixture装饰的参数'''
	return request.param

def test_one(getDate):
	assert add(getDate[0],getDate[1]) == getDate[2]





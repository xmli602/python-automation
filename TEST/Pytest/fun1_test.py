# -*-coding:utf-8 -*-
# Author:xmLi

# 基础执行顺序

import pytest

def test_002():
	assert 1==2

@pytest.mark.login
def test_001():
	assert 1==1

@pytest.mark.logout
class TestLogin(object):
	def test_login(self):
		assert 1==1

	def add(self):
		assert 1==1


def add(a,b):
	return a+b

@pytest.mark.login
def test_add():
	try:
		assert add(1,"1") == 2
	except Exception as e:
		print(e.args[0])




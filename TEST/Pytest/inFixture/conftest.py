# -*-coding:utf-8 -*-
# Author:xmLi

import pytest

def pytest_addoption(parser):
	parser.addoption('--username',action='store',default='15730332499',help='')
	parser.addoption('--password',action='store',default='123456',help='')

@pytest.fixture()
def username(request):
	return request.config.getoption('--username')

@pytest.fixture()
def password(request):
	return request.config.getoption('--password')

# -*-coding:utf-8 -*-
# Author:xmLi

from base.method import Requests
from utils.operationExcel import OperartionExcel
from utils.operationYaml import OperationYaml
import pytest

obj = Requests()
yaml = OperationYaml()
excel = OperartionExcel()

@pytest.fixture()
def getToken():
	'''获取运营端token'''
	r = obj.post(url=yaml.readYaml()[1]['url'],data=yaml.readYaml()[1]['data'])
	token = r.json()['data']['jwtToken']
	return token




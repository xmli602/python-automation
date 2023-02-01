# -*-coding:utf-8 -*-
# Author:xmLi

from common.public import *
from base.method import Requests
from utils.operationExcel import OperartionExcel
from utils.operationYaml import OperationYaml
import pytest



class TestAccount():
	obj = Requests()
	excel = OperartionExcel()
	objyaml = OperationYaml()

	def test_accountAdd_001(self,getToken):
		'''新增运营端数据'''
		r = self.obj.post(
			url=self.excel.get_url(row=1),
			json=self.excel.get_data(1),
			headers={'Authorization':'{0}'.format(getToken)})
		assert self.excel.get_except(row=1) == r.json()['message']

	def test_accountGet_002(self,getToken):
		'''获取新增的账号id'''
		url = self.excel.get_url(row=2)
		caseID = self.excel.get_caseId(row=2)
		r = self.obj.get(
			url=str(url).replace('{telephone}',self.objyaml.dictYaml()[caseID]),
			headers={'Authorization': '{0}'.format(getToken)}
		)
		writeFile(r.json()['data']['records'][0]['id'])
		assert self.excel.get_except(row=2) in r.text

	def test_accountLeave_003(self,getToken):
		'''离职运营端账号'''
		url = self.excel.get_url(3)
		r = self.obj.get(
			url=str(url).replace('{ID}',readFile()),
			headers={'Authorization': '{0}'.format(getToken)}
		)
		assert self.excel.get_except(row=2) in r.text



if __name__ == '__main__':
    pytest.main(["-s","-v","test_account.py::TestAccount::test_accountLeave_003"])
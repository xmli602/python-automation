# -*-coding:utf-8 -*-
# Author:xmLi

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

	# @pytest.fixture()
	def test_accountGet_002(self,getToken):
		'''获取新增的账号id'''
		r = self.obj.get(
			url=self.excel.get_url(row=2),
			headers={'Authorization': '{0}'.format(getToken)}
		)
		print(r.json())


if __name__ == '__main__':
    pytest.main(["-v","test_account.py::TestAccount::test_accountGet_002"])
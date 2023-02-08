# -*-coding:utf-8 -*-
# Author:xmLi

import pytest
import json
from utils.operationDB import *
from utils.operationExcel import OperartionExcel
from utils.operationYaml import OperationYaml
from datetime import datetime
from base.method import Requests

# 组装基础数据
def r_params(params):
	for key, value in basics.items():
		if key in params.keys():
			params[key] = str(value)
	return params

class TestDeliver():
	obj = Requests()
	excel = OperartionExcel()
	yaml = OperationYaml()

	def test_deliver_001(self,get_BC_token,job_data):
		'''检查是否发起聊天'''
		params = self.excel.get_data(row=1)
		r = self.obj.post(
			url = self.excel.get_url(row=1),
			json = r_params(params),
			headers = json.loads(str(self.excel.get_headers(row=1)).replace('{token}',get_BC_token))
		)
		print(r.text)

if __name__ == '__main__':
	pytest.main(["-s", "-v", "test_deliver.py"])



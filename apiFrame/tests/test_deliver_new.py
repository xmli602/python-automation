# -*-coding:utf-8 -*-
# Author:xmLi

# C端用户投递

import pytest
import json
from utils.operationDB import *
from utils.opreationExcelN import OperationExcelN,ExcelVarles
from utils.operationYaml import OperationYaml
from common.public import *
from datetime import datetime
from base.method import Requests

obj = Requests()
excel = OperationExcelN()
yaml = OperationYaml()

@pytest.mark.parametrize('datas',excel.runs())
def test_deliver(datas,get_BC_token,get_userid):
	'''简历投递流程测试'''

	# 对请求参数为空以及做反序列化处理
	params = datas[ExcelVarles.params]
	if len(str(params).strip()) == 0:
		pass
	elif len(str(params).strip()) >= 0:
		params = json.loads(params)

	def r_params():
		'''组装请求参数，将参数替换为投递基础数据'''
		for key,value in basics.items():
			if key in params.keys():
				params[key] = str(value)
		return params

	# 对请求头为空以及做反序列化处理
	header = datas[ExcelVarles.headers]
	if len(str(header).strip()) == 0:
		pass
	elif len(str(header).strip()) >= 0:
		header = json.loads(header)

	r_code = int(datas[ExcelVarles.status_code])
	def case_assert_result(rquest):
		'''
		封装断言，状态码和期望值
		:param rquest:
		:return:
		'''
		assert rquest.status_code == r_code
		assert datas[ExcelVarles.expect] in json.dumps(rquest.json(),ensure_ascii=False)

	# 获取token
	prevResult = get_BC_token
	# 调用替换token
	header = excel.prevHeaders(prevResult)

	# # 执行前置条件关联的测试点
	# r = obj.post(
	# 	url=excel.case_prev(datas[ExcelVarles.casePre])[ExcelVarles.caseUrl],
	# 	json = json.loads(excel.case_prev(datas[ExcelVarles.casePre])[ExcelVarles.params])
	# )


	if datas[ExcelVarles.casePre] == '':
		print(r_params())
		r = obj.post(url=datas[ExcelVarles.caseUrl],
		             json=r_params(), headers=header)
		case_assert_result(rquest=r)
		print(r.json())
	elif datas[ExcelVarles.casePre] != '':
		print(excel.case_prev(datas[ExcelVarles.casePre])[ExcelVarles.params])
		r = obj.post(
			url=excel.case_prev(datas[ExcelVarles.casePre])[ExcelVarles.caseUrl],
			json=json.loads(excel.case_prev(datas[ExcelVarles.casePre])[ExcelVarles.params]),
			headers = header
		)
		# r.json()['data']['totle']
		print('前置条件：'+ str(r.json()))
		r_new = obj.post(url=datas[ExcelVarles.caseUrl], json=r_params(), headers=header)
		case_assert_result(rquest=r_new)
		print('创建房间：' + str(r_new.json()))

if __name__ == '__main__':
	pytest.main(["-s", "-v", "test_deliver_new.py"])


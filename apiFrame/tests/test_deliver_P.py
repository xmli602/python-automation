# -*-coding:utf-8 -*-
# Author:xmLi

# C端用户投递

import pytest
import json
from utils.operationDB import *
from utils.opreationExcelN import OperationExcelN,ExcelVarles
from utils.operationYaml import OperationYaml
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

	check_msg = ''  # 是否发起聊天
	check_deliver = '' # 是否存在未接受的投递
	check_deliver_msg = '' # 检查投递返回消息

	if datas[ExcelVarles.caseName] == '检查是否已发起聊天':
		print(r_params())
		r = obj.post(url=datas[ExcelVarles.caseUrl],json = r_params(),headers = header)
		case_assert_result(rquest=r)
		check_msg = r.json()['data']
	elif datas[ExcelVarles.caseName] == '创建聊天房间' and check_msg is '':
		r = obj.post(url=datas[ExcelVarles.caseUrl],json = r_params(),headers = header)
		case_assert_result(rquest=r)
		basics.update({"extension":r.json()['data']['deliverId']})
		basics.update({"roomId":r.json()['data']['roomId']})
	elif datas[ExcelVarles.caseName] == '检查是否有未接收的投递':
		r = obj.post(url=datas[ExcelVarles.caseUrl], json=r_params(), headers=header)
		case_assert_result(rquest=r)
		check_deliver = r.json()['data']
		check_deliver_msg = r.json()['message']
		if check_deliver == True:
			excel.write_casePre(casePre=check_deliver)
	elif datas[ExcelVarles.casePre] == check_deliver:
		if datas[ExcelVarles.caseName] == '发送聊天消息':
			r_params()["sendId"] = basics["userId"]
			r_params()["receiveId"] = basics["hrId"]
			r_params()["sendTime"] = "2023-02-08 11:19:00"
		r = obj.post(url=datas[ExcelVarles.caseUrl],json = r_params(),headers = header)
		case_assert_result(rquest=r)
	else:
		print(check_deliver_msg)

if __name__ == '__main__':
	pytest.main(["-s", "-v", "test_deliver_P.py"])


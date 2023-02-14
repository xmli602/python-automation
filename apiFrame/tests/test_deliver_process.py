# -*-coding:utf-8 -*-
# Author:xmLi

# C端用户投递

import pytest
import json
from utils.operationDB import *
from utils.opreationExcelN import *
from utils.operationYaml import OperationYaml
from common.public import *
from datetime import datetime
from base.method import Requests

obj = Requests()


@pytest.mark.parametrize('datas',execl.runs())
def test_deliver(datas,get_BC_token,get_userid):
	'''简历投递流程测试'''

	# 对请求参数为空以及做反序列化处理
	params = datas[ExcelVarles.params]
	if len(str(params).strip()) == 0:
		pass
	elif len(str(params).strip()) >= 0:
		params = json.loads(params)

	def r_params(params):
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

	# 状态码、期望结果分裂处理
	r_code = str(datas[ExcelVarles.status_code])
	r_code_list = r_code.split('|')
	new_code = [int(x) for x in r_code_list]
	r_expect = str(datas[ExcelVarles.expect])
	r_expect_list = r_expect.split('|')
	def case_assert_result(rquest):
		'''
		封装断言，状态码和期望值
		:param rquest:
		:return:
		'''
		assert rquest.status_code in new_code
		assert rquest.json()['message'] in r_expect_list

	# 获取token
	prevResult = get_BC_token
	# 调用替换token
	header = execlN.prevHeaders(prevResult)


	# 执行所有前置条件关联的测试点
	case_pre = datas[ExcelVarles.casePre]
	casepre_list = str(case_pre).split('|')
	for pre in casepre_list:
		try:
			r_pre = obj.post(
				url=execlN.case_prev(pre)[ExcelVarles.caseUrl],
				json = r_params(json.loads(execlN.case_prev(pre)[ExcelVarles.params])),
				headers = header)
			if execlN.case_prev(pre)[ExcelVarles.caseName] == '检查是否已发起聊天' and r_pre.json()['data'] != '':
				basics.update({"roomId":r_pre.json()['data']['records'][0]['roomId']})
			elif execlN.case_prev(pre)[ExcelVarles.caseName] == '创建聊天房间' and r_pre.json()['code'] == 200:
				basics.update({"roomId": r_pre.json()['data']['roomId'],"extension": r_pre.json()['data']['deliverId']})
			elif execlN.case_prev(pre)[ExcelVarles.caseName] == '检查是否有未接收的投递' and r_pre.json()['message'] == '请等待HR接收！':
				pytest.exit('存在未接受简历,结束执行',returncode=1)
			elif execlN.case_prev(pre)[ExcelVarles.caseName] == '投递简历' and r_pre.json()['code'] == 200:
				basics.update({"extension": r_pre.json()['data'],"sendId": basics["userId"],"receiveId": basics["hrId"],"sendTime": "2023-02-09 15:44:00"})
		except Exception as e:
			print(str(datas[ExcelVarles.caseName]) + str(e))

	r = obj.post(url=datas[ExcelVarles.caseUrl],json = r_params(params),headers = header)
	case_assert_result(rquest=r)
	print('投递简历请求成功，响应报文：'+str(r.json()))

if __name__ == '__main__':
	pytest.main(["-s", "-v", "test_deliver_process.py"])


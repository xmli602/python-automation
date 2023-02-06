# -*-coding:utf-8 -*-
# Author:xmLi

# C端用户投递

import pytest
from utils.operationDB import connSQL,cursorCre
from utils.opreationExcelN import OperationExcelN,ExcelVarles
from utils.operationYaml import OperationYaml
from common.public import *
from base.method import Requests
import json

obj = Requests()
excel = OperationExcelN()
yaml = OperationYaml()
cursor = cursorCre()


def job_data():
	'''获取投递基础数据,岗位id,企业id,hrid'''
	sql_data = '''
	select id as jobId,enterprise_id as companyId,hr_id as hrId from enterprise_job where hr_id <>'1000000000' and status = 3 and source =0 order by rand() limit 1 
'''
	cursor.execute(sql_data)
	result = cursor.fetchall()
	data_job = result[0]
	return data_job





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
		for key,value in job_data().items():
			if key in params.keys():
				params[key] = str(value)
		return params

	# 对请求头为空以及做反序列化处理
	header = datas[ExcelVarles.headers]
	if len(str(header).strip()) == 0:
		pass
	elif len(str(header).strip()) >= 0:
		header = json.loads(header)

	# 获取token
	prevResult = get_BC_token
	# 调用替换token
	header = excel.prevHeaders(prevResult)

	check_msg = ''  # 是否发起聊天

	if datas[ExcelVarles.caseName] == '检查是否已发起聊天':
		for key,value in job_data().items():
			if key in params.keys():
				params[key] = str(value)
		params['userId'] = get_userid
		r = obj.post(url=datas[ExcelVarles.caseUrl],json = params,headers = header)
		assert r.json()['code'] == 200
		check_msg = datas[ExcelVarles.post_params] = r.json()['data']
	elif datas[ExcelVarles.caseName] == '创建聊天房间' and check_msg is '':
		r = obj.post(url=datas[ExcelVarles.caseUrl],json = r_params(),headers = header)
		print(r.json())





if __name__ == '__main__':
	pytest.main(["-s", "-v", "test_deliver.py"])


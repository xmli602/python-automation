# -*-coding:utf-8 -*-
# Author:xmLi

import pytest
from utils.opreationExcelN import OperationExcelN,ExcelVarles
from utils.operationYaml import OperationYaml
from common.public import *
from common.log import *
from base.method import Requests
import json
import time
from datetime import datetime
import openpyxl

obj = Requests()
excel = OperationExcelN()
yaml = OperationYaml()
cursor = cursorCre()

# def test_001(get_BC_token,get_userid):
# 	print(get_userid)
#
# if __name__ == '__main__':
# 	pytest.main(["-s", "-v", "test_aa.py"])

def job_data():
	'''获取投递基础数据,岗位id,企业id,hrid,userid,简历id'''
	basics = {}
	sql_dels = [{'sql':"select id as jobId,enterprise_id as companyId,hr_id as hrId from enterprise_job where hr_id <>'1000000000' and status = 3 and source =0 order by rand() limit 1"},
	            {'sql':"select a.id as userId,b.id from rcw_user a LEFT JOIN resume b on a.id = b.user_id where a.telephone = {0}".format(yaml.readYaml()[0]['data']['account'])}]
	for sql in sql_dels:
		cursor.execute(sql['sql'])
		result = cursor.fetchall()
		basics.update(result[0])
	return basics

def WriteExcel(excelpath: str, sheetname: str, index: int, writevalue: str):
	"""
	写入数据
	:param excelpath: 文件路径 -->  Excel
	:param sheetname: 文件sheet名称
	:param writevalue: 写入的数据
	:param index: 单元格位置
	:return: inster
	"""
	try:
		wb = openpyxl.load_workbook(excelpath)  # 加载工作簿
		sheet = wb[sheetname]  # 获得sheet对象
		active = wb.active  # 写入文件时需要激活
		active[index] = str(writevalue)  # 通过单元格写入 例如：A1 A2 A3等
		wb.save(excelpath)  # 保存
		log.info('成功在%s表的%s页%s单元格写入数据内容为：%s' % (excelpath, sheetname, index, writevalue))
	except Exception as e:
		log.error("WriteExcel Error：{}".format(e))

# WriteExcel(excelpath=filePath(fileDir='data',fileName='delivertest.xlsx'),sheetname='Sheet1',index='A8',writevalue='lxm')

# a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
# print(type(a))
# b = eval(a)
# print(type(b))
# print(b)


# params = { "sendId":"{user}","receiveId":"{hr_id}"}
#
# if 'sendId' or 'receiveId' in params.keys():
# 	params["sendId"] = job_data()["userId"]
# 	params["receiveId"] = job_data()["hrId"]

# sendTime = datetime.now().replace(microsecond=0)
# print(sendTime)






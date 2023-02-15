# -*-coding:utf-8 -*-
# Author:xmLi

from base.method import Requests
from utils.operationExcel import *
from utils.operationYaml import *
import pytest
import pymysql

obj = Requests()
# yaml = OperationYaml()
# excel = OperartionExcel()

@pytest.fixture()
def getToken():
	'''获取运营端token'''
	r = obj.post(url=yaml_example.readYaml()[2]['url'],data=yaml_example.readYaml()[2]['data'])
	token = r.json()['data']['jwtToken']
	return token

@pytest.fixture()
def get_BC_token():
	'''获取BC端token'''
	r = obj.post(url=yaml_example.readYaml()[0]['url'],json = yaml_example.readYaml()[0]['data'])
	token = 'bearer ' + r.json()['data']['accessToken']
	return token

@pytest.fixture()
def get_userid(get_BC_token):
	'''获取userid'''
	r = obj.get(url=yaml_example.readYaml()[1]['url'],headers={'Authorization':'{0}'.format(get_BC_token)})
	return r.json()['data']['userId']

@pytest.fixture()
def connSQL():
	'''链接数据库'''
	db = pymysql.connect(host="192.168.18.168",port=3306,user="lixiaoman",password="lxm@123!",database="cq_rcw_new")
	return db

@pytest.fixture()
def cursorCre(connSQL):
	'''数据库游标实例化'''
	cursor = connSQL.cursor(cursor=pymysql.cursors.DictCursor)
	return cursor

@pytest.fixture()
def define_sql(sql):
	'''
	定义sql语句
	:param sql:
	:return:
	'''
	return sql


@pytest.fixture()
def sql_execute(connSQL,cursorCre,define_sql):
	'''
	执行sql，并捕获执行结果
	:param connSQL: 数据库链接
	:param cursorCre: 数据库游标
	:param sql: 需要执行的sql语句
	:return:
	'''
	cursorCre.execute(define_sql)
	result_sql = cursorCre.fetchall()
	return result_sql



@pytest.fixture()
def job_data(connSQL,cursorCre):
	'''获取投递基础数据,岗位id,企业id,hrid,userid,简历id'''
	basics = {}
	sql_dels = [{'sql':"select id as jobId,enterprise_id as companyId,hr_id as hrId from enterprise_job where hr_id <>'1000000000' and status = 3 and source =0 order by rand() limit 1"},
	            {'sql':"select a.id as userId,b.id from rcw_user a LEFT JOIN resume b on a.id = b.user_id where a.telephone = {0}".format(yaml.readYaml()[0]['data']['account'])}]
	for sql in sql_dels:
		cursorCre.execute(sql['sql'])
		result = cursorCre.fetchall()
		basics.update(result[0])
	return basics

# @pytest.fixture()
# def r_params(job_data,params):
# 	for key, value in job_data.items():
# 		if key in params.keys():
# 			params[key] = str(value)
# 	return params

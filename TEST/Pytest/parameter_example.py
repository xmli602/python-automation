# -*-coding:utf-8 -*-
# Author:xmLi
# 参数实例化


import pytest
import requests
from TEST.Pytest.read_data import *


@pytest.mark.parametrize('data',readJson())
def test_login_json(data):
	'''json文件传参'''
	r = requests.post(url=data['request']['url'],json=data['request']['body'])
	assert r.json()['message'] == data['response']['message']


@pytest.mark.parametrize('data',readYaml())
def test_login_yaml(data):
	'''yaml文件传参'''
	r = requests.post(url=data['url'],json=json.loads(data['body']))
	print(r.json()['message'],type(r.json()['message']))
	assert r.json()['message'] == json.loads(data['response'])['message']

@pytest.mark.parametrize('data',readCsv())
def test_login_csv(data):
	'''csv文件传参'''
	r = requests.post(url=data[0],json=json.loads(data[1]))
	assert r.json()['message'] == json.loads(data[2])['message']

@pytest.mark.parametrize('data',readExcel())
def test_login_excel(data):
	'''excel文件传参'''
	r = requests.post(url=data[0],json=json.loads(data[1]))
	assert r.json()['message'] == json.loads(data[2])['message']



if __name__ == '__main__':
    pytest.main(["-s","-v","parameter_example.py::test_login_excel"])



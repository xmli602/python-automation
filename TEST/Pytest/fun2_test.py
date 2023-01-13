# -*-coding:utf-8 -*-
# Author:xmLi

# 执行命令行 pytest -s --durations=0 fun2_test.py
# 调试打印响应时间 --durations=0
# 调试打印响应时间时长前五 --durations=5

import requests
import pytest

def test_baidu():
	r = requests.get(url='http://www.baidu.com/')
	assert r.status_code == 200

def test_taobao():
	r = requests.get(url='http://www.taobao.com/')
	print(r.elapsed.total_seconds())
	assert r.status_code == 200

def test_jd():
	r = requests.get(url='http://www.jd.com/')
	assert r.status_code == 200

def test_sina():
	r = requests.get(url='http://www.sina.com/')
	assert r.status_code == 200
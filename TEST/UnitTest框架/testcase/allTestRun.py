# -*-coding:utf-8 -*-
# Author:xmLi

import unittest
import os
import HTMLTestRunner
import time

def getNowTime():
	return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))


def allTests():
	suite = unittest.TestLoader().discover(
		start_dir=os.path.dirname(__file__),
		pattern='test_*.py',
		top_level_dir=None)
	return suite

def run():
	fp = os.path.join(os.path.dirname(__file__),'report',getNowTime()+'-testReport.html')
	HTMLTestRunner.HTMLTestRunner(
		stream=open(fp,'wb'),title='自动化测试报告',description='自动化测试报告详细信息').run(allTests())
	# unittest.TextTestRunner(verbosity=2).run(allTests())

# print(os.path.join(os.path.dirname(__file__),'report','testReport.html'))   # 拼接文件url
if __name__ == '__main__':
	run()


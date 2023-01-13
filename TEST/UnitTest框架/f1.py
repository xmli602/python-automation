# -*-coding:utf-8 -*-
# Author:xmLi

import unittest

class F1(unittest.TestCase):
	def setUp(self) -> None:
		'''用做准备工作'''
		print('准备工作已完成')

	def tearDown(self) -> None:
		'''用做收尾工作'''
		print('已处理')

	def test_map(self):
		print('test001')

	def test_add(self):
		print('test002')

	def test_age(self):
		print('test003')

if __name__ == '__main__':
    unittest.main(verbosity=2)
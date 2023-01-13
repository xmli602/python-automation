# -*-coding:utf-8 -*-
# Author:xmLi

import unittest
import time
from init import *


class BaiduSo(Init):
	def test_baidu_so_enabled(self):
		'''首页搜索测试：输入框可编辑'''
		input_1 = self.driver.find_element_by_id('kw')
		self.assertTrue(input_1.is_enabled())

	def test_baidu_so(self):
		'''首页搜索测试：关键字搜索测试'''
		input_1 = self.driver.find_element_by_id('kw')
		input_1.send_keys('webdriver')
		self.driver.find_element_by_id('su').click()
		self.assertEquals(input_1.get_attribute('value'),'webdriver')

# 	@staticmethod
# 	def suite():
# 		suite = unittest.TestLoader().loadTestsFromTestCase(BaiduSo)
# 		return suite
#
# if __name__ == '__main__':
# 	unittest.TextTestRunner(verbosity=2).run(BaiduSo.suite())
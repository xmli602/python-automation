# -*-coding:utf-8 -*-
# Author:xmLi

import unittest
from selenium import webdriver
import time

class BaiduLink(unittest.TestCase):
	@classmethod
	def setUpClass(cls) -> None:
		cls.driver = webdriver.Chrome()
		cls.driver.maximize_window()
		cls.driver.implicitly_wait(30)
		cls.driver.get('http://www.baidu.com')

	@classmethod
	def tearDownClass(cls) -> None:
		cls.driver.quit()

	def test_baidu_news(self):
		'''首页链接测试：验证新闻的链接'''
		self.driver.find_element_by_xpath("//a[contains(text(),'新闻')]").click()
		time.sleep(2)

	def test_baidu_map(self):
		'''首页链接测试：验证地图的链接'''
		self.driver.find_element_by_xpath("//a[contains(text(),'地图')]").click()
		time.sleep(2)

class BaiduSo(unittest.TestCase):
	@classmethod
	def setUpClass(cls) -> None:
		cls.driver = webdriver.Chrome()
		cls.driver.maximize_window()
		cls.driver.implicitly_wait(30)
		cls.driver.get('http://www.baidu.com')

	@classmethod
	def tearDownClass(cls) -> None:
		cls.driver.quit()

	def test_baidu_s(self):
		'''首页搜索测试：搜索测试'''
		self.driver.find_element_by_xpath("//input[contains(@type,'text')]").send_keys("webdriver")
		time.sleep(2)


if __name__ == '__main__':
	# 按模块来加载执行
	suite = unittest.TestLoader().loadTestsFromModule('frame_example_module.py')
	unittest.TextTestRunner(verbosity=2).run(suite)

	# 按类加载测试用例
	# suite = unittest.TestSuite(unittest.makeSuite(BaiduTest))
	# suite = unittest.TestLoader().loadTestsFromTestCase(BaiduLink)

	# 手动加载单个测试用例
	# suite.addTest(BaiduTest('test_baidu_news'))
	# suite.addTest(BaiduTest('test_baidu_map'))



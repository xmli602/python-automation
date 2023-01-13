# -*-coding:utf-8 -*-
# Author:xmLi

import unittest
from selenium import webdriver

class Init(unittest.TestCase):
	@classmethod
	def setUpClass(cls) -> None:
		cls.driver = webdriver.Chrome()
		cls.driver.maximize_window()
		cls.driver.implicitly_wait(30)
		cls.driver.get('http://www.baidu.com')

	@classmethod
	def tearDownClass(cls) -> None:
		cls.driver.quit()
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

	def switch_new_window(self):
		'''切换到最新窗口'''
		# 找出新窗口
		new_window = self.driver.window_handles[-1]  # '-1'代表打开的最后一个窗口
		# 切换到新窗口
		self.driver.switch_to.window(new_window)

	def switch_old_window(self):
		'''返回原窗口'''
		# 找出原窗口
		old_window = self.driver.window_handles[0]  # '0'代表打开的第一个窗口
		# 切换到新窗口
		self.driver.switch_to.window(old_window)

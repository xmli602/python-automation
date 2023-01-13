# -*-coding:utf-8 -*-
# Author:xmLi

import time
from init import *

class BaiduLink(Init):
	def test_baidu_news(self):
		'''首页链接测试：验证新闻的链接'''
		self.driver.find_element_by_xpath("//a[contains(text(),'新闻')]").click()
		self.switch_new_window()
		self.assertIn('百度新闻',self.driver.title)

	# @unittest.skip('该功能已取消，忽略该条测试用例')
	def test_baidu_map(self):
		'''首页链接测试：验证地图的链接'''
		self.driver.find_element_by_xpath("//a[contains(text(),'地图')]").click()
		self.switch_new_window()
		self.assertIn('百度地图', self.driver.title)
		self.switch_old_window()

# 	@staticmethod
# 	def suite():
# 		'''将测试套件封装成一个方法'''
# 		# 按类加载测试用例
# 		suite = unittest.TestLoader().loadTestsFromTestCase(BaiduLink)
# 		return suite
#
# if __name__ == '__main__':
# 	unittest.TextTestRunner(verbosity=2).run(BaiduLink.suite())
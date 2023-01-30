# -*-coding:utf-8 -*-
# Author:xmLi


import requests

class Requests:
	'''请求方法的封装'''
	def request(self,url,method='get',**kwargs):
		if method == 'get':
			return requests.request(url=url,method=method,**kwargs)
		elif method =='post':
			return requests.request(url=url, method=method, **kwargs)

	def get(self,url,**kwargs):
		return self.request(url=url,**kwargs)

	def post(self,url,**kwargs):
		return self.request(url=url,method='post',**kwargs)
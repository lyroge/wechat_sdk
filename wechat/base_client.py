# -*- coding: UTF-8 -*-
"""
提供其他类别调用的基础
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from core import get_request_wechat_api
from core import post_request_wechat_api


class BaseClient(object):

    def __init__(self, access_token):
        self.access_token = access_token

    def get(self, path):
        query_string = 'access_token=%s' % self.access_token
        d = get_request_wechat_api(path, query_string)
        return d

    def post(self, path, data):
        query_string = 'access_token=%s' % self.access_token
        d = post_request_wechat_api(path, query_string, data)
        return d

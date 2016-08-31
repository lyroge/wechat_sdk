# -*- coding: UTF-8 -*-

from unittest import TestCase

from wechat.core import wechat_api_domain
from wechat.base import get_access_token_dict
from wechat.base import get_wechat_serverip_list

from settings import APPID, APPSECRET


class CoreTestCase(TestCase):

    def test_wechat_api_domain(self):
        """ 测试获取微信服务器域名
        """
        self.assertEqual(wechat_api_domain, 'api.weixin.qq.com')

    def test_get_access_token_dict(self):
        """ 测试获取access_token方法
        """
        d = get_access_token_dict(APPID, APPSECRET)
        key_true = 'access_token' in d and 'expires_in'
        self.assertTrue(key_true)

    def test_get_wechat_serverip_list(self):
        """ 获取微信服务器ip列表
        """
        access_token = get_access_token_dict(APPID, APPSECRET)

        d = get_wechat_serverip_list(access_token['access_token'])
        key_true = 'ip_list' in d

        self.assertTrue(key_true)

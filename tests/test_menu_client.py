# -*- coding: UTF-8 -*-

import json
from unittest import TestCase

from wechat.base import get_access_token_dict
from wechat.menu.client import Client

from settings import APPID, APPSECRET


class MenuClientTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        access_token = get_access_token_dict(APPID, APPSECRET)
        cls.client = Client(access_token['access_token'])

    def _check_json_result(self, d):
        errcode = d.get('errcode', 0)
        self.assertTrue(not errcode)

    def test_0_create_menu(self):
        data = {
            "button": [
                {
                    "type": "click",
                    "name": "abc",
                    "key": "V1001_TODAY_MUSIC"
                },
                {
                    "name": "def",
                    "sub_button": [
                        {
                            "type": "view",
                            "name": "a",
                            "url": "http://www.soso.com/"
                        },
                        {
                            "type": "view",
                            "name": "b",
                            "url": "http://v.qq.com/"
                        },
                        {
                            "type": "click",
                            "name": "c",
                            "key": "V1001_GOOD"
                        }
                    ]
                }
            ]
        }
        data = json.dumps(data)
        d = self.client.create_menu(data)
        self._check_json_result(d)

    def test_1_get_menu(self):
        """ 测试获取菜单功能
        """
        d = self.client.get_menu()
        self._check_json_result(d)

    def test_2_delete_menu(self):
        """ 测试删除菜单功能
        """
        d = self.client.delete_menu()
        self._check_json_result(d)

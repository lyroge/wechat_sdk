# -*- coding: UTF-8 -*-

from unittest import TestCase

from wechat.message import BaseHandler


class TestBaseHandler(BaseHandler):

    def on_text(self, xml_dict):
        print xml_dict['MsgType']


class BaseHandlerTestCase(TestCase):

    def test_on_text(self):
        """ 测试处理文本消息的方法
        """

        xml = """
        <xml>
         <ToUserName><![CDATA[toUser]]></ToUserName>
         <FromUserName><![CDATA[fromUser]]></FromUserName>
         <CreateTime>1348831860</CreateTime>
         <MsgType><![CDATA[text]]></MsgType>
         <Content><![CDATA[this is a test]]></Content>
         <MsgId>1234567890123456</MsgId>
        </xml>
        """

        test_hd = TestBaseHandler()
        test_hd(xml)

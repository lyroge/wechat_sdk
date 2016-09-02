# -*- coding: UTF-8 -*-

from unittest import TestCase

from wechat.message import BaseHandler


class TestBaseHandler(BaseHandler):

    def on_text(self, xml_dict):
        return 'text' == xml_dict['MsgType'] and 'Content' in xml_dict

    def on_image(self, xml_dict):
        return 'image' == xml_dict['MsgType'] and 'PicUrl' in xml_dict

    def on_voice(self, xml_dict):
        return 'voice' == xml_dict['MsgType'] and 'Format' in xml_dict

    def on_video(self, xml_dict):
        return 'video' == xml_dict['MsgType'] and 'ThumbMediaId' in xml_dict

    def on_shortvideo(self, xml_dict):
        return 'shortvideo' == xml_dict['MsgType'] and 'ThumbMediaId' in xml_dict

    def on_location(self, xml_dict):
        return 'location' == xml_dict['MsgType'] and 'Location_X' in xml_dict

    def on_link(self, xml_dict):
        return 'link' == xml_dict['MsgType'] and 'Title' in xml_dict

    def on_event_subscribe(self, xml_dict):
        """ 用户关注、包括扫码关注
        """
        return 'subscribe' == xml_dict['Event']

    def on_event_unsubscribe(self, xml_dict):
        """ 用户取消关注
        """
        return 'unsubscribe' == xml_dict['Event']

    def on_event_scan(self, xml_dict):
        """ 用户扫码进入场景
        """
        return 'SCAN' == xml_dict['Event']

    def on_event_location(self, xml_dict):
        """ 用户上报位置
        """
        return 'LOCATION' == xml_dict['Event'] and 'Longitude' in xml_dict

    def on_event_click(self, xml_dict):
        """ 用户点击菜单事件
        """
        return 'CLICK' == xml_dict['Event']


# 定义统一处理消息的类
test_hd = TestBaseHandler()


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
        r = test_hd(xml)
        self.assertTrue(r)

    def test_on_image(self):
        """ 测试处理图片的消息的方法
        """

        xml = """
        <xml>
             <ToUserName><![CDATA[toUser]]></ToUserName>
             <FromUserName><![CDATA[fromUser]]></FromUserName>
             <CreateTime>1348831860</CreateTime>
             <MsgType><![CDATA[image]]></MsgType>
             <PicUrl><![CDATA[this is a url]]></PicUrl>
             <MediaId><![CDATA[media_id]]></MediaId>
             <MsgId>1234567890123456</MsgId>
         </xml>
        """
        r = test_hd(xml)
        self.assertTrue(r)

    def test_on_voice(self):
        """ 测试处理语音的消息的方法
        """

        xml = """
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1357290913</CreateTime>
            <MsgType><![CDATA[voice]]></MsgType>
            <MediaId><![CDATA[media_id]]></MediaId>
            <Format><![CDATA[Format]]></Format>
            <MsgId>1234567890123456</MsgId>
        </xml>
        """
        r = test_hd(xml)
        self.assertTrue(r)

    def test_on_video(self):
        """ 测试处理视频的消息的方法
        """

        xml = """
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1357290913</CreateTime>
            <MsgType><![CDATA[video]]></MsgType>
            <MediaId><![CDATA[media_id]]></MediaId>
            <ThumbMediaId><![CDATA[thumb_media_id]]></ThumbMediaId>
            <MsgId>1234567890123456</MsgId>
        </xml>
        """
        r = test_hd(xml)
        self.assertTrue(r)

    def test_on_shortvideo(self):
        """ 测试处理小视频的消息的方法
        """

        xml = """
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1357290913</CreateTime>
            <MsgType><![CDATA[shortvideo]]></MsgType>
            <MediaId><![CDATA[media_id]]></MediaId>
            <ThumbMediaId><![CDATA[thumb_media_id]]></ThumbMediaId>
            <MsgId>1234567890123456</MsgId>
        </xml>
        """
        r = test_hd(xml)
        self.assertTrue(r)

    def test_on_location(self):
        """ 测试处理位置消息的方法
        """

        xml = """
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1351776360</CreateTime>
            <MsgType><![CDATA[location]]></MsgType>
            <Location_X>23.134521</Location_X>
            <Location_Y>113.358803</Location_Y>
            <Scale>20</Scale>
            <Label><![CDATA[位置信息]]></Label>
            <MsgId>1234567890123456</MsgId>
        </xml>
        """
        r = test_hd(xml)
        self.assertTrue(r)

    def test_on_link(self):
        """ 测试处理链接消息的方法
        """

        xml = """
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1351776360</CreateTime>
            <MsgType><![CDATA[link]]></MsgType>
            <Title><![CDATA[公众平台官网链接]]></Title>
            <Description><![CDATA[公众平台官网链接]]></Description>
            <Url><![CDATA[url]]></Url>
            <MsgId>1234567890123456</MsgId>
        </xml>
        """
        r = test_hd(xml)
        self.assertTrue(r)

    def test_on_event_subscribe(self):
        """ 测试处理关注消息的方法
        """

        xml = """
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[FromUser]]></FromUserName>
            <CreateTime>123456789</CreateTime>
            <MsgType><![CDATA[event]]></MsgType>
            <Event><![CDATA[subscribe]]></Event>
        </xml>
        """
        r = test_hd(xml)
        self.assertTrue(r)

    def test_on_event_unsubscribe(self):
        """ 测试处理关注消息的方法
        """

        xml = """
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[FromUser]]></FromUserName>
            <CreateTime>123456789</CreateTime>
            <MsgType><![CDATA[event]]></MsgType>
            <Event><![CDATA[unsubscribe]]></Event>
        </xml>
        """
        r = test_hd(xml)
        self.assertTrue(r)

    def test_on_event_scan(self):
        """ 测试处理扫码的方法
        """

        xml = """
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[FromUser]]></FromUserName>
            <CreateTime>123456789</CreateTime>
            <MsgType><![CDATA[event]]></MsgType>
            <Event><![CDATA[SCAN]]></Event>
            <EventKey><![CDATA[SCENE_VALUE]]></EventKey>
            <Ticket><![CDATA[TICKET]]></Ticket>
        </xml>
        """
        r = test_hd(xml)
        self.assertTrue(r)

    def test_on_event_location(self):
        """ 测试上报位置的方法（服务号的位置信息）
        """

        xml = """
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>123456789</CreateTime>
            <MsgType><![CDATA[event]]></MsgType>
            <Event><![CDATA[LOCATION]]></Event>
            <Latitude>23.137466</Latitude>
            <Longitude>113.352425</Longitude>
            <Precision>119.385040</Precision>
        </xml>
        """
        r = test_hd(xml)
        self.assertTrue(r)

    def test_on_event_click(self):
        """ 测试点击自定义菜单的事件
        """

        xml = """
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[FromUser]]></FromUserName>
            <CreateTime>123456789</CreateTime>
            <MsgType><![CDATA[event]]></MsgType>
            <Event><![CDATA[CLICK]]></Event>
            <EventKey><![CDATA[EVENTKEY]]></EventKey>
        </xml>
        """
        r = test_hd(xml)
        self.assertTrue(r)

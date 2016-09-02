# -*- coding: UTF-8 -*-

from unittest import TestCase

import xmltodict

from wechat.message import *


class TestResponse(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.d = {
            'from_user': 'from_user',
            'to_user': 'to_user',
            'create_time': 'create_time',
        }

        # 音频、图片
        cls.d.update({
            'media_id': 'media_id'
        })

        #  文本消息
        cls.d.update({
            'content': 'content'
        })

        # 视频
        cls.d.update({
            'title': 'title',
            'description': 'description'
        })

        # 多图文
        cls.d.update({
            'item_list': [
                {'title': 'title1', 'description': 'description1', 'picurl': 'picurl1', 'url': 'url1'}
            ]
        })

    def test_text_response(self):

        r = TextResponse(**self.d)

        d = xmltodict.parse(str(r))
        root = d['xml']

        self.assertEqual('text', root['MsgType'])

    def test_image_response(self):

        r = ImageResponse(**self.d)

        d = xmltodict.parse(str(r))
        root = d['xml']

        self.assertEqual('image', root['MsgType'])

    def test_voice_response(self):

        r = VoiceResponse(**self.d)

        d = xmltodict.parse(str(r))
        root = d['xml']

        self.assertEqual('voice', root['MsgType'])

    def test_video_response(self):

        r = VideoResponse(**self.d)

        d = xmltodict.parse(str(r))
        root = d['xml']

        self.assertEqual('video', root['MsgType'])

    def test_news_response(self):

        r = NewsResponse(**self.d)

        d = xmltodict.parse(str(r))
        root = d['xml']

        self.assertEqual('news', root['MsgType'])

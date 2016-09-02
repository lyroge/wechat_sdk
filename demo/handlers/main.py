# -*- coding: UTF-8 -*-

import tornado.ioloop
import tornado.web

from wechat.message import *


class MessageHandler(BaseHandler):
    def on_text(self, xml_dict):
        from_user = xml_dict['FromUserName']
        to_user = xml_dict['ToUserName']
        create_time = xml_dict['CreateTime']
        content = xml_dict['Content']

        text_response = TextResponse(from_user=from_user, to_user=to_user, create_time=create_time, content=content)
        return text_response

# 统一处理消息的类实例
hd = MessageHandler()

# 测试公众号
appid = 'wx863e67751855b610'
appsecret = 'd4624c36b6795d1d99dcf0547af5443d'


class MainHandler(tornado.web.RequestHandler):

    def get(self):

        # s = self.get_argument('s', '')
        # d = get_access_token_dict(appid, appsecret)

        s = 'ok'
        self.write(s)

    def post(self):
        # 处理消息
        body = self.request.body
        text = str(hd(body))

        self.write(text)

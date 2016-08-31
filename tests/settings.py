# -*- coding: UTF-8 -*-

import logging

stream_hd = logging.StreamHandler()

logger = logging.getLogger('wechat')
logger.setLevel(logging.INFO)
logger.addHandler(stream_hd)


# 微信公众号key
APPID = 'wx863e67751855b610'
APPSECRET = 'd4624c36b6795d1d99dcf0547af5443d'

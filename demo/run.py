# -*- coding: UTF-8 -*-

import tornado.ioloop
import tornado.web

from tornado.options import define, options

from settings import app_settings
from urls import url_patterns

# 定义默认的程序端口号
define("port", default=9999, type=int, help="port", metavar='server port')

tornado.options.parse_command_line()

application = tornado.web.Application(url_patterns, **app_settings)

if __name__ == "__main__":
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

# -*- coding: UTF-8 -*-

import logging

import xmltodict

logger = logging.getLogger(__name__)


class BaseHandler(object):

    def __call__(self, xml):
        self._dispatch(xml)

    def _dispatch(self, xml):
        logger.info('post xml:%s', xml)

        # 解析提交过来的数据
        d = xmltodict.parse(xml)

        # 获取提交信息的类别，分配到对应方法
        root = d['xml']
        msg_type = root['MsgType']

        meth = getattr(self, 'on_%s' % msg_type, None)
        r = meth(root)

        logger.info('return: %s', r)

        return r

    def on_text(self, xml_dict):
        pass

    def on_image(self, xml_dict):
        pass

    def on_voice(self, xml_dict):
        pass

    def on_video(self, xml_dict):
        pass

    def on_shortvideo(self, xml_dict):
        pass

    def on_location(self, xml_dict):
        pass

    def on_link(self):
        pass

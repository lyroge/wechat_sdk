# -*- coding: UTF-8 -*-

import logging

import xmltodict

logger = logging.getLogger(__name__)


class BaseHandler(object):

    def __call__(self, xml):
        return self._dispatch(xml)

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

    def on_link(self, xml_dict):
        pass

    def on_event(self, xml_dict):
        """ 事件信息分发
        """
        event = xml_dict['Event'].lower()

        meth = getattr(self, 'on_event_%s' % event, None)
        r = meth(xml_dict)

        return r

    def on_event_subscribe(self, xml_dict):
        """ 用户关注、包括扫码关注
        """
        pass

    def on_event_unsubscribe(self, xml_dict):
        """ 用户取消关注
        """
        pass

    def on_event_scan(self, xml_dict):
        """ 用户扫码进入场景
        """
        pass

    def on_event_location(self, xml_dict):
        """ 用户上报位置（服务号的位置信息）
        """
        pass

    def on_event_click(self, xml_dict):
        """ 用户点击菜单事件
        """
        pass

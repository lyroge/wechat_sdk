# -*- coding: UTF-8 -*-

from functools import partial
import requests

from wechat.constants import WECHAT_API_DOMAIN_LIST
from wechat.utils import logger


def get_api_domain():
    """ 获取第一个主域名
        说明：内部获取微信域名方法
    """
    return WECHAT_API_DOMAIN_LIST[0]

# 全局调用的微信服务域名
wechat_api_domain = get_api_domain()


def request_wechat_api(path, query_string='', data='', method='get'):
    """ 请求微信服务基础接口
    """

    url = 'https://%s/%s?%s' % (wechat_api_domain, path, query_string)

    args = [url]
    if data and method == 'post':
        args.append(data)

    # 获取方法
    meth = getattr(requests, method)
    r = meth(*args)

    # 输出请求相关日志
    logger.info('[%s]%s', method.upper(), args)

    d = r.json()

    # 如果查询结果出现问题，打印
    if d.get('errcode', 0):
        logger.error(d)

    return d

# 请求微信服务的get、post方法
get_request_wechat_api = partial(request_wechat_api)
post_request_wechat_api = partial(request_wechat_api, method='post')

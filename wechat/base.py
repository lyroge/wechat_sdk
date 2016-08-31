# -*- coding: UTF-8 -*-

from core import get_request_wechat_api


def get_access_token_dict(appid, appsecret):
    """ 获取access_token对象字典
    """
    path = 'cgi-bin/token'

    args = (appid, appsecret)
    query_string = 'grant_type=client_credential&appid=%s&secret=%s' % args

    d = get_request_wechat_api(path, query_string)
    return d


def get_wechat_serverip_list(access_token):
    path = 'cgi-bin/getcallbackip'
    query_string = 'access_token=%s' % access_token

    d = get_request_wechat_api(path, query_string)
    return d

微信公众平台SDK
=================

项目背景
--------
从2014年开始玩微信公众平台，试用过其中大多数的功能，如：消息回复、自定义菜单、公众号中的支付，页面授权等。之前的程序中都是直接调用公众平台的接口，这样复用功能无法实现。现将功能独立出单独模块

目前完成
-----------
* 获取access_token方法
* 获取微信服务器IP地址
* 自定义菜单中的查询、创建、删除（不包括个性化菜单接口）
* 消息管理中的接收普通消息、接收事件推送
* 消息管理中的被动回复用户消息
* 添加tornado代码的demo实例

使用示例
-----------

获取access_token方法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::  
    
    from wechat.base import get_access_token_dict
    
    get_access_token_dict(APPID, APPSECRET)


消息处理基类
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

继承基础的消息处理类BaseHandler， 重写对应方法即可。 如文本、图片、视频等对应的处理方法分别问on_text、on_image、on_video。

::

    from wechat.message import *

    class MessageHandler(BaseHandler):
    
      def on_text(self, xml_dict):
      
          from_user = xml_dict['FromUserName']
          to_user = xml_dict['ToUserName']
          create_time = xml_dict['CreateTime']
          content = xml_dict['Content']
  
          text_response = TextResponse(from_user=from_user, to_user=to_user, create_time=create_time, content=content)
          return text_response
          

自定义菜单接口
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    from wechat.menu.client import Client
    
    client = Client(access_token['access_token'])
    
    # 创建菜单
    client.create_menu(data)
    
    # 获取菜单
    client.get_menu()
    
    # 删除菜单
    client.delete_menu()
    

下一步计划
-------------
1. 继续补充其他常用接口

**感兴趣的同学可以加入到项目中一起完善**

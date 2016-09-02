# -*- coding: UTF-8 -*-


class BaseResponse(object):
    """ 公众号回复消息基类
    """

    # 模板中有哪些key
    allow_key_list = []

    # 回复的消息模板字符串
    xml_str_template = ''

    def __init__(self, **kwargs):
        for k in self.allow_key_list:
            v = kwargs.pop(k, '')
            setattr(self, k, v)

    def __str__(self):
        d = dict((k, getattr(self, k)) for k in self.allow_key_list)
        return self.xml_str_template.format(**d)


class TextResponse(BaseResponse):
    """ 公众号回复文本消息
    """

    allow_key_list = ['to_user', 'from_user', 'create_time', 'content']

    xml_str_template = """
    <xml>
        <ToUserName><![CDATA[{to_user}]]></ToUserName>
        <FromUserName><![CDATA[{from_user}]]></FromUserName>
        <CreateTime>{create_time}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{content}]]></Content>
    </xml>
    """


class ImageResponse(BaseResponse):
    """ 公众号回复图片消息
    """

    allow_key_list = ['to_user', 'from_user', 'create_time', 'media_id']

    xml_str_template = """
    <xml>
        <ToUserName><![CDATA[{to_user}]]></ToUserName>
        <FromUserName><![CDATA[{from_user}]]></FromUserName>
        <CreateTime>{create_time}</CreateTime>
        <MsgType><![CDATA[image]]></MsgType>
        <Image>
            <MediaId><![CDATA[{media_id}]]></MediaId>
        </Image>
    </xml>
    """


class VoiceResponse(BaseResponse):
    """ 公众号回复语音消息
    """

    allow_key_list = ['to_user', 'from_user', 'create_time', 'media_id']

    xml_str_template = """
    <xml>
        <ToUserName><![CDATA[{to_user}]]></ToUserName>
        <FromUserName><![CDATA[{from_user}]]></FromUserName>
        <CreateTime>{create_time}</CreateTime>
        <MsgType><![CDATA[voice]]></MsgType>
        <Voice>
            <MediaId><![CDATA[media_id]]></MediaId>
        </Voice>
    </xml>
    """


class VideoResponse(BaseResponse):
    """ 公众号回复视频消息
    """

    allow_key_list = ['to_user', 'from_user', 'create_time', 'media_id', 'title', 'description']

    xml_str_template = """
    <xml>
        <ToUserName><![CDATA[{to_user}]]></ToUserName>
        <FromUserName><![CDATA[{from_user}]]></FromUserName>
        <CreateTime>{create_time}</CreateTime>
        <MsgType><![CDATA[video]]></MsgType>
        <Video>
            <MediaId><![CDATA[{media_id}]]></MediaId>
            <Title><![CDATA[{title}]]></Title>
            <Description><![CDATA[{description}]]></Description>
        </Video>
    </xml>
    """


class NewsResponse(BaseResponse):
    """ 公众号回复图文消息
    """

    allow_key_list = ['to_user', 'from_user', 'create_time', 'item_list']

    xml_str_template = """
    <xml>
        <ToUserName><![CDATA[{to_user}]]></ToUserName>
        <FromUserName><![CDATA[{from_user}]]></FromUserName>
        <CreateTime>{create_time}</CreateTime>
        <MsgType><![CDATA[news]]></MsgType>
        <ArticleCount>{article_count}</ArticleCount>
        <Articles>{articles}</Articles>
        </xml>
    """

    item_str_template = """
        <item>
            <Title><![CDATA[{title}]]></Title>
            <Description><![CDATA[{description}]]></Description>
            <PicUrl><![CDATA[{picurl}]]></PicUrl>
            <Url><![CDATA[{url}]]></Url>
        </item>
    """

    def __str__(self):
        item_list = self.item_list
        article_count = len(item_list)

        articles = ''
        for item in item_list:
            articles += self.item_str_template.format(**item)

        d = {
            'from_user': self.from_user,
            'to_user': self.to_user,
            'create_time': self.create_time,
            'article_count': article_count,
            'articles': articles
        }
        return self.xml_str_template.format(**d)

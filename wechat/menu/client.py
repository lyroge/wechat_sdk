# -*- coding: UTF-8 -*-

from wechat.base_client import BaseClient


class Client(BaseClient):
    """ 操作菜单创建、产出、查询的客户端
    """
    base_path = 'cgi-bin/menu/'

    def get_menu(self):
        path = self.base_path + 'get'
        d = self.get(path)
        return d

    def create_menu(self, data):
        path = self.base_path + 'create'
        d = self.post(path, data)
        return d

    def delete_menu(self):
        path = self.base_path + 'delete'
        d = self.get(path)
        return d

# -*- encoding:utf-8 -*-

__author__ = 'devin'
__date__ = '2018/12/24/024 13:26'


class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def build_url(path):
        return path

    @staticmethod
    def build_static_url(path):
        ver = "%s" % (22222222)
        path = "/static" + path + "?ver=" + ver
        return UrlManager.build_url(path)

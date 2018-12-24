# -*- encoding:utf-8 -*-

__author__ = 'devin'
__date__ = '2018/12/24/024 14:03'

from application import app
from web.controllers.index import route_index

app.register_blueprint(route_index, url_prefix="/")

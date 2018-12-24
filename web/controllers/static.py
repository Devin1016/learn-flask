# -*- encoding:utf-8 -*-

__author__ = 'devin'
__date__ = '2018/12/24/024 15:50'

from flask import Blueprint, send_from_directory

from application import app

route_static = Blueprint("static", __name__)


@route_static.route("/<path:filename>")
def index(filename):
    return send_from_directory(app.root_path + "/web/static/", filename)

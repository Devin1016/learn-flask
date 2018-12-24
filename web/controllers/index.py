# -*- encoding:utf-8 -*-

__author__ = 'devin'
__date__ = '2018/12/24/024 14:46'

from flask import Blueprint, render_template

route_index = Blueprint("index_page", __name__)


@route_index.route("/")
def index():
    return render_template("index/index.html")

#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file:errors.py
@file_author:lgd
@edit_time:2021/05/16
@fun_desc:
"""
from flask import render_template

from myapp import db
from myapp.views.routes import blue


@blue.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@blue.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

if __name__ == '__main__':
    pass

#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file:__init__.py
@file_author:lgd
@edit_time:2021/05/09
@fun_desc:
"""
import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from myapp.models import db, login
from myapp.settings import envs
from myapp.views.routes import blue
from . import views
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(envs.get('develop'))
    app.register_blueprint(blueprint=blue)
    db.init_app(app)
    migrate.init_app(app=app, db=db)
    login.init_app(app=app)
    login.login_view = 'first_blue.login'
    Bootstrap(app=app)

    print("打印是否调试", app.debug)
    if not app.debug:
        print("打印环境邮箱服务器地址", app.config['MAIL_SERVER'])
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            secure = None
            if app.config['MAIL_USE_TLS']:
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                toaddrs=app.config['ADMINS'], subject='Microblog Failure',
                credentials=auth, secure=secure)
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

    return app

if __name__ == '__main__':
    pass

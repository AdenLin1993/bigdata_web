#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file:settings.py
@file_author:lgd
@edit_time:2021/05/12
@fun_desc:
"""
print(__name__, "加载环境设置！")
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'templates')
STATIC_FOLDER = os.path.join(BASE_DIR, 'static')

def get_db_url(dbinfo):

    ENGING = dbinfo.get('ENGING') or 'mysql'
    DRIVER = dbinfo.get('DRIVER') or 'pymysql'
    USER = dbinfo.get('USER') or 'root'
    PASSWORD = dbinfo.get('PASSWORD') or 'rock1204'
    HOST = dbinfo.get('HOST') or 'localhost'
    PORT = dbinfo.get('PORT') or '3306'
    NAME = dbinfo.get('NAME') or 'test'

    return "{}+{}://{}:{}@{}:{}/{}".format(ENGING, DRIVER, USER, PASSWORD, HOST, PORT, NAME)

class Config:
    DEBUG = False
    TESTING = False
    POSTS_PER_PAGE = 3
    SECRET_KEY = "1277033771carey"
    SESSION_TYPE = "redis"
    # SQLALCHEMY_TRACK_MODIFICATIONS配置项用于设置数据发生变更之后是否发送信号给应用，我不需要这项功能，因此将其设置为False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 添加邮件设置，通过电子邮件发送错误
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SERVER = '127.0.0.1'
    MAIL_PORT = 1000
    MAIL_USE_TLS = 1
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['15016259750@139.com']

class DevelopConfig(Config):
    DEBUG = False

    DATABASE = {
        'ENGING': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'Lin1277033771',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'bigdata_web_dev'
    }

    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)

class TestingConfig(Config):
    TESTING = True

    DATABASE = {
        'ENGING': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'rock1204',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'Python1804FlaskProjectTesting'
    }

    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)

class StagingConfig(Config):

    DATABASE = {
        'ENGING': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'rock1204',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'Python1804FlaskProjectStaging'
    }

    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)

class ProductConfig(Config):

    DATABASE = {
        'ENGING': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'rock1204',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'Python1804FlaskProjectProduct'
    }

    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)

envs = {
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'product': ProductConfig
}

if __name__ == '__main__':
    pass

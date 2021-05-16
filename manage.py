#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file:manage.py
@file_author:lgd
@edit_time:2021/05/09
@fun_desc:web control scrip
"""

from flask_migrate import MigrateCommand
from flask_script import Manager
from myapp import create_app

app = create_app()
manager = Manager(app=app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

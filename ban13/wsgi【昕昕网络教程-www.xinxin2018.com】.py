#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname

# 设置当前目录为工作目录
sys.path.insert(0, abspath(dirname(__file__)))

# 引入 app.py
import app

# 必须有一个叫做 application 的变量
# gunicorn 就要这个变量
# 这个变量的值必须是 Flask 实例
# 这是规定的套路(协议)
application = app.app

# 这是把代码部署到 apache gunicorn nginx 后面的套路
"""
这个文件夹下写一个xx.conf
➜  ~ cat /etc/supervisor/conf.d/xx.conf

内容是如下的套路 哪个目录下的 自动重启
[program:todo]
command=/usr/local/bin/gunicorn wsgi --bind 0.0.0.0:2000 --pid /tmp/todo.pid
directory=/root/web13
autostart=true
"""

# 服务器上编辑文本用nano
service 命令最大 可以把服务器停掉
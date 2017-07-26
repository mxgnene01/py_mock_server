#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Meng xiangguo <mxgnene01@gmail.com>
#
#              _____               ______
#     ____====  ]OO|_n_n__][.      |    |]
#    [________]_|__|________)<     |MENG|
#     oo    oo  'oo OOOO-| oo\_   ~o~~~o~'
# +--+--+--+--+--+--+--+--+--+--+--+--+--+
#                        17/5/19  下午10:28
#
from mock.common.app import WebApplication, run_app
import logging
import random
import time
import torndb
from tornado.options import (define as tornado_define,
                             options as tornado_options,
                             parse_command_line)

tornado_define('mysql_host', default='10.36.2.22', help='mysql host')
tornado_define('mysql_port', default=3306, help='mysql port')
tornado_define('mysql_username', default='ymall_mobile', help='username')
tornado_define('mysql_password', default='pwd:hfh36FVBv', help='password')
tornado_define('mysql_dbname', default='mockserver', help='database')

DB = torndb.Connection(tornado_options.mysql_host, tornado_options.mysql_dbname,
                       tornado_options.mysql_username, tornado_options.mysql_password)

LOG = logging.getLogger('tornado.application')

class MockServer(WebApplication):

    enabled_apps = ['mock.apps.rewrite',
                    'mock.apps.keepalive']

    def before_run(self, io_loop):
        random.seed(time.time())
        LOG.info('starting mock server ...')


def run():
    run_app(MockServer)

if __name__ == '__main__':
    run()
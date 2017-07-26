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
from tornado.gen import coroutine, Task, Return
import logging
from mock.commands.server import DB

BIZLOG = logging.getLogger("mock.business")

def get_result(domain, uri):
    result = DB.query("SELECT parms, expect "
                      "FROM interface_mock "
                      "WHERE status = 1 and domain = '%s' and uri = '%s'" % (domain, uri))
    return result
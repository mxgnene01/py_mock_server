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
from mock.apps.rewrite import services
from mock.common.route import route
from mock.common import controller
from tornado.gen import coroutine
from tornado.httpclient import HTTPClient


@route('(.*)')
class MockRewriteController(controller.APIBaseController):

    @coroutine
    def get(self, uri):
        domain = self.request.host
        yield self.request_handler(domain, uri)

    @coroutine
    def post(self, uri):
        domain = self.request.host
        yield self.request_handler(domain,uri)


    def request_handler(self, domain, uri):
        responses = services.get_result(domain, uri)
        origin_args = self.request.arguments

        status, index = self.parms_is_equal(responses, origin_args)

        if status:
            try:
                self.finish(responses[index]['expect'])
            except:
                self.set_status(500)
                self.reply(dict(status=5002, reason=responses[index]))
        else:
            url = self.request.protocol + "://" + self.request.host + self.request.uri + self.request.query
            http_client = HTTPClient()
            temp = http_client.fetch(url)
            self.finish(temp.body)

    def parms_is_equal(self, responses, origin_args):
        dict_parms = {}
        ismock = False
        # 为了返回结果list 的index
        index = -1
        if len(responses) > 0 :
            for response in responses:
                index += 1
                parms = response['parms'].split('&')

                for parm in parms:
                    origin_key = parm.split("=")[0]
                    origin_val = parm.split("=")[1]
                    dict_parms[origin_key] = [origin_val]

                if cmp(origin_args, dict_parms) == 0:
                    ismock = True

        return ismock, index
import json
from odoo import http
from odoo.http import request

# class ExtTrigger(http.Controller):
#
#     @http.route(['/service/trigger'], type='json', auth='none')
#     def eval_trigger(self):
#         return {
#             'rendered_html': False,
#             'error': "No display found",
#             'id':'1234'
#         }
#
#
# class ExtAction(http.Controller):
#
#     @http.route(['/service/action'], type='json', auth='none')
#     def exec_action(self):
#         return {
#             'rendered_html': False,
#             'error': "No display found",
#             'id': '1234'
#         }
#
#
# class ExtAuth(http.Controller):
#
#     @http.route(['/service/auth'], type='json', auth='none')
#     def exec_action(self):
#         return {
#             'code': 200,
#             'status': True,
#             'id': '1234'
#         }










class ExtTrigger(http.Controller):

    @http.route(['/service/trigger'], type='http', auth='none', method='GET', cors='*')
    def eval_trigger(self):
        resp = 'This is a test'
        return request.make_response(['rendered_html','error'], {
            'Cache-Control': 'no-cache',
            'Content-Type': 'text/html; charset=utf-8',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
        })


class ExtAction(http.Controller):

    @http.route(['/service/action'], type='http', auth='none')
    def exec_action(self):
        return {
            'rendered_html': False,
            'error': "No display found",
            'id': '1234'
        }


class ExtAuth(http.Controller):

    @http.route(['/service/auth'], type='http', auth='none')
    def exec_action(self):
        return {
            'code': 200,
            'status': True,
            'id': '1234'
        }
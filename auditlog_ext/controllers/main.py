import json
from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class ExtTrigger(http.Controller):

    @http.route(['/service/trigger'], type='json', auth='none')
    def eval_trigger(self, **kwargs):
        ret_dict = dict()
        _logger.info("*********************************")
        _logger.info(request)
        _logger.info("*********************************")
        return {
            'rendered_html': False,
            'error': "No display found"
        }


class ExtAction(http.Controller):

    @http.route(['/service/action'], type='json', auth='none')
    def exec_action(self):
        return {
            'rendered_html': False,
            'error': "No display found",
            'id': '1234'
        }


class ExtAuth(http.Controller):

    @http.route(['/service/auth'], type='json', auth='none')
    def exec_action(self):
        return {
            'code': 200,
            'status': True,
            'id': '1234'
        }




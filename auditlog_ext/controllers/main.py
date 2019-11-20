import json
from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class ExtTrigger(http.Controller):

    @http.route(['/service/trigger'], type='json', auth='none')
    def eval_trigger(self, **kwargs):
        ret_dict = dict(rendered_html=False,error='None')
        if request.httprequest and request.httprequest.args:
            for k, v in request.httprequest.args.items():
                if k == 'id':
                    ret_dict.update({k:v})
                _logger.info(k)
                _logger.info(v)
        _logger.info(ret_dict)
        return ret_dict


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
    def exec_action(self, **kwargs):
        return {'id':None}




import json
from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class ExtTrigger(http.Controller):

    @http.route(['/service/trigger'], type='json', auth='none')
    def eval_trigger(self, **kwargs):
        ret_dict = dict(code=200,msg='None')
        if request.httprequest and request.httprequest.args and ('id' in request.httprequest.args):
            if request.env['subscribe.app'].sudo().search_count([('current_token', '=', request.httprequest.args.get('id',0)),\
                                                          ('state','=','active')]):
                _logger.info(request.httprequest.args.get('id',0))
                _logger.info(request.httprequest.args.get('model', 0))
                _logger.info(request.httprequest.args.get('action', 0))
                rule = request.env['auditlog.rule'].sudo().search([('subscribe_app_id.current_token','=',\
                                                             request.httprequest.args.get('id',0)),\
                                                            ('model_id.model','=',\
                                                             request.httprequest.args.get('model','')),\
                                                            ('log_'+request.httprequest.args.get('action',''),'=',True)])
                if rule:
                    ret_dict.update({'msg':'Success'})
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
        ret_dict = dict(code=200, logged=False)
        if request.httprequest and request.httprequest.args:
            for k, v in request.httprequest.args.items():
                if k == 'id' and request.env['subscribe.app'].sudo().search_count([('current_token', '=', v),\
                                                                            ('state','=','active')]):
                    ret_dict.update({'logged':True})
        return ret_dict




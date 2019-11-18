from odoo import http
from odoo.http import request

class ExtTrigger(http.Controller):

    @http.route(['/service/trigger'], type='json', auth='none')
    def eval_trigger(self):
        return {
            'rendered_html': False,
            'error': "No display found",
        }


class ExtAction(http.Controller):

    @http.route(['/service/action'], type='json', auth='none')
    def exec_action(self):
        return {
            'rendered_html': False,
            'error': "No display found",
        }


class ExtAuth(http.Controller):

    @http.route(['/service/auth'], type='json', auth='none')
    def exec_action(self):
        return {
            'code': 200,
            'status': True,
        }
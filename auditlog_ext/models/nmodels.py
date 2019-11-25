# -*- coding: utf-8 -*-

from uuid import uuid4
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models, _, tools


class SubscribeApp(models.Model):
    _name = 'subscribe.app'
    _description = "Subscribe App"

    name = fields.Char()
    url = fields.Char()
    current_token = fields.Char('Current UUID', compute='_get_current_token', store=True)
    subscribe_app_line_ids = fields.One2many('subscribe.app.line', 'subscribe_app_id', 'Tokens')
    state = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')],
        string='Status', required=True, tracking=True, copy=False, default='active')


    @api.depends('subscribe_app_line_ids')
    def _get_current_token(self):
        for record in self:
            record.current_token = record.subscribe_app_line_ids and \
                                   record.subscribe_app_line_ids.\
                                   sorted(key=lambda app: app.sequence, reverse=False)[0].name or ''

    def create_token(self):
        sal_obj = self.env['subscribe.app.line']
        for record in self:
            sequence = record.subscribe_app_line_ids and \
                                   record.subscribe_app_line_ids.\
                                   sorted(key=lambda app: app.sequence, reverse=False)[0].sequence or 10
            sal_obj.create({'sequence':sequence-1})


    def set_active(self):
        self.ensure_one()
        self.state = 'active'


    def set_disabled(self):
        self.ensure_one()
        self.state = 'inactive'


    def generate_uuid(self):
        self.ensure_one()
        sequence = self.subscribe_app_line_ids and (self.subscribe_app_line_ids[0].sequence - 1) or 10
        self.env['subscribe.app.line'].create({'sequence':sequence,'subscribe_app_id':self.id})



class SubscribeAppLine(models.Model):
    _name = 'subscribe.app.line'
    _description = "Subscribe App Line"
    _order = 'sequence, id'

    name = fields.Char('UUID', size=50, index=True, default=lambda self: str(uuid4()), copy=False)
    sequence = fields.Integer(default=10, index=True)
    subscribe_app_id = fields.Many2one('subscribe.app', 'Subscribe App')

# -*- coding: utf-8 -*-

from odoo import api, fields, models, _, tools


class AuditLogInh(models.Model):
    _inherit = 'auditlog.log'

    subscribe_app_id = fields.Many2one('subscribe.app', string='Apps subscribed')
    external = fields.Boolean(compute='_get_external', store=True)

    @api.depends('subscribe_app_id')
    def _get_external(self):
        for record in self:
            record.external = self.subscribe_app_id and True or False



class AuditLogRuleInh(models.Model):
    _inherit = 'auditlog.rule'

    subscribe_app_id = fields.Many2one('subscribe.app', string='Apps subscribed')
    external = fields.Boolean(compute='_get_external', store=True)

    @api.depends('subscribe_app_id')
    def _get_external(self):
        for record in self:
            record.external = self.subscribe_app_id and True or False



class AuditLogHttpSessionInh(models.Model):
    _inherit = 'auditlog.http.session'

    subscribe_app_id = fields.Many2one('subscribe.app', string='Apps subscribed')
    external = fields.Boolean(compute='_get_external', store=True)

    @api.depends('subscribe_app_id')
    def _get_external(self):
        for record in self:
            record.external = self.subscribe_app_id and True or False



class AuditLogHttpRequestInh(models.Model):
    _inherit = 'auditlog.http.request'

    subscribe_app_id = fields.Many2one('subscribe.app', string='Apps subscribed')
    external = fields.Boolean(compute='_get_external', store=True)

    @api.depends('subscribe_app_id')
    def _get_external(self):
        for record in self:
            record.external = self.subscribe_app_id and True or False
# -*- coding: utf-8 -*-

import time
import math
import re

from uuid import uuid4
from odoo.osv import expression
from odoo.tools.float_utils import float_round as round, float_compare
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models, _, tools
from odoo.tests.common import Form


class SubscribeApp(models.Model):
    _name = 'subscribe.app'

    name = fields.Char()
    url = fields.Char()
    token = fields.Char('UUID', size=50, index=True, default=lambda self: str(uuid4()), copy=False)
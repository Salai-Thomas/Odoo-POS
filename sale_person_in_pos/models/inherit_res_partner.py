# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritResPartner(models.Model):
    _inherit = 'res.partner'

    is_sale_person = fields.Boolean("Sale Person",default=False)



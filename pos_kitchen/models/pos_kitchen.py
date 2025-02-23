# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PosKitchen(models.Model):
    _name = 'pos.kitchen'

    sequence = fields.Char("Sequence")
    pos_config_id = fields.Many2one("pos.config",string="Allowed POS",help="Allowed POS For Kitchen")
    pos_category = fields.Many2one("pos.category",string="Allowed POS Category",help="Allowed POS Category For Kitchen")


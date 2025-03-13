# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PosPreparationDisplayStage(models.Model):
    _inherit = 'pos_preparation_display.stage'

    is_noti = fields.Boolean("Noti To Preparation")


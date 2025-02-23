# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PosKitchen(models.Model):
    _name = 'pos.kitchen'

    sequence= fields.Char("Sequence")



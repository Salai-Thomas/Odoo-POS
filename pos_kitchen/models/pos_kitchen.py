# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PosKitchen(models.Model):
    _name = 'pos.kitchen'

    sequence = fields.Char(readonly=True, default='New',copy=False, tracking=True, help="Sequence of items")

    def _pos_config_id(self):
        """Domain for pos_config-id"""
        kitchen = self.search([])
        if kitchen:
            return [("module_pos_restaurant","=",True),
                    ("id","not in",[rec.id for rec in kitchen.pos_config_id])]
        else:
            return [("module_pos_restaurant","=",True)]

    pos_config_id = fields.Many2one("pos.config",domain=_pos_config_id,string="Allowed POS",help="Allowed POS For Kitchen")
    pos_category = fields.Many2one("pos.category",string="Allowed POS Category",help="Allowed POS Category For Kitchen")

    @api.model
    def create(self, vals):
        """To Create sequence"""
        if vals.get(self.sequence,"New" == "New") :
            vals['sequence'] = self.env['ir.sequence'].next_by_code('pos.kitchen')

        result = super(PosKitchen, self).create(vals)
        return result



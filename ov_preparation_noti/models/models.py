# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ov_preparation_noti(models.Model):
#     _name = 'ov_preparation_noti.ov_preparation_noti'
#     _description = 'ov_preparation_noti.ov_preparation_noti'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


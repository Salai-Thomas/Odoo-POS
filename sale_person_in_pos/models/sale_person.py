from odoo import fields, models

class SalePerson(models.Model):
    _name = 'sale.person'
    _description = 'SalePerson'

    name = fields.Char("Sale Person")
    


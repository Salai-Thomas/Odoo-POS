from odoo import models,fields

class InheritPosOrders(models.Model):
    _inherit = "pos.order"

    def check_order_status(self,order):
        if order:
            pos_orders = self.env['pos.order'].search([("pos_reference","=",order)])
            print(pos_orders,'======================pos_orders')



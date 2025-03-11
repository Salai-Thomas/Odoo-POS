from odoo import models,fields

class InheritPosOrders(models.Model):
    _inherit = "pos.order"

    def check_order_status(self,order):
        if order:
            print(order,'====================order')
            print(type(order),"========================type of order")

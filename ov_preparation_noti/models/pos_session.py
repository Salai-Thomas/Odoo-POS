from odoo import fields, models


class PosSession(models.Model):
    _inherit = 'pos.session'

    def change_order_stage(self,id):
        rec = self.search([['id','=',id]])
        session_name = rec.name
        print(session_name,'=============session_name')
        channel = rec._get_bus_channel_name()

        self.env['bus.bus']._sendone(channel,"change_order_stage",{"message":"change_order_stage"})
        print(channel,"=======================")

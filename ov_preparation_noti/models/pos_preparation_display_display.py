from odoo import models,fields

class PosPreparationDisplay(models.Model):
    _inherit = 'pos_preparation_display.display'


    # stage_ids = fields.One2many('pos_preparation_display.stage', 'preparation_display_id', string="Stages", default=[
    #     {'name': 'To prepare', 'color': '#6C757D', 'is_noti':False,'alert_timer': 10},
    #     {'name': 'Ready', 'color': '#4D89D1','is_noti':False, 'alert_timer': 5},
    #     {'name': 'Completed', 'color': '#4ea82a','is_noti':False, 'alert_timer': 0}
    # ])
    #
    # def get_preparation_display_data(self):
    #     return {
    #         'categories': self._get_pos_category_ids().read(['id', 'display_name', 'sequence']),
    #         'stages': self.stage_ids.read(['name','color','is_noti']),
    #         'orders': self.env["pos_preparation_display.order"].get_preparation_display_order(self.id),
    #         'attributes': self.env['product.attribute'].search([]).read(['id', 'name']),
    #         'attribute_values': self.env['product.template.attribute.value'].search([]).read(['id', 'name', 'attribute_id']),
    #     }
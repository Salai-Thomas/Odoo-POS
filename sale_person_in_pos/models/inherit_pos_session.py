from odoo import api, fields, models

class InheritPosSession(models.Model):
    _inherit = 'pos.session'

    def _pos_ui_models_to_load(self):
        result = super()._pos_ui_models_to_load()
        new_model = 'sale.person'
        if new_model not in result:
            result.append(new_model)
        return result

    def _loader_params_sale_person(self):
        return {
            'search_params': {
                'fields': ['name'],
            },
        }

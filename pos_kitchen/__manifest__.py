# -*- coding: utf-8 -*-
{
    'name': "pos_kitchen",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale','pos_restaurant'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/pos_kitchen.xml',
    ],

    'assets':{
        'point_of_sale._assets_pos': [
            'pos_kitchen/static/src/js/order_button.js',
        ],
        'web.assets_backend': [
            'pos_kitchen/static/src/js/kitchen_screen.js',
            'pos_kitchen/static/src/xml/kitchen_screen.xml',
        ],
    }

}


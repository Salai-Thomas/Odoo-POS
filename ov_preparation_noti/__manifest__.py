# -*- coding: utf-8 -*-
{
    'name': "Preparation Notification",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "odoo VERSE",
    'category': 'Point Of Sale',
    'version': '17.0.1.0.0',
    'depends': ['base','pos_preparation_display'],
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],

    'assets': {
        'pos_preparation_display.assets': [
            'ov_preparation_noti/static/src/app/components/override/order/order.js'
        ],

    },

    'license': 'OEEL-1',
    'installable': True,
    'auto_install': False,
    'application': False,
    "images": [
        "static/description/icon.png",
    ],
}


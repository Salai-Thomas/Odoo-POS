# -*- coding: utf-8 -*-
{
    'name': "sale_person_in_pos",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale','sale'],

    'data': [
        'security/ir.model.access.csv',
        'views/inherit_res_partner.xml',
        'views/sale_person.xml',
    ],

}


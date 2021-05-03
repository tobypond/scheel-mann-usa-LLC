# -*- coding: utf-8 -*-
{
    'name': "Scheel Mann LLC Purchase",

    'summary': """Product Variant Costs on Purchase Order""",

    'description': """
        [2466472] Pull product variant costs into purchase order line description and total cost
        """,

    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com/',

    'category': 'Custom Development',
    'version': '1.0',
    'license': 'OEEL-1',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],

    # always loaded
    'data': [
        'views/product_attribute_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'application': False,
}

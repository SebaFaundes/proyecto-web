# -*- coding: utf-8 -*-
{
    'name': "recursos",

    'summary': """
        Módulo de inventario general""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Sebatián Faúndes",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/view_inventario.xml',
        # 'views/view_proveedor.xml',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #   'demo/demo.xml',
    #],
}
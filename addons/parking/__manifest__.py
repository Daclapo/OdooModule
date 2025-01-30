# -*- coding: utf-8 -*-
{
    'name': "Gestión de garajes",

    'summary': """
        Gestión de plazas de aparcamiento""",

    'description': """
        Módulo de ejemplo para 2º DAM de SGE
    """,

    'author': "Profesor SGE",
    'website': "http://www.sgecompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/parking_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/parking_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # Se indica que es una aplicación
    'application': True,
}

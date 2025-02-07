# -*- coding: utf-8 -*-
{
    'name': "Dgb Clinica Veterinaria",

    'summary': """
       Clinica veterinaria de David Gonzalo Barroso""",

    'description': """
        Aplicacion de un centro veterinario que permite gestionar el inventario de productos,
        a los medicos veterinarios en plantilla, a los dueños de mascotas registrados
        y las mascotas.
    """,

    'author': "David Gonzalo Barroso",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/dgb_clinica_veterinaria_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/dgb_clinica_veterinaria_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

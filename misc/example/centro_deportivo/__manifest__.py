# -*- coding: utf-8 -*-
{
    'name': "Centro Deportivo Hugo",

    'description': """
        Este módulo ha sido creado para la gestión de centros deportivos.
    """,

    'author': "Hugo Córdoba",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/centro_deportivo_security.xml',
        'security/ir.model.access.csv',
        'views/main_menu.xml',
        'views/cliente_view.xml',
        'views/servicio_view.xml',
        'views/trabajador_view.xml',
        'views/centro_view.xml',
        'data/centro_deportivo_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # Se indica que es una aplicación
    'application': True,
}
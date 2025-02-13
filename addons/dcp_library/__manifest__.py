# -*- coding: utf-8 -*-
{
    'name': "dcp_library",

    'summary': "Modulo para la gestion de prestamos de libros en bibliotecas",

    'description': """
Este es un módulo creado para la gestion de prestamos de libros en bibliotecas, el cual permite llevar un control de los libros prestados, los libros disponibles, los usuarios que han solicitado un libro, los usuarios que han devuelto un libro, entre otros.
    """,

    'author': "David Clarkson Postigo",
    'website': "https://iesclaradelrey.es/portal/index.php/es/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/dcp_library_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],


}

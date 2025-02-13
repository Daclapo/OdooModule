# -*- coding: utf-8 -*-
# from odoo import http


# class LibraryPrueba(http.Controller):
#     @http.route('/library_prueba/library_prueba', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_prueba/library_prueba/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_prueba.listing', {
#             'root': '/library_prueba/library_prueba',
#             'objects': http.request.env['library_prueba.library_prueba'].search([]),
#         })

#     @http.route('/library_prueba/library_prueba/objects/<model("library_prueba.library_prueba"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_prueba.object', {
#             'object': obj
#         })


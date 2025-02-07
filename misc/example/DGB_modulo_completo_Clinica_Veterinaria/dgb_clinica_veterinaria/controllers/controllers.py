# -*- coding: utf-8 -*-
# from odoo import http


# class DgbClinicaVeterinaria(http.Controller):
#     @http.route('/dgb_clinica_veterinaria/dgb_clinica_veterinaria', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dgb_clinica_veterinaria/dgb_clinica_veterinaria/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dgb_clinica_veterinaria.listing', {
#             'root': '/dgb_clinica_veterinaria/dgb_clinica_veterinaria',
#             'objects': http.request.env['dgb_clinica_veterinaria.dgb_clinica_veterinaria'].search([]),
#         })

#     @http.route('/dgb_clinica_veterinaria/dgb_clinica_veterinaria/objects/<model("dgb_clinica_veterinaria.dgb_clinica_veterinaria"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dgb_clinica_veterinaria.object', {
#             'object': obj
#         })

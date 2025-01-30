# -*- coding: utf-8 -*-
# from odoo import http


# class SgeScooters(http.Controller):
#     @http.route('/sge_scooters/sge_scooters', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sge_scooters/sge_scooters/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sge_scooters.listing', {
#             'root': '/sge_scooters/sge_scooters',
#             'objects': http.request.env['sge_scooters.sge_scooters'].search([]),
#         })

#     @http.route('/sge_scooters/sge_scooters/objects/<model("sge_scooters.sge_scooters"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sge_scooters.object', {
#             'object': obj
#         })


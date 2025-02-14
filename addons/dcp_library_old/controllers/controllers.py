# -*- coding: utf-8 -*-
# from odoo import http


# class DcpLibrary(http.Controller):
#     @http.route('/dcp_library/dcp_library', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dcp_library/dcp_library/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dcp_library.listing', {
#             'root': '/dcp_library/dcp_library',
#             'objects': http.request.env['dcp_library.dcp_library'].search([]),
#         })

#     @http.route('/dcp_library/dcp_library/objects/<model("dcp_library.dcp_library"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dcp_library.object', {
#             'object': obj
#         })


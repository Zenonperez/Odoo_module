# -*- coding: utf-8 -*-
# from odoo import http


# class Zpc2324(http.Controller):
#     @http.route('/zpc2324/zpc2324', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zpc2324/zpc2324/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('zpc2324.listing', {
#             'root': '/zpc2324/zpc2324',
#             'objects': http.request.env['zpc2324.zpc2324'].search([]),
#         })

#     @http.route('/zpc2324/zpc2324/objects/<model("zpc2324.zpc2324"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zpc2324.object', {
#             'object': obj
#         })

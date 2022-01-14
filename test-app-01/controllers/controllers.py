# -*- coding: utf-8 -*-
# from odoo import http


# class Test-app-01(http.Controller):
#     @http.route('/test-app-01/test-app-01', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test-app-01/test-app-01/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test-app-01.listing', {
#             'root': '/test-app-01/test-app-01',
#             'objects': http.request.env['test-app-01.test-app-01'].search([]),
#         })

#     @http.route('/test-app-01/test-app-01/objects/<model("test-app-01.test-app-01"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test-app-01.object', {
#             'object': obj
#         })

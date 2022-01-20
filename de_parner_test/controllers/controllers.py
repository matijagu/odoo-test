# -*- coding: utf-8 -*-
# from odoo import http


# class DeParnerTest(http.Controller):
#     @http.route('/de_parner_test/de_parner_test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_parner_test/de_parner_test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_parner_test.listing', {
#             'root': '/de_parner_test/de_parner_test',
#             'objects': http.request.env['de_parner_test.de_parner_test'].search([]),
#         })

#     @http.route('/de_parner_test/de_parner_test/objects/<model("de_parner_test.de_parner_test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_parner_test.object', {
#             'object': obj
#         })

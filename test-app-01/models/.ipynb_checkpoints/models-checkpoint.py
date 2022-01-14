# -*- coding: utf-8 -*-

# from odoo import models, fields, api


class test-app-01(models.Model):
    _inherit = 'res.partner'
    birthday = fields.Datetime('Date of birth')
  
#     _name = 'test-app-01.test-app-01'
#     _description = 'test-app-01.test-app-01'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

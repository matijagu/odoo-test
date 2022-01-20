# -*- coding: utf-8 -*-

from odoo import models, fields, api


class test-module(models.Model):
     _inherit = 'res.partner'
#     _description = 'test-module.test-module'

     testField = fields.Char('Test Field')
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

# -*- coding: utf-8 -*-

# from odoo import models, fields, api


class Partner(models.Model):
     _inherit = 'res.partner'
     birthday = fields.Datetime('Date of Birth')


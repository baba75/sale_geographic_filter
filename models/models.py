# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleGeographic(models.Model):
    _inherit = 'sale.order'
    
    country_id = fields.Many2one(related='partner_id.country_id', string='Partner country', store='true')
    state_id = fields.Many2one(related="partner_id.state_id", string='Partner state',store='true')
    
class InvoiceGeograpich(models.Model):
    _inherit = 'account.invoice'
    
    country_id = fields.Many2one(related='partner_id.country_id', string='Partner country', store='true')
    state_id = fields.Many2one(related="partner_id.state_id", string='Partner state',store='true')
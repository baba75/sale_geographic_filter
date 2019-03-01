# -*- coding: utf-8 -*-
from odoo import http

# class SaleGeographicFilter(http.Controller):
#     @http.route('/sale_geographic_filter/sale_geographic_filter/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_geographic_filter/sale_geographic_filter/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_geographic_filter.listing', {
#             'root': '/sale_geographic_filter/sale_geographic_filter',
#             'objects': http.request.env['sale_geographic_filter.sale_geographic_filter'].search([]),
#         })

#     @http.route('/sale_geographic_filter/sale_geographic_filter/objects/<model("sale_geographic_filter.sale_geographic_filter"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_geographic_filter.object', {
#             'object': obj
#         })
# -*- coding: utf-8 -*-
from odoo import http

# class ExtensionReportePosGastos(http.Controller):
#     @http.route('/extension_reporte__pos_gastos/extension_reporte__pos_gastos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extension_reporte__pos_gastos/extension_reporte__pos_gastos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extension_reporte__pos_gastos.listing', {
#             'root': '/extension_reporte__pos_gastos/extension_reporte__pos_gastos',
#             'objects': http.request.env['extension_reporte__pos_gastos.extension_reporte__pos_gastos'].search([]),
#         })

#     @http.route('/extension_reporte__pos_gastos/extension_reporte__pos_gastos/objects/<model("extension_reporte__pos_gastos.extension_reporte__pos_gastos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extension_reporte__pos_gastos.object', {
#             'object': obj
#         })
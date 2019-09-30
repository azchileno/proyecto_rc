# -*- coding: utf-8 -*-
from odoo import http

# class ProyectoRc(http.Controller):
#     @http.route('/proyecto_rc/proyecto_rc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyecto_rc/proyecto_rc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyecto_rc.listing', {
#             'root': '/proyecto_rc/proyecto_rc',
#             'objects': http.request.env['proyecto_rc.proyecto_rc'].search([]),
#         })

#     @http.route('/proyecto_rc/proyecto_rc/objects/<model("proyecto_rc.proyecto_rc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyecto_rc.object', {
#             'object': obj
#         })
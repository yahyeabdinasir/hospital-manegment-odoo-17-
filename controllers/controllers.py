# -*- coding: utf-8 -*-
# from odoo import http


# class QaranHospital(http.Controller):
#     @http.route('/qaran__hospital/qaran__hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qaran__hospital/qaran__hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('qaran__hospital.listing', {
#             'root': '/qaran__hospital/qaran__hospital',
#             'objects': http.request.env['qaran__hospital.qaran__hospital'].search([]),
#         })

#     @http.route('/qaran__hospital/qaran__hospital/objects/<model("qaran__hospital.qaran__hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qaran__hospital.object', {
#             'object': obj
#         })




from odoo import models, fields, api


class QaranHospital(models.Model):
    _name = 'hospital.patients'
    _description = 'qaran hispital patient '

    name = fields.Char()
    age  = fields.Integer()
    gender = fields.Selection([
        ('male','male'),
        ('female','female'),
    ])
    state = fields.Selection([
        ('Draft', 'draft'),
        ('Waiting ', 'waiting'),
        ('In_cansualtion', 'in_cansualtion'),
        ('Done', 'Done'),
    ])




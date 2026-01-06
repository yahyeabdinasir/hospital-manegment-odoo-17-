from odoo import models, fields, api
# from odoo.fields import Date
from datetime import date


class QaranHospital(models.Model):
    _name = 'hospital.patients'
    _description = 'qaran hispital patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="name", tracking=True)
    age = fields.Integer(string="age", tracking=True, compute="_compute_age")

    date_of_birth = fields.Date(string="date of birth")
    gender = fields.Selection([
        ('male', 'male'),
        ('female', 'female'),
    ], string="gender")

    booked_date = fields.Date(string="booked date", default=fields.Date.context_today)

    @api.depends("date_of_birth")
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year or 0
            else:
                rec.age = 0

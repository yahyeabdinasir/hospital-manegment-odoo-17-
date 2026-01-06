from odoo import models, fields, api
# from odoo.fields import Date
from datetime import date


class QaranHospital(models.Model):
    _name = 'hospital.appoitnment'
    _description = 'hospital appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "patient_id"

    patient_id = fields.Many2one("hospital.patient", string="paitent id ", tracking=True)
    number = fields.Char(string="number")
    date_appoinment = fields.Date()
    note = fields.Text(string="note", tracking=True)

    date_of_birth = fields.Date(string="date of birth")

    state = fields.Selection([
        ('Draft', 'draft'),
        ('Waiting ', 'waiting'),
        ('In_cansualtion', 'in_cansualtion'),
        ('Done', 'Done'),
    ], string="state")

    @api.model
    def create(self, vals_list):
        vals_list['number'] = self.env["ir.sequence"].next_by_code("hospital.appoitnment")
        return super(QaranHospital, self).create(vals_list)


    def write(self, vals):
        for rec in self:
            if not rec.number:
                vals['number'] = self.env["ir.sequence"].next_by_code("hospital.appoitnment")
        return  super(QaranHospital , self).write(vals)







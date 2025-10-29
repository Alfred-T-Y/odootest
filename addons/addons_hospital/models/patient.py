from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread']
    _description = "Patient Master" 

    name = fields.Char(string="Name", required=True)
    date_of_birth = fields.Date(string="D_O_B")
    gender = fields.Selection([('male','Male'),('female','Female')], string="Gender")
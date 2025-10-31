from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread']
    _description = "Hospital appointment" 

    patient_id = fields.Many2one("hospital.patient", string="Patient", required=True, tracking=True )
    date_appointment = fields.Date(string="Date", tracking=True)
    note = fields.Text(string="Note", tracking=True)

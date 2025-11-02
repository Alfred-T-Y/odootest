from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread']
    _description = "Hospital appointment"
    _rec_name = "patient_id" 

    reference = fields.Char(string="Reference", default="New")
    patient_id = fields.Many2one("hospital.patient", string="Patient", required=True, tracking=True )
    date_appointment = fields.Date(string="Date", tracking=True)
    note = fields.Text(string="Note", tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('reference') == 'New' or vals.get('reference') is None:
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super().create(vals_list) 

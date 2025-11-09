from odoo import api, models


class ReportAppointmentPdf(models.AbstractModel):
    _name= 'report.addons_hospital.template_appointment_pdf'
    _description= 'Report Appointment pdf'

    @api.model
    def _get_report_values(self, docids, data=None):
        print("=== DEBUG REPORT ===")
        print("DocIDs:", docids)
        print("Context:", self.env.context)
        print("Active ID:", self.env.context.get('active_id'))
        model = 'hospital.appointment'
        docs = self.env[model].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': model,
            'data': data,
            'docs': docs,
        }
from odoo import api, models


class ReportAppointmentPdf(models.AbstractModel):
    _name= 'report.addons_hospital.template_appointment_pdf'
    _description= 'Report Appointment pdf'

    @api.model
    def _get_report_values(self, docids, data=None):

        model = 'hospital.appointment'
        docs = self.env[model].browse(docids)
        data = []
        for doc in docs:
            patient = doc.mapped('patient_id')
            tags_list = patient.mapped('tags_ids')
            data.append({
                'doc':doc, 
                'tag':tags_list,
            })
       

        

        #lastpatient=patients.pop()
        #beforelastpatient=patients.pop()

        return {
            'doc_ids': docids,
            'doc_model': model,
            'data': data,
            #'beforelastpatient' : beforelastpatient,
            #'lastpatient' : lastpatient,
        } 
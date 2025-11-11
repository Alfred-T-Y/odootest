from odoo import models

class AppointmentReportXlsx(models.AbstractModel):
    _name = 'report.addons_hospital.report_appointment_xls'
    _inherit = 'report.report_xlsx.abstract'
     
    def generate_xlsx_report(self, workbook, data, lines):
            
        sheet = workbook.add_worksheet('appointments')
        bold = workbook.add_format({'bold': True})
        row=2
        col=3
        for obj in lines:
            row += 1
            sheet.write(col, row, obj.patient_id.name, bold)

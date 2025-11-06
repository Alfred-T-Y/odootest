from odoo import models

class PatientCardXlsx(models.AbstractModel):
    _name = 'report.addons_hospital.report_patient_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        #sheet = workbook.add_worksheet(report_name[:31])
        bold = workbook.add_format({'bold': True})
        #sheet.write(0, 0, obj.name, bold)

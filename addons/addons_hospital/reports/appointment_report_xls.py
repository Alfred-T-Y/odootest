from odoo import models

class AppointmentReportXlsx(models.AbstractModel):
    _name = 'report.addons_hospital.report_appointment_xls'
    _inherit = 'report.report_xlsx.abstract'
     
    def generate_xlsx_report(self, workbook, data, lines):
            
        sheet = workbook.add_worksheet('appointments')
        bold = workbook.add_format({'bold': True})
        title = workbook.add_format({'bold': True, 'align':'center', 'bg_color':'yellow'})
        date_format = workbook.add_format({'num_format': 'dd/mm/yyyy'})
        row=2
        col=3
        sheet.merge_range(col-1,row,col-1,row+6,'Appointments',title)
        sheet.write(col, row, 'Reference', bold)
        sheet.write(col+1, row, 'Name', bold)
        sheet.write(col+2, row, 'Date', bold)
        sheet.write(col+3, row, 'Tags', bold)
        sheet.set_column('C:C', 10)
        sheet.set_column('D:I', 15)
        for obj in lines:
            tags_list = []
            for tag in obj.patient_id.tags_ids:
                tags_list.append(tag.name)
            tags = ', '.join(tags_list)
            row += 1
            sheet.write(col, row, obj.reference)
            sheet.write(col+1, row, obj.patient_id.name)
            if obj.date_appointment:
                sheet.write(col+2, row, obj.date_appointment, date_format)
            sheet.write(col+3, row, tags)

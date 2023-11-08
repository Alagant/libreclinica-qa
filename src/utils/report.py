from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

class ReportGenerator:
    def __init__(self, filename):
        self.filename = filename

    def generate_report(self, data):
        doc = SimpleDocTemplate(self.filename, pagesize=letter)
        styles = getSampleStyleSheet()

        # define title and summary 
        title_style = styles["Title"]
        title_style.fontName = "Helvetica-Bold"
        title_style.alignment = 1 #center alignment

        # summary style
        summary_style = styles["Normal"]
        summary_style.fontName = "Helvetica-Bold"

        company_name_style = styles["Title"]
        company_name_style.fontName = "Helvetica-Bold"
        company_name_style.alignment = 0 #left alignment

        # create content for report
        report_content = []
        report_content.append(Paragraph("Alagant LLC", company_name_style))

        report_content.append(Paragraph("Test Report for LibreClinica", title_style))
        report_content.append(Spacer(1, 6))

        # summary
        report_content.append(Paragraph(f"Test Summary: {data['fullName']}", summary_style))
        report_content.append(Spacer(1, 6))

        report_content.append(Paragraph("Step execution details", summary_style))
        report_content.append(Spacer(1, 6))
        
        table_data = [["Description", "Status", "Attachments"]]
        for item in data['steps']:
            if "attachments" in item and len(item['attachments']) > 0:
                step_attachment = item['attachments'][0].get('source')
                if step_attachment:
                    image = Image('allure-results/'.__add__(step_attachment), width=1.25*inch, height=2*inch)
                
                table_data.append([item['name'], item['status'], image])
            else:
                table_data.append([item['name'], item['status'], "No attachments"])
        
        table_width = 0.8 * letter[0]
        col_widths = [table_width * 0.65, table_width * 0.20]

        table = Table(table_data, colWidths=col_widths)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.lightslategray),
            ('TEXTCOLOR', (0,0), (-1,-1), 0.25, colors.whitesmoke),
            ('ALIGN', (0,0), (-1,-1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('GRID', (0,0), (-1,-1), 0.25, colors.black),
            ('WORDWRAP', (0, 1), (-1, -1), 1),
        ]))

        # Save the PDF
        report_content.append(table)
        report_content.append(Spacer(1, 12))
        
        doc.build(report_content)

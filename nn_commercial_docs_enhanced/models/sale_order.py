from odoo import models, api, fields



class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    pdf_logo = fields.Boolean(string="Show Logo in PDF", default=True,
                              help="If checked, the company logo will be shown in the PDF report")
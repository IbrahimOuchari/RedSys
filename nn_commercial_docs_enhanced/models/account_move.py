from odoo import models, api, fields



class AccountMoveInherit(models.Model):
    _inherit = 'account.move'
    pdf_logo = fields.Boolean(string="Show Logo in PDF", default=True,
                              help="If checked, the company logo will be shown in the PDF report")
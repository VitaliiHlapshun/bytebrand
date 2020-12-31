from odoo import models, fields, api

class NewApplication(models.TransientModel):
    _name = 'new_application'

    applicant_id = fields.Many2one('first_module.applicant', string="Applicant")
    application_date = fields.Date(string="Application Date")
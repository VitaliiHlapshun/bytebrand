# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectTaskInherit(models.Model):
    _inherit = 'project.task'

    complexity = fields.Char(string='Complexity')
    skill_level = fields.Char(string='Skill level')
    urgency = fields.Boolean()

class first_module(models.Model):
    _name = 'first_module.first_module'
    _description = 'first_module.first_module'

    name = fields.Char()
    lastname = fields.Boolean()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    birth_date = fields.Datetime(string="Date of birth")

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

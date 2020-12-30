# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectTaskInherit(models.Model):
    _inherit = 'project.task'
    complexity = fields.Char()
    skill_level = fields.Char()
    urgency = fields.Boolean()
    experience = fields.Integer()

class Student(models.Model):
    _name = 'first_module.student'
    _description = "student"

    name = fields.Char()
    birth_date = fields.Datetime(string="Date of birth")

    module_ids = fields.One2many('first_module.first_module', 'student_id', string="Module")

class first_module(models.Model):
    _name = 'first_module.first_module'
    _description = 'first_module'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    student_id = fields.Many2one('first_module.student', string="Student")

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

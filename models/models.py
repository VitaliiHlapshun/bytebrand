# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectTaskInherit(models.Model):
    _inherit = 'project.task'
    complexity = fields.Char()
    skill_level = fields.Char()
    urgency = fields.Boolean()
    experience = fields.Integer()

class first_module(models.Model):
    _name = 'first_module.first_module'
    _description = 'first_module'

    def _dafault_description(self):
        return "... Python Developer"
    name = fields.Char()
    total_score = fields.Integer(string="Total Score")
    mark = fields.Float(compute="_value_pc", store=True)
    status = fields.Char(compute="_status")
    description = fields.Text(string="Description", default=_dafault_description)
    is_registered = fields.Boolean('Registered', copy=False)

    student_picture = fields.Binary(string='Picture')

    parents_id = fields.Many2one('first_module.parents', string="Parents",
                                 required=False, default=lambda self: self.env.user)

    class Parents(models.Model):
        _name = 'first_module.parents'
        _description = "parents"

        name_of_mother = fields.Char()
        name_of_father = fields.Char()
        birth_date = fields.Date(string="Date of birth", default=fields.Date.today)

        module_ids = fields.One2many('first_module.first_module', 'parents_id', string="Module")

    @api.depends('total_score')
    def _value_pc(self):
        for record in self:
            record.mark = float(record.total_score) / 100

    @api.depends('mark')
    def _status(self):
        for record in self:
            if record.mark >= 1.25:
                record.status = "Passed"
            else:
                record.status = "Not passed"
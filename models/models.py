from odoo import models, fields, api
from odoo.exceptions import ValidationError

def _default_description(self):
    return "... Python Developer"

class ProjectTaskInherit(models.Model):
    _inherit = 'project.task'
    complexity = fields.Char(help="Level of difficulty")
    skill_level = fields.Char(requried=True, default=_default_description)
    date_begin = fields.Datetime(string='Start Date')
    experience = fields.Integer(help="Amount of years of experience", default=60)

class first_module(models.Model):
    _name = 'first_module.first_module'
    _description = 'first_module'

    def base_methods(self):
        for record in self:
            students = self.env['first_module.first_module'].search([])
            print(students)
            passed_students = self.env['first_module.first_module'].search([('status', '=', 'Passed')])
            print("passed_student are...", passed_students)

            filtered_passed_students = self.env['first_module.first_module'].search([]).filtered(lambda s: s.status == 'Passed')
            print("filtered_passed_students...", filtered_passed_students)

            record_to_copy = self.env['first_module.first_module'].browse(4)
            record_to_copy.copy()

            record_to_copy = self.env['first_module.first_module'].browse(12)
            record_to_copy.unlink()

    def cursor_query(self):
        self.env.cr.execute('SELECT * FROM first_module WHERE status="Passed"')
        return self.env.cr.fetchall()

    name = fields.Char()
    total_score = fields.Integer(string="Total Score")
    mark = fields.Float(compute="_value_pc", store=True)
    status = fields.Char(compute="_status")
    description = fields.Text(string="Description", default=_default_description)
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

    @api.model
    def create(self, vals):
        res = super(first_module, self).create(vals)
        print("Works!")
        return res

    def write(self, vals):
        res = super(first_module, self).write(vals)
        print("Again works")
        return res

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

    @api.constrains('total_score')
    def check_total_score(self):
        for record in self:
            if record.total_score >= 1000.0:
                print ("Mark can not be more than 1000")
                raise ValidationError("Mark can not be more than 1000")
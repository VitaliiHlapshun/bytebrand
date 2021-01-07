from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class students(models.Model):
    _name = 'students.students'
    _description = 'students.students'

    name = fields.Char()
    total_score = fields.Integer(string="Total Score")
    mark = fields.Float(compute="_value_pc", store=True)
    status = fields.Char(compute="_status")
    description = fields.Text(string="Description", default="...Python Developer")
    is_registered = fields.Boolean('Registered', required=False)
    signature = fields.Binary(string='Signature')
    school_id = fields.Many2one('students.school', string="School",
                                required=True, default=1)

    def base_methods_search(self):
        students = self.env['students.students'].search([])
        print(students)

    def base_methods_search_with_domain(self):
        passed_students = self.env['students.students'].search([('status', '=', 'Passed')])
        print("passed_student are...", passed_students)

    def base_methods_filter(self):
        filtered_passed_students = self.env['students.students'].search([]).filtered(
            lambda s: s.status == 'Passed')
        print("filtered_passed_students...", filtered_passed_students)

    def base_methods_copy(self):
        record_to_copy = self.env['students.students'].browse(4)
        record_to_copy.copy()

    def base_methods_delete(self):
        record_to_copy = self.env['students.students'].browse(6)
        record_to_copy.unlink()

    def cursor_query(self):
        self.env.cr.execute("select * from students_students")
        res = self.env.cr.fetchall()
        print(res)

    def custom_button_method(self):
        print("Hello")

    @api.model
    def create(self, vals):
        vals['is_registered'] = True
        res = super(students, self).create(vals)
        print("Works!")
        return res

    def write(self, vals):
        vals['total_score'] = 999
        res = super(students, self).write(vals)
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
                print("Mark can not be more than 1000")
                raise ValidationError("Mark can not be more than 1000")


class School(models.Model):
    _name = 'students.school'
    _description = "school"

    name = fields.Char(string="School", required=True)
    school_type = fields.Selection([('public', 'Public School'),
                                    ('private', 'Private School')],
                                   string="Type of School")
    start = fields.Date()
    graduated = fields.Date()
    description = fields.Text(string="Description...")

    def name_get(self):
        list = []
        for school in self:
            name = school.name
            if school.school_type:
                name += " ({})".format(school.school_type)
            list.append((school.id, name))
        return list


class ProjectTaskInherit(models.Model):
    _inherit = 'project.task'

    complexity = fields.Char(help="Level of difficulty")
    skill_level = fields.Char(requried=True, default="Python Developer")
    date_begin = fields.Datetime(string='Start Date')
    experience = fields.Integer(help="Amount of years of experience", default=60)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def action_view_url(self):
        url = self.partner_id.website
        if url:
            return {
                "type": "ir.actions.act_url",
                "url": "%s" % url,
                "target": "new"
            }
        else:
            raise UserError("There is no such webpage")

    def batch_quotation_confirm(self):
        for order in self:
            if order.state == 'draft':
                order.button_confirm()

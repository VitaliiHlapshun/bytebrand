from odoo import api, models, fields

class StudentsTotalScoreWizard(models.TransientModel):
    _name = "students.total.score.update.wizard"

    total_score = fields.Integer(string="Total Score")

    def students_total_score_update(self):
        print("Success")

        self.env['students.students'].browse(self._context.get("active_ids")).update({'total_score': self.total_score})
        return True
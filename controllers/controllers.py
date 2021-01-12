from odoo import http


class Students(http.Controller):
    @http.route('/students/students/', auth='public', website=True)
    def index(self, **kw):
        Teachers = http.request.env['students.teachers']
        return http.request.render('students.index', {
            'teachers': Teachers.search([])
        })

    @http.route('/students/students/objects/', auth='public', website=True)
    def list(self, **kw):
        return http.request.render('students.listing', {
            'root': '/students/students',
            'objects': http.request.env['students.students'].search([]),
        })

    @http.route('/students/students/objects/<model("students.students"):obj>/', auth='public', website=True)
    def object(self, obj, **kw):
        return http.request.render('students.object', {
            'object': obj
        })

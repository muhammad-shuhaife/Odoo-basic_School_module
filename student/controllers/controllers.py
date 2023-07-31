# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


# class Student(http.Controller):
#     @http.route('/student/student', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/student/student/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('student.listing', {
#             'root': '/student/student',
#             'objects': http.request.env['student.student'].search([]),
#         })

#     @http.route('/student/student/objects/<model("student.student"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('student.object', {
#             'object': obj
#         })

# class Car_rental_template(http.Controller):
#     @http.route('/car',auth='public',website=True)
#     def custom_car_rental_template(self):
#         res = request.env['car.rental'].search([])
#         return request.render('student.car_rental_template', {'car': res})
class Library_website_template(http.Controller):
    @http.route('/book', auth='public', website=True)
    def custom_library_template(self):
        res = request.env['student.library'].search([])
        return request.render('student.library_template', {'book': res})


class StudentRegistrationController(http.Controller):
    @http.route(['/employee_registration'], type='http', auth="public", website=True)
    def student_registration_form(self):
        return request.render('student.employee_registration_form')

    @http.route(['/register_submit'], type='http', auth="public", website=True)
    def website_menu_student(self, **post):
        email = post.get('email')
        res = request.env['res.partner'].search([('email', '=', email)])
        if res:
            return request.render('student.email_exist_template')

        else:
            request.env['res.partner'].create(post)
            return request.render('student.registration_success_template')



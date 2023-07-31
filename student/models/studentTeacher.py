
from odoo import models, fields, api


class StudentTeacher(models.Model):
    _name = 'student.teacher'
    _description = 'student.teacher '
    _rec_name = "first_name"

    teacher_sequence = fields.Integer("teacher Id")
    first_name = fields.Char(string="first name",required=True)
    last_name = fields.Char(string="second name")
    date_of_birth = fields.Integer(string="date of birth")
    specialisation = fields.Char(string="Specialisation")
    phone = fields.Char(string="phone")
    email = fields.Char(string="email")
    place = fields.Char(string="place")
    Is_teacher = fields.Boolean(default=True)
    subject = fields.Char(string="subject allocated")
    # user_id = fields.Many2one('res.users')

    # @api.model
    # def create(self, values):
    #     teacher = super(StudentTeacher, self).create(values)
    #     if teacher.Is_teacher:
    #         teacher_group = self.env.ref('student.manager_group')
    #         if teacher_group:
    #             teacher_group.users = [(4, teacher.env.user.id)]
    #     return teacher
    #
    # def write(self, values):
    #     if 'Is_teacher' in values:
    #         teacher_group = self.env.ref('student.manager_group')
    #         if teacher_group:
    #             if values['Is_teacher']:
    #                 teacher_group.users = [(4, self.env.user.id)]
    #             else:
    #                 teacher_group.users = [(3, self.env.user.id)]
    #     return super(StudentTeacher, self).write(values)

    @api.model
    def demo_cron(self):
        print("wondeful")

    # @api.model
    # def write(self, vals):
    #     vals.update({
    #         'specialisation': 'Msc'
    #     })
    #     new_record1 = self.env['student.teacher'].search([('specialisation', '=', 'bsc')])
    #     if new_record1:
    #         new_record1.write(vals)

    # def create(self, vals):
    #     vals = {
    #         'first_name': 'sangeetha',
    #         'last_name': 's',
    #         'specialisation': 'bsc'
    #      }
    #     # Perform any additional validation or manipulation of the input values if needed
    #     # ...
    #
    #     # Call the create() method to create the new record
    #     new_record = super(StudentTeacher, self).create(vals)
    #     new_record1 = self.env['student.teacher'].browse([('specialisation', '=', 'bsc')])
    #     print("===================================================================", new_record1)
    #     if new_record1:
    #         self.env['student.teacher'].write([('specialisation', '=', 'maths')])

from odoo import models, fields, api


class StudentClass(models.Model):
    _name = 'student.class'
    _description = 'student.class '
    _rec_name = 'class_name'

    class_sequence = fields.Integer("class Id")
    class_name = fields.Char(string="Class name",required=True)
    description = fields.Char(string="Description")
    schedule = fields.Datetime("Timing")
    strength = fields.Integer(string="Strength")
    student_id = fields.Many2one("student.student", string='Student')
    division_id = fields.Many2one("student.division", string="Division")
    teacher = fields.Many2one("student.teacher", string="Teacher", related="division_id.staff_id")
    item = fields.Char(string="item",readonly=True)

from odoo import models, fields, api


class StudentDivision(models.Model):
    _name = 'student.division'
    _description = 'student.division '
    _rec_name = "division_name"

    division_sequence = fields.Integer(string="DivisionId")
    division_name = fields.Char(string="division name",required=True)
    description = fields.Char(string="Description")
    location = fields.Char("Location")
    staff_id = fields.Many2one("student.teacher", string="Teacher")

    
    
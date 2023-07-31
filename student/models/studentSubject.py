from odoo import models,api,fields


class Subject(models.Model):
    _name = 'student.subject'
    _description = 'student.subject'

    name = fields.Char(string="subject Name")
    sequence = fields.Char(string="Subject Id")

    def subject_allocation(self):
        action = self.env.ref('student.subject_allocation_wizard').sudo().read()[0]
        return action



from odoo import fields,models,api


class SubjectAllocationWizard(models.TransientModel):
    _name = 'student.subject.wizard'
    _description = 'student.subject.wizard'

    name = fields.Many2many('student.subject', string="Subject")
    teacher_id = fields.Many2one('student.teacher',string="Select the teacher")

    # def allocate_to_teacher(self):
    #     student_class = self.env['student.teacher'].browse(self.teacher_id.id)
    #     item_names = self.name.mapped('name')
    #
    #     student_class.subject = ', '.join(item_names)
    #     return

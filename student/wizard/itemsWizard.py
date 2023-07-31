from odoo import fields,models,api


class ItemsWizard(models.TransientModel):
    _name = 'student.items.wizard'
    _description = 'student.item.wizard'

    class_name = fields.Many2one('student.class', string="class")
    item = fields.Many2many('student.items', string="items")

    def allocate_to_class(self):
        student_class = self.env['student.class'].browse(self.class_name.id)
        item_names = self.item.mapped('name')

        student_class.item = ', '.join(item_names)


from odoo import models,fields,api


class BookAllocation(models.Model):
    _name = 'student.allocation'
    _description = 'book.allocation'

    book = fields.Char()
    student = fields.Char()

    def change_status(self):
        student_library = self.env['student.library'].search([('name', '=', self.book)])
        if student_library:
            student_library.write({'status': 'available'})
        self.unlink()

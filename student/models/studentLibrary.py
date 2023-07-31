from odoo import models,fields,api


class StudentLibrary(models.Model):
    _name = 'student.library'
    _description = 'student.library'

    book_sequence = fields.Char(string="Book Id", default="New")
    name = fields.Char(string="first name",required=True)
    author = fields.Char(string="Author of book")
    status = fields.Selection([
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
    ], string="Status", default="available")

    @api.model
    def create(self, vals):
        vals['book_sequence'] = self.env['ir.sequence'].next_by_code('student.library')
        return super(StudentLibrary, self).create(vals)

    def allocation_action(self):
        action = self.env.ref('student.book_allocation_wizard_action').read()[0]
        return action

from odoo import models, fields, api


class BookAllocation(models.TransientModel):
    _name = 'student.allocation.wizard'
    _description = 'book.allocation_wizard'

    book_id = fields.Many2one('student.library', string="Select the book", default=lambda self: self.show_id())
    student_id = fields.Many2one('student.student', string="Select the student")

    def print_report(self):
        model = self.env.context.get('active_model')
        docs = self.env[model].browse(self.env.context.get('active_ids', []))
        return self.env.ref('student.book_allocation_card').report_action(docs)
        # values ={}
        # data = {
        #     'ids': self.ids,
        #     'model': self._name,
        #     'form': {
        #         'book_id': self.book_id.id,
        #         'student_id': self.student_id.id,
        #     },
        # }
        # values.update(data)
        # print("==================================",values)
        #
        # return self.env.ref('student.book_allocation_card').report_action(self, data=values)

    def print_sale_report(self):
        for record in self:
            values = {}
            model = self.env.context.get('active_model')
            docs = self.env[model].browse(self.env.context.get('active_ids', []))
            data = {'records': self.env['sale.order'].search([], limit=1).ids}
            values.update(data)
            return self.env.ref('student.action_manager_id_card').report_action(docs, data=values)

    def allocate_book(self):
        save = self.env['student.allocation']
        if self.book_id:
            self.book_id.write({'status': 'borrowed'})
        else:
            self.book_id.write({'status': 'available'})
        record_vals = {
            'book': self.book_id.name,
            'student': self.student_id.first_name,
        }
        save.create(record_vals)

    @api.model
    def show_id(self):
        active_id = self.env.context.get('active_id')
        if active_id:
            return self.env['student.library'].browse(active_id)

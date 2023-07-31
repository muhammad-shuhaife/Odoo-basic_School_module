from odoo import models, fields, api


class Items(models.Model):
    _name = 'student.items'
    _description = 'student.item'

    name = fields.Char(string='name of item')
    count = fields.Char(string='count')
    price = fields.Char(string="price of the item")

    def allocate_item(self):
        action = self.env.ref('student.item_allocation_wizard').sudo().read()[0]
        return action

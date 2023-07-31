from odoo import models,fields


class Car_rental(models.Model):
    _name = 'car.rental'
    _description = 'car.rental'

    name = fields.Char(string="Name", required=True)
    price = fields.Char(string="price")
    details = fields.Char(string="details")

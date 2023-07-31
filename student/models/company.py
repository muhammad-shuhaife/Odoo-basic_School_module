from odoo import models,fields,api


class CompanyKanban(models.Model):
    _name = 'company.kanban'
    _description = 'company.kanban'

    email = fields.Char(string="Email")
    name = fields.Char(string="Name",required=True)
    phone = fields.Char(string="phone")
    address = fields.Char(string="Address")
    start_date = fields.Datetime(string="Date start")
    end_date = fields.Datetime(string="Date end")
    image = fields.Binary(string="Image")

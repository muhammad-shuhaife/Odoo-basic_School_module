from odoo import models, fields, api,_
from dateutil.relativedelta import relativedelta
from datetime import date, datetime
from datetime import timedelta


class Test12(models.Model):
    _name = 'test.test'

    name = fields.Char()
    expiry_date = fields.Datetime()
    alert_after = fields.Datetime(compute="_default_validity_date",store=True)
    user_id = fields.Many2one('res.users')
    state = fields.Selection([("New", "New"), ("Expired", "Expired"), ("Canceled", "Canceled")], default='New')
    current_user = fields.Char(default=lambda self: self.env.user.name)

    @api.depends('expiry_date')
    def _default_validity_date(self):
        days = self.env['ir.config_parameter'].sudo().get_param('student.alert_after')
        days = int(days)
        if days:
            if days > 0:
                a = datetime.now() + relativedelta(days=days)
                self.alert_after = a


class SettingsInherit(models.TransientModel):
    _inherit = 'res.config.settings'

    alert_after = fields.Integer(string=" Alert after",
                                 config_parameter="student.alert_after")


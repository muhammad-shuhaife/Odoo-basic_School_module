from odoo import fields, models, api


class Sale_inherit_model(models.Model):
    _inherit = "sale.order"
    _description = "sale.order"

    discount = fields.Integer(string="discount percentage")

    def context_func(self):
        for record in self:
            dis = self._context.get('discount_per')
            if record.amount_total:
                record.amount_total = record.amount_total - (record.amount_total / 100) * float(dis)


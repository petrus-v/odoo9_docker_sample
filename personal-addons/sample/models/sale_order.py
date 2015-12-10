# -*- encoding: utf-8 -*-
from openerp import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create(self, vals):
        # this is obiviously a bad example!
        raise NotImplementedError()

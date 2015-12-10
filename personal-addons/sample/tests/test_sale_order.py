# -*- coding: utf-8 -*-
from openerp.tests import common


class test_sale_order(common.TransactionCase):
    """ Test Product set"""

    def setUp(self):
        super(test_sale_order, self).setUp()

    def test_add_set(self):
        with self.assertRaises(NotImplementedError):
            self.env['sale.order'].create({'name': 'test'})

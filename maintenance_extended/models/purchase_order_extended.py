# -*- coding: utf-8 -*-
"""
* Created by gonzalezoscar on 7/08/18
* beton_dev
"""

from odoo import api, fields, models


class PurchaseOrderExtended(models.Model):
    _inherit = 'purchase.order'

    x_s4g_orden_trabajo = fields.Many2one(
        'ops4g.orden_trabajo',
        string="Orden de mantenimiento",
        help="Orden de mantenimiento origen"
    )
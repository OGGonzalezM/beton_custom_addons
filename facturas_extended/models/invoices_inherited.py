# -*- coding: utf-8 -*-
from odoo import api, fields, models


class InvoicesInherited(models.Model):
    _inherit = 'account.invoice'

    x_analytic_account_id = fields.Many2one(
        'account.analytic.account',
        string="Cuenta analítica",
        required=True
    )

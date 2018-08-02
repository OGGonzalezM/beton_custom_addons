"""
* Created by gonzalezoscar on 31/07/18
* expenses
"""

# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HREmployeeExtended(models.Model):
    _inherit = 'hr.employee'

    costo_hora = fields.Float(
        string="Costo / Hora",
    )
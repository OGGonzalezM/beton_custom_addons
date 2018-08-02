# -*- coding: utf-8 -*-
"""
* Created by gonzalezoscar on 2/08/18
* beton_dev
"""
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class MaintenanceRequestExtended(models.Model):
    _inherit = 'maintenance.request'

    x_orden_trabajo = fields.Many2one(
        'ops4g.orden_trabajo',
        string="Orden de trabajo",
    )
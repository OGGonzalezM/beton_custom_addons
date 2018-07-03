# -*- coding: utf-8 -*-
from odoo import fields, models


class Fields_Employees(models.Model):
    _inherit = 'hr.employee'

    x_beton_fechaaltaimss = fields.Char(string="Fecha de alta en IMSS")

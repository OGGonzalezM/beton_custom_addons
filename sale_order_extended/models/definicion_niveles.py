# -*- coding: utf-8 -*-
from odoo import fields, models


class Definicion_niveles(models.Model):
	_name = 'sale.order.niveles'

	name = fields.Char("Nivel")
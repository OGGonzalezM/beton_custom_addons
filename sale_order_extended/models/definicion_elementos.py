# -*- coding: utf-8 -*-
from odoo import fields, models


class Definicion_elementos(models.Model):
	_name = 'sale.order.elementos'

	name = fields.Char("Elemento")
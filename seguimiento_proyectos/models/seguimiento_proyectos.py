# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SeguimientoProyectos(models.Model):
	_inherit = 'account.analytic.line'

	x_beton_folioentrega = fields.Char(
		string="Folio de la entrega"
	)

	x_beton_equipoentrega = fields.Many2one(
		'fleet.vehicle',
		string="Equipo de entrega"
	)
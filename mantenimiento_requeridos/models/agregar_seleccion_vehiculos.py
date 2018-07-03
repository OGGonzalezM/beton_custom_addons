# -*- coding: utf-8 -*-
from odoo import fields, models


class Seleccion_vehiculos(models.Model):
	_inherit = 'maintenance.equipment'

	x_beton_mantenimiento_vehiculo = fields.Many2one('fleet.vehicle', "Vehículo")
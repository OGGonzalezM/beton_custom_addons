# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Sale_order_extra_data(models.Model):
	_inherit = 'sale.order'

	x_beton_folio_venta = fields.Char("Folio")
	x_beton_pedido_cliente = fields.Char("Pedido de cliente")
	x_beton_niveles = fields.Many2many('sale.order.niveles', string="Niveles")
	x_beton_elementos = fields.Many2many('sale.order.elementos', string="Elementos")
	x_beton_premezclador = fields.Char(string="Premezclador")
	x_beton_tuberia_vertical = fields.Float("Tubería vertical")
	x_beton_tuberia_horizontal = fields.Float("Tuberia horizontal")
	x_beton_tuberia_total = fields.Float("Tubería Total" ,compute='obtener_total_tuberia')
	x_beton_tipo_equipo_solicitado = fields.Selection(selection=[('estacionario','Estacionario'),('pluma','Pluma')], string="Tipo de equipo solicitado")
	x_beton_equipo_solicitado = fields.Many2one('fleet.vehicle', string="Equipo solicitado")

	@api.one
	@api.depends('x_beton_tuberia_vertical','x_beton_tuberia_horizontal')
	def obtener_total_tuberia(self):
		for record in self:
			record['x_beton_tuberia_total'] = record['x_beton_tuberia_vertical'] + record['x_beton_tuberia_horizontal']

	x_beton_fecha_hora_pedido = fields.Datetime("Fecha y hora del servicio")

	x_beton_hora_llegada = fields.Float(
		string="Hora de llegada"
	)

	x_beton_hora_listos = fields.Float(
		string="Hora listos"
	)

	x_beton_hora_inicio = fields.Float(
		string="Hora de inicio"
	)

	x_beton_hora_termino = fields.Float(
		string="Hora de termino"
	)

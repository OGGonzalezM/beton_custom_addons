# -*- coding: utf-8 -*-
"""
* Created by gonzalezoscar on 2/08/18
* beton_dev
"""
from datetime import datetime

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class MaintenanceRequestExtended(models.Model):
    _inherit = 'maintenance.request'

    x_orden_trabajo = fields.Many2one(
        'ops4g.orden_trabajo',
        string="Orden de trabajo",
    )

    x_proveedor_materiales_id = fields.Many2one(
        'res.partner',
        string="Proveedor para la orden de compra",
        domain="[('supplier', '=', True)]"
    )

    orden_compra_creada = fields.Boolean(
        string="Orden de compra creada",
        help="Si esta casilla se encuentra marcada significa que ya fue "
             "creada una orden de compra para esta petición de mantenimiento.\n"
             "Si desea volver a crear la orden de compra desmarque esta opción",
        default=False,
        track_visibility='onchange',
    )

    @api.multi
    def crear_orden_compra(self):
        if self.x_orden_trabajo:
            if self.x_proveedor_materiales_id:
                proveedor = self.x_proveedor_materiales_id.id
            else:
                proveedor = self.env['res.partner'].sudo().search(
                    [
                        ('supplier', '=', True)
                    ]
                )
                proveedor = proveedor[0]
            orden_compra = self.env['purchase.order'].sudo().create(
                {
                    'partner_id': proveedor,
                }
            )

            orden_trabajo = self.x_orden_trabajo
            for tarea in orden_trabajo.tareas_ids:
                tarea_odoo = tarea.tarea_id
                for material in tarea_odoo.listado_materiales_ids:
                    unidad_medida = material.product_id.uom_id
                    precio_unitario = material.product_id.standard_price
                    fecha_planeada = datetime.now()
                    nombre_producto = material.product_id.name + \
                                      " del mantenimiento " + \
                                      orden_trabajo.name + \
                                      " de " + self.name

                    self.env['purchase.order.line'].sudo().create(
                        {
                            'name': nombre_producto ,
                            'order_id': orden_compra.id,
                            'product_id': material.product_id.id,
                            'product_uom': unidad_medida.id,
                            'price_unit': precio_unitario,
                            'date_planned': fecha_planeada,
                            'product_qty': material.cantidad,
                        }
                    )
            self.orden_compra_creada = True
        else:
            raise ValidationError("Por favor asigne una orden de trabajo")

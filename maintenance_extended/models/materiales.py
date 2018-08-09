# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Materiales(models.Model):
    _name = 'ops4g.materiales'

    task_id = fields.Many2one(
        'project.task',
        string="Tarea"
    )

    product_id = fields.Many2one(
        'product.product',
        string="Material",
        domain="[('purchase_ok', '=', True)]",
        required=True,
    )

    display_name = fields.Char(
        string="Nombre a mostrar",
        related='product_id.display_name'
    )

    cantidad = fields.Float(
        string="Cantidad",
        required=True,
    )

    uom_id = fields.Many2one(
        'product.uom',
        string="U.M",
        related='product_id.uom_id'
    )

    costo = fields.Float(
        string="Costo",
        related='product_id.standard_price'
    )

    importe = fields.Float(
        string="Importe",
        compute='getimportetotal'
    )

    @api.one
    @api.depends('cantidad','costo')
    def getimportetotal(self):
        if self.cantidad and self.costo:
            total = self.cantidad * self.costo
            self.importe = total
        else:
            self.importe = 0.00
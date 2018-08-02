# -*- coding: utf-8 -*-
"""
* Created by gonzalezoscar on 31/07/18
* expenses
"""
from odoo import api, fields, models


class OrdenTrabajo(models.Model):
    _name = 'ops4g.orden_trabajo'

    name = fields.Char(
        string="Nombre",
        default=lambda self: 'OT000X',
        required=True,
    )

    descripcion = fields.Char(
        string=u"Descripción",
        required=True,
    )

    responsable = fields.Many2one(
        'hr.employee',
        string="Responsable",
        required=True,
    )

    responsable_supervision = fields.Many2one(
        'hr.employee',
        string="Responsable de supervisión",
    )

    costo_horas_hombre = fields.Float(
        string="Costo horas hombre",
        compute="get_subcostos",
    )

    costo_recursos = fields.Float(
        string="Costo recursos",
        compute="get_subcostos"
    )

    costo_total = fields.Float(
        string="Costo total",
        compute="get_costototal"
    )

    tareas_ids = fields.One2many(
        'ops4g.tareas',
        'orden_trabajo_id',
        string="Tareas",
    )

    @api.model
    def create(self, vals):
        if vals.get('name', 'OT000X') == 'OT000X':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'ops4g_orden_trabajo'
            ) or 'OT000X'
        return super(OrdenTrabajo, self).create(vals)

    @api.one
    @api.depends('tareas_ids')
    def get_subcostos(self):
        for record in self:
            if len(record.tareas_ids) > 0:
                costo_horas_hombre = 0
                costo_recursos = 0
                for tarea in record.tareas_ids:
                    costo_recusos_tarea = tarea.tarea_id.costo_recursos
                    if costo_recusos_tarea:
                        costo_recursos += costo_recusos_tarea
                    costo_horas_hombre += tarea.importe
                record.costo_horas_hombre = costo_horas_hombre
                record.costo_recursos = costo_recursos

    @api.multi
    @api.depends('costo_horas_hombre', 'costo_recursos')
    def get_costototal(self):
        for record in self:
            if record.costo_recursos > 0 and record.costo_horas_hombre > 0:
                costo_total = record.costo_recursos + record.costo_horas_hombre
                record.costo_total = costo_total
            else:
                record.costo_total = 0.00

"""
* Created by gonzalezoscar on 31/07/18
* expenses
"""

# -*- coding: utf-8 -*-
from odoo import api, fields, models
import datetime


class Tareas(models.Model):
    _name = 'ops4g.tareas'

    tarea_id = fields.Many2one(
        'project.task',
        string="Tarea",
        required=True
    )

    ejecuta_employee_id = fields.Many2one(
        'hr.employee',
        string="Ejecuta",
    )

    fecha_hora = fields.Datetime(
        string="Fecha y hora",
        default=lambda self: fields.datetime.now(),
    )

    horas = fields.Float(
        string="Horas",
    )

    costo_hora = fields.Float(
        string="$ / Hora",
        related="ejecuta_employee_id.costo_hora",
        readonly=True
    )

    importe = fields.Float(
        string="Importe",
        compute="getimporte",
    )

    orden_trabajo_id = fields.Many2one(
        'ops4g.orden_trabajo',
        string="Orden de trabajo"
    )

    @api.one
    @api.depends('horas', 'costo_hora')
    def getimporte(self):
        for record in self:
            importe_total = record.horas * record.costo_hora
            record.importe = importe_total

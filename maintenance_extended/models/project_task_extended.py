# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ProjectTaskExtended(models.Model):
    _inherit = 'project.task'

    finalizada = fields.Boolean(
        string="Finalizada"
    )

    project_id = fields.Many2one(
        'project.project',
        default=lambda self: self.env.ref('maintenance_extended.maintenance_project'),
    )

    costo_recursos = fields.Float(
        string="Costo de Recursos",
        compute='getcostorecursos',
    )

    listado_materiales_ids = fields.One2many(
        'ops4g.materiales',
        'task_id',
        string="Listado de materiales"
    )

    @api.multi
    @api.depends('listado_materiales_ids')
    def getcostorecursos(self):
        for record in self:
            total_recursos = 0
            for material in record.listado_materiales_ids:
                total_recursos += material.importe
            record.costo_recursos = total_recursos

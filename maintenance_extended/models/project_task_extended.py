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

    x_ot_relacionada = fields.Many2one(
        'ops4g.orden_trabajo',
        string="Última orden de trabajo relacionada",
        compute='getotrelacionada',
        help="Aquí se muestra de ultima orden de trabajo que se ha relacionado a esta tarea"
    )

    @api.multi
    @api.depends('listado_materiales_ids')
    def getcostorecursos(self):
        for record in self:
            total_recursos = 0
            for material in record.listado_materiales_ids:
                total_recursos += material.importe
            record.costo_recursos = total_recursos

    @api.multi
    def getotrelacionada(self):
        for record in self:
            if record.listado_materiales_ids:
                s4g_tareas = record.env['ops4g.tareas'].sudo().search(
                    [
                        ('tarea_id.id', '=', record.id),
                    ]
                )

                if s4g_tareas:
                    print("Tareas relacionadas")
                    print(s4g_tareas)

                    if s4g_tareas[-1]:
                        record.x_ot_relacionada = s4g_tareas[-1].orden_trabajo_id
                    else:
                        record.x_ot_relacionada = s4g_tareas[0].orden_trabajo_id
                else:
                    print("\n *****No hay tareas relacionadas")



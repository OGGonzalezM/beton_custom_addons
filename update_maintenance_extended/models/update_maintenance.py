# encoding: utf-8
# Created by Oscar Gonzalez at 9/08/18
# Created to beton_custom
from odoo import api, fields, models


class UpdateMaintenance(models.Model):
    _inherit = 'project.task'

    x_ot_relacionada = fields.Many2one(
        'ops4g.orden_trabajo',
        string="Última orden de trabajo relacionada",
        compute='getotrelacionada',
        # store=True,
        help="Aquí se muestra de ultima orden de trabajo que se ha relacionado a esta tarea",
    )

    @api.multi
    def getotrelacionada(self):
        for record in self:
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
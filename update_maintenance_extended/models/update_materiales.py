# encoding: utf-8
# Created by Oscar Gonzalez at 9/08/18
# Created to beton_custom
from odoo import fields, models


class UpdateMateriales(models.Model):
    _inherit = 'ops4g.materiales'

    ot_relacionada_tarea_id = fields.Many2one(
        'ops4g.orden_trabajo',
        string="Orden de trabajo",
        related='task_id.x_ot_relacionada',
        store=True,
    )

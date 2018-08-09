# -*- coding: utf-8 -*-
{
    'name': "Mantenimiento extended",

    'summary':
        """
            * Extendido el módulo de mantenimiento
        """,

    'description':
        """
            * Crear Ordenes de trabajo para el mantenimiento
            * Datos agregados a las tareas.
        """,

    'author': "Soluciones4G - OGM",
    'website': "www.soluciones4g.com",
    'license': 'AGPL-3',

    'category': 'Extra Tools',
    'version': '0.1',

    'depends': [
        'base',
        'purchase',
        'project',
        'maintenance',
        'hr',
        'stock'
    ],

    'demo': [],

    'data': [
        'security/ir.model.access.csv',
        'data/maintenance_project.xml',
        'views/hr_employee_extended_view.xml',
        'views/project_task_extended_view.xml',
        'data/orden_trabajo_consecutivo.xml',
        'views/orden_trabajo_view.xml',
        'views/maintenance_request_extended_view.xml',
        'views/purchase_order_extended_view.xml',
        'report/orden_trabajo_report.xml',
        'views/materiales_view.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,
}

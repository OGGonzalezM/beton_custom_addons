# -*- coding: utf-8 -*-
{
    'name': "Actualización para mantenimiento",

    'summary':
        """
            * Extendido el módulo de mantenimiento
        """,

    'description':
        """
        """,

    'author': "Soluciones4G - OGM",
    'website': "www.soluciones4g.com",
    'license': 'AGPL-3',

    'category': 'Extra Tools',
    'version': '0.1',

    'depends': [
        'base',
        'project',
        'maintenance_extended',
    ],

    'demo': [],

    'data': [
        'views/update_maintenance_extended_view.xml',
        'views/update_materiales_view.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,
}

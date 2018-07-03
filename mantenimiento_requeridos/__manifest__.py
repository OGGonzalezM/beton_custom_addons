# -*- coding: utf-8 -*-
{
    'name': "Mantenimiento requerimientos",

    'summary': """
        Agregado de campos para el modulo de mantenimiento""",

    'description': """
        Modificaciones al modulo de mantenimiento
    """,

    'author': "Soluciones4g",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','maintenance'],

    # always loaded
    'data': [
        'views/agregar_campo_vehiculo_view.xml',
    ],
    'installable':True,
    'auto_install':False,
}

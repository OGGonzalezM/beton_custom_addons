# -*- coding: utf-8 -*-
{
    'name': "Seguimiento de proyectos Beton",

    'summary': """
        Agregado de campos en parte de proyecto""",

    'description': """
        Agregado de campos para el seguimiento de proyectos en Beton, agregados: folio, equipo
    """,

    'author': "Soluciones4g",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'account',
        'analytic',
        'account_accountant',
        'fleet',
        'project',
        'hr_timesheet',
        'mail'
    ],

    # always loaded
    'data': [
        'views/campo_vehiculos_cuentasa.xml',
        #'views/seguimiento_proyectos_fields_view.xml',
    ],
    'installable':True,
    'auto_install':False,
}

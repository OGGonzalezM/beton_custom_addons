# -*- coding: utf-8 -*-
{
    'name': "Report projects following",

    'summary': """
        Edición del reporte generado en las cuentas analiticas""",

    'description': """
        Reporte editado para mostrar datos del proyecto en cuestión
    """,

    'author': "Soluciones4g",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','project','analytic'],

    # always loaded
    'data': [
        'views/edicion_reporte_horas.xml',
        'views/edicion_vista_arbol_proyectos_view.xml',
        'report/reporte_proyectos.xml',
    ],
    'installable':True,
    'auto_install':False,
}

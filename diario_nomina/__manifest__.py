# -*- coding: utf-8 -*-
{
    'name': "Diario Nomina",

    'summary': """
        Deshabilitar campo requerido del diario de salarios""",

    'description': """
        Modulo creado para BETON
    """,

    'author': "Soluciones4g",
    'website': "http://www.soluciones4g.com",
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['hr_payroll'],

    # always loaded
    'data': ['views/diario_nomina_view.xml'],
    'installable':True,
    'auto_install':False,
}

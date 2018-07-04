# -*- coding: utf-8 -*-
{
    'name': "Nomina",

    'summary': """
        Creación de las lineas de dias trabajados con codigo WORK100""",

    'description': """
        Modulo creado para BETON
    """,

    'author': "Soluciones4g",
    'website': "http://www.soluciones4g.com",
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['account','hr','hr_payroll','hr_contract'],

    # always loaded
    'data': ['views/hr_payslip_view.xml'],
    'installable':True,
    'auto_install':False,
}

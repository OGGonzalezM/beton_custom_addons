# -*- coding: utf-8 -*-
{
    'name': "Agregar campos a empleados",

    'summary': """Datos de empleados""",

    'description': """
    """,

    'author': "Soluciones4G",
    'website': "soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_dat$
    # for the full list
    'category': 'Sale Wizard',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr','hr_recruitment', 'hr_payroll', 'hr_contract', 'hr_mx_ext'],

    # always loaded
    'data': [
        'views/fields_employees_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}

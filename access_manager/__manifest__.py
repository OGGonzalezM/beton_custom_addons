# -*- coding: utf-8 -*-
{
    'name': "Access Manager",

    'summary': """
            * Extensión de las facturas de clientes
        """,

    'description':
        """
            * Agregados permisos de acceso para que solo 
              cierto grupo de usuarios pueda crear cuentas contables
        """,

    'author': "Soluciones4G - OGM",
    'website': "",

    'category': 'Extra Tools',
    'version': '1.0',

    'depends': [
        'base',
        'account_accountant',
        'analytic',
        'project',
    ],

    'demo': [],

    'data': [
        'security/security_groups.xml',
        'security/ir.model.access.csv',
    ],

    'installable': True,
    'auto_install': False,
}

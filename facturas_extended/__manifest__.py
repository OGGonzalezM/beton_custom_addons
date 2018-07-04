# -*- coding: utf-8 -*-
{
    'name': "Facturas Extended",

    'summary': """
            -Cuenta analitica para los registros de las facturas de clientes y proveedores
        """,

    'description':
        """
            Datos agregados para las facturas de los clientes y proveedores
        """,

    'author': "Soluciones4G - OGM",
    'website': "",

    'category': 'Extra Tools',
    'version': '1.0',

    'depends': [
        'base',
        'account',
    ],

    'demo': [],

    'data': [
        'views/invoices_inherited_view.xml',
    ],

    'installable': True,
    'auto_install': False,
}

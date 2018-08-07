# -*- coding: utf-8 -*-
{
    'name': "Extensión a reportes",

    'summary':
        """
            * Edición o agregado de datos en los reportes
        """,

    'description':
        """
            * Agregado de campos a la impresión de reportes
        """,

    'author': "Soluciones4G - OGM",
    'website': "www.soluciones4g.com",
    'license': 'AGPL-3',

    'category': 'Extra Tools',
    'version': '0.1',

    'depends': [
        'base',
        'purchase',
        'sale',
    ],

    'demo': [],

    'data': [
        'report/report_purchaseorder_document_extended.xml',
        'report/report_purchasequotation_document_extended.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,
}

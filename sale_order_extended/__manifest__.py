# -*- coding: utf-8 -*-
{
    'name': "Detalles orden de venta",

    'summary': """
        Agregado de campos para las ordenes de venta""",

    'description': """
        Agregar campos para el detalle de una orden de venta
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','sale','fleet',],

    'data': [
        'views/sale_order_extended_view.xml',
	'reports/sale_order_extended_report.xml',
    ],
    'installable':True,
    'auto_install':False,
}

# -*- coding: utf-8 -*-
{
    'name': "Sale Geographic Filter",

    'summary': """
        Adds a "Group by state" and "Group by country" options in sales
        """,

    'description': """
        This module adds a "Group by state" and "Group by country" options
        to the quotations and sales orders tree view
    """,

    'author': "Alberto Carollo",
    'website': "http://www.ecobeton.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
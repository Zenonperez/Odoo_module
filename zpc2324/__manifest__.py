# -*- coding: utf-8 -*-
{
    'name': "zpc2324",

    'summary': """
        Odoo module for doing a project with a team""",

    'description': """
        Odoo module for doing a project with a team""",

    'author': "Zenon",
    'website': "https://github.com/Zenonperez/Odoo_module",

    'images': ['static/description/icon.png'],
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Generic Modules',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'views/template_report_member.xml',
        'views/template_report_task.xml',
        'views/template_report_team.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml'
    ],
    'installable': True,
    'application': True,
}

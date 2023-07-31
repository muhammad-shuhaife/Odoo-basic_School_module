# -*- coding: utf-8 -*-
{
    'name': "student",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','product','account','mail','website'],

    # always loaded
    'data': [

        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/bookAllocationWizard.xml',
        'wizard/subjectAllocate.xml',
        'wizard/itemsWizard.xml',
        'data/ir_sequence_data.xml',
        'data/email_template.xml',
        'views/student.xml',
        'views/teacher.xml',
        'views/class.xml',
        'views/division.xml',
        'views/subject.xml',
        'views/templates.xml',
        'data/crone.xml',
        'reports/student_card.xml',
        'reports/book_allocation_report.xml',
        'reports/saleOrderReport.xml',
        'views/users.xml',
        'views/bookAllocation.xml',
        'views/library.xml',
        # 'views/asset.xml',
        'views/items.xml',
        'views/context_inherit.xml',
        'views/employee.xml',
        'views/company.xml',
        # 'views/car_rental.xml',
        'views/website_menu.xml',
        'views/settings_view.xml',
        'views/stud_registration.xml',





    ],
    'qweb': [
        # 'static/src/js/invoice_custom_message.js',


         ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

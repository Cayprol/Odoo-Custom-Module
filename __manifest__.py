# -*- coding: utf-8 -*-
{
    'name': "OVIS",

    'summary': """Custom Module for OVIS""",

    'description': """
        OVIS  module for daily operation:
            - Additional Product Fields
            - Additional Shortcut to Views
    """,
    'installable': True,
    'application': True,
    
    'author': "Cayprol",
    'website': "http://www.ovis.com.tw",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'TEST',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'sale', 'purchase', 'product', 'stock', 'mrp'],
    # always loaded
    'data': [
        'views/inherit_product_supplierinfo_form_view.xml',
        'views/inherit_product_template_only_form_views.xml',
        'views/inherit_stock_picking_views.xml',
        'views/inherit_view_partner_form.xml',
        'views/inherit_view_order_form.xml',
        # 'views/product_molding_form_view.xml',  THIS WAS CREATED DURING TESTING
        'views/stock_picking_shipping.xml',
        'views/sales_menu.xml',
        'views/purchases_menu.xml',
        'report/report_packing_list.xml',
        'report/report_pro_forma_invoice.xml',
        'report/report_views.xml',

    ],
}


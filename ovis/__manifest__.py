{
    'name': 'OVIS',
    'version': '12.0.0',
    'category': 'Other',
    'description': 'Custom module for OVIS',
    'author': 'Cayprol',
    'depends': [
                'account',
                'base',
                'contacts',
                'purchase',
                'sale',
                'stock',
                'web',
                'confirm_popup',
                'sale_back_order',
                # 'dev_sale_delivery_by_dates',
                # 'invoice_bank_info',
                # 'invoice_statement',
                # 'invoice_without_down_payment', 
                'l10n_cn_province',
                'l10n_kr',
                'l10n_th_province',
                'l10n_tw',
                'ovis_coa'
            ],
    'data': [
            'data/product.category.csv',
            # 'data/res_config_settings.xml',
            # 'data/sequence.xml',
            'data/uom.xml',
            # 'report/purchase_order_templates.xml',
            # 'report/purchase_quotation_templates.xml',
            # 'report/purchase_reports.xml',
            # 'report/sale_report_templates.xml',
            # 'views/product_template_views.xml',
            # 'views/product_views.xml',
            # 'views/purchase_views.xml',
            # 'views/report_invoice.xml',
            'views/sale_views.xml',
            # 'views/stock_views.xml',
            # 'wizard/quote_to_order.xml',
            ],
    'license': 'AGPL-3', 
    'installable': True,
    'application'   : True,
    'auto_install'  : False,
}
# -*- encoding: utf-8 -*-
{
    'name': "OVIS",
    'version': '12.0.0',
    'summary': 'Custom Module For OVIS.',
    'category': 'Other',
    'description': """Custom Module For OVIS.""",
    'author': 'Cayprol',
    "depends" : ['base', 'mrp', 'product', 'purchase', 'sale', 'web'],
    'data': ['views/inherit_product_template_only_form_views.xml',
             ],
    "images": [],
    'license': 'LGPL-3',
    'qweb': [
            ],  
    
    'installable': True,
    'application'   : True,
    'auto_install'  : False,
}

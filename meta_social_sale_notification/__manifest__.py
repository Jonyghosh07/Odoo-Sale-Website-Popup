{
    'name': 'Social Sale Notification',
    'version': '15.0.0',
    'category': 'Extra Tools',
    'sequence': 0,
    'summary': """Custom Snippet in Website""",

    'description': """ """,

    'author': 'Metamorphosis',
    'website': "https://www.metamorphosis.com.bd",
    
    'depends': ['website', 'sale'],

    'data': [
        "security/ir.model.access.csv",
        "views/assets.xml",
        "views/purchase_bar.xml",
        "views/view_bar.xml",
    ],


    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}

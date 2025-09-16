{
    'name': 'Hello Odoo',
    'version': '1.0',
    'summary': 'Hande’nin ilk Odoo modülü',
    'description': 'Basit bir model ve form ekranı içeren deneme modülü',
    'author': 'Hande',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hello_views.xml',
    ],
    'installable': True,
    'application': True,
}
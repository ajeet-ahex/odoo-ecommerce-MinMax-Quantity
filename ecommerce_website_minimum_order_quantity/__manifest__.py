{
    'name': 'Minimum Order Quantity',
    'version': '17.0.0.1',
    'category': 'eCommerce',
    'author': 'Ahex Technologies',
    'summary': 'Easily define minimum quantities for products in your e-commerce store',
    'website': '',
    'sequence': '10',
    'description': """
     Website Customization
    """,
    'depends': ['base', 'web', 'sale', 'website_sale_stock', 'website_sale', 'website_sale_comparison', 'website_sale_product_configurator'],
    'images': [
        'static/description/banner.png',
        ],
        
    'data': [
        'views/products_view.xml',
        'views/website_product_view.xml',
    ],
    'license': 'LGPL-3',
    'application': True,
    'installable': True,
    'website': 'https://www.ahex.co',
}

{
    'name': 'App One',
    'author': 'Mohamed Hassan',
    'category': '',
    'version': '17.0.0.1.0',
    'depends': ['base', 'sale_management','mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/property_view.xml',
        'views/building_view.xml',
        'views/owner_view.xml',
        'views/tag_view.xml',
        'views/account_move_view.xml',
        'views/sale_order_view.xml',
        'views/property_history.xml',
        'wizard/change_state_wizard_view.xml',
        'reports/property_report.xml',
        'views/base_menu.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'app_one/static/src/css/property.css',
        ],
    },

    'installable': True,
    'application': True,
}

{
    'name': "qaran Hospital",

    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'sequence': -102,

    'description': "Long description of module's purpose",

    'author': "Qaran hospital ",
    'category': 'Uncategorized',
    'version': '0.1',

    'assets': {
        'web.assets_backend': [
            'qaran__hospital/static/src/css/title_fix.css',
        ],
    },
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/appointment_sequenece.xml',
        'views/menu_view.xml',
        'views/patient_view.xml',
        'views/patient_view_only.xml',
        'views/appointment.xml'

    ],

    'application': True
}

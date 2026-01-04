{
    'name': "qaran Hospital",

    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'sequence':-102,

    'description': "Long description of module's purpose",


    'author': "Qaran hospital ",
    'category': 'Uncategorized',
    'version': '0.1',

    'assets':{
        'web.assets_backend':[
            'qaran__hospital/static/src/css/title_fix.css',
        ],
    },

    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'views/menu_view.xml',
        'views/views.xml',

],

    'application':True
}


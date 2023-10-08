SPECTACULAR_SETTINGS = {
    'TITLE': 'CBE API Documentation',
    'DESCRIPTION': 'Description api',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SPECTACULAR_DEFAULTS': {
        'SERVE_PERMISSIONS': ['rest_framework.permissions.AllowAny'],
    },
    'SCHEMA_PATH_PREFIX': r'/api/v[0-9]',
}

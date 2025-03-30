from DjangoAuth0.settings.components.common import env

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}
AUTH0_DOMAIN = env('AUTH0_DOMAIN')
AUTH0_API_ID = env('AUTH0_API_ID')

JWT_AUTH = {
    'JWT_PAYLOAD_GET_USERNAME_HANDLER':
        'apps.auth0_auth.jwt_get_username_from_payload_handler',
    'JWT_DECODE_HANDLER':
        'apps.auth0_auth.jwt_decode_token',
    'JWT_ALGORITHM': 'RS256',
    'JWT_AUDIENCE': AUTH0_API_ID,
    'JWT_ISSUER': f'https://{AUTH0_DOMAIN}/',
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}
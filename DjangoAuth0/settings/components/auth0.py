from DjangoAuth0.settings.components.common import env

# User Credentials to use as Machine to Machine APP
AUTH0_MTM_CLIENT_SECRET = env('AUTH0_MTM_CLIENT_SECRET')
AUTH0_MTM_CLIENT_ID = env('AUTH0_MTM_CLIENT_ID')

# App secretes to create a USER token
AUTH0_APP_CLIENT_ID = env('AUTH0_APP_CLIENT_ID')
AUTH0_APP_CLIENT_SECRET = env('AUTH0_APP_CLIENT_SECRET')


from split_settings.tools import include

settings = [
    'components/common.py',
    'components/auth0.py',
    'components/drf.py',
    'settings.py'
]

include(*settings)
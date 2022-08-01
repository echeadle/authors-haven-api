from .base import *
from .base import env


DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='django-insecure-l17_&4)9@n^(d9+549%qr*nyap$93n*9-5)4wsuhsjv$=)eg(a',

)
ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']

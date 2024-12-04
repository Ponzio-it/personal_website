from .base import *

environ.Env.read_env(env_file='.env.production')

DEBUG = False
ALLOWED_HOSTS= env('ALLOWED_HOST').split(',')

STATICFILES_DIRS = [BASE_DIR/ 'portfolio' / 'static']
STATIC_ROOT = BASE_DIR/ 'mypersonalsite'/ 'staticfiles'

EMAIL_BACKEND = env('EMAIL_BACKEND')
EMAIL_HOST = env('EMAIL_HOST') 
EMAIL_PORT = env.int('EMAIL_PORT')
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL =  env('DEFAULT_FROM_EMAIL')
ADMIN_EMAIL = env('ADMIN_EMAIL')


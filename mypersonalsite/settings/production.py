from .base import *

environ.Env.read_env(env_file='.env.production')

DEBUG = False
ALLOWED_HOSTS= env("ALLOWED_HOST").split(',')

SECURE_SSL_REDIRECT = True  # Redirect all HTTP traffic to HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')  # Recognize HTTPS requests behind a proxy
SESSION_COOKIE_SECURE = True  # Secure cookies
CSRF_COOKIE_SECURE = True  # Secure CSRF cookies
SECURE_HSTS_SECONDS = 31536000  # Enable HTTP Strict Transport Security (1 year)
SECURE_HSTS_PRELOAD = True  # Allow browser preload of HSTS
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains

STATIC_URL = '/static/'
STATICFILES_DIRS = []
STATIC_ROOT = BASE_DIR / 'mypersonalsite'/ 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

EMAIL_BACKEND = env('EMAIL_BACKEND')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env.int('EMAIL_PORT')
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL =  env('DEFAULT_FROM_EMAIL')
ADMIN_EMAIL = env('ADMIN_EMAIL')


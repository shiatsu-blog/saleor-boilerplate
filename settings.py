# -*- coding: utf-8 -*-
INSTALLED_ADDONS = [
    # <INSTALLED_ADDONS>  # Warning: text inside the INSTALLED_ADDONS tags is auto-generated. Manual changes will be overwritten.
    'aldryn-addons',
    'aldryn-django',
    'aldryn-sso',
    # </INSTALLED_ADDONS>
]

import aldryn_addons.settings
aldryn_addons.settings.load(locals())

# all django settings can be altered here
import ast
import os.path

import dj_database_url
import dj_email_url
import django_cache_url
from django.contrib.messages import constants as messages
from django.utils.translation import gettext_lazy as _, pgettext_lazy
from django_prices.templatetags.prices_i18n import get_currency_fraction

INSTALLED_APPS.extend([
    # add your project specific apps here
    'django.forms',

    # Local apps
    'saleor.account',
    'saleor.discount',
    'saleor.product',
    'saleor.checkout',
    'saleor.core',
    'saleor.graphql',
    'saleor.menu',
    'saleor.order',
    'saleor.dashboard',
    'saleor.seo',
    'saleor.shipping',
    'saleor.search',
    'saleor.site',
    'saleor.data_feeds',
    'saleor.page',
    'saleor.payment',

    # External apps
    'django.contrib.postgres',
    'versatileimagefield',
    'django_babel',
    'bootstrap4',
    'django_measurement',
    'django_prices',
    'django_prices_openexchangerates',
    'django_prices_vatlayer',
    'graphene_django',
    'mptt',
    'webpack_loader',
    'social_django',
    'django_countries',
    'django_filters',
    'django_celery_results',
    'impersonate',
    'phonenumber_field',
    'captcha',
])


def get_list(text):
    return [item.strip() for item in text.split(',')]


BASE_DIR = os.path.join(os.path.join(os.path.dirname(__file__), 'app'))

# ROOT_URLCONF = 'saleor.urls'

DEBUG = os.environ.get('DEBUG', False)

INTERNAL_IPS = get_list(os.environ.get('INTERNAL_IPS', '127.0.0.1'))

# Some cloud providers (Heroku) export REDIS_URL variable instead of CACHE_URL
REDIS_URL = os.environ.get('REDIS_URL')
if REDIS_URL:
    CACHE_URL = os.environ.setdefault('CACHE_URL', REDIS_URL)
CACHES = {'default': django_cache_url.config()}

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://postgres:postgres@localhost:5432/db',
        conn_max_age=600)}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('ar', _('Arabic')),
    ('az', _('Azerbaijani')),
    ('bg', _('Bulgarian')),
    ('bn', _('Bengali')),
    ('ca', _('Catalan')),
    ('cs', _('Czech')),
    ('da', _('Danish')),
    ('de', _('German')),
    ('en', _('English')),
    ('es', _('Spanish')),
    ('fa', _('Persian')),
    ('fr', _('French')),
    ('hi', _('Hindi')),
    ('hu', _('Hungarian')),
    ('it', _('Italian')),
    ('ja', _('Japanese')),
    ('ko', _('Korean')),
    ('mn', _('Mongolian')),
    ('nb', _('Norwegian')),
    ('nl', _('Dutch')),
    ('pl', _('Polish')),
    ('pt-br', _('Brazilian Portuguese')),
    ('ro', _('Romanian')),
    ('ru', _('Russian')),
    ('sk', _('Slovak')),
    ('sr', _('Serbian')),
    ('sv', _('Swedish')),
    ('tr', _('Turkish')),
    ('uk', _('Ukrainian')),
    ('vi', _('Vietnamese')),
    ('zh-hans', _('Simplified Chinese')),
    ('zh-hant', _('Traditional Chinese'))]
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]
USE_I18N = True
USE_L10N = True
USE_TZ = True

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

ENABLE_SSL = os.environ.get('ENABLE_SSL', False)

if ENABLE_SSL:
    SECURE_SSL_REDIRECT = not DEBUG

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static/')
STATIC_URL = os.environ.get('STATIC_URL', '/static/')

STATICFILES_DIRS = [
    ('assets', os.path.join(STATIC_ROOT, 'assets')),
    ('favicons', os.path.join(STATIC_ROOT, 'favicons')),
    ('images', os.path.join(STATIC_ROOT, 'images')),
    ('dashboard', os.path.join(STATIC_ROOT, 'dashboard')),
    ('dashboard/images', os.path.join(STATIC_ROOT, 'dashboard', 'images'))]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder']

context_processors = [
    'django.contrib.auth.context_processors.auth',
    'django.template.context_processors.debug',
    'django.template.context_processors.i18n',
    'django.template.context_processors.media',
    'django.template.context_processors.static',
    'django.template.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.template.context_processors.request',
    'saleor.core.context_processors.default_currency',
    'saleor.checkout.context_processors.cart_counter',
    'saleor.core.context_processors.search_enabled',
    'saleor.site.context_processors.site',
    'social_django.context_processors.backends',
    'social_django.context_processors.login_redirect']

loaders = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader']

if not DEBUG:
    loaders = [('django.template.loaders.cached.Loader', loaders)]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates', os.path.join(BASE_DIR, 'templates/')],
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': context_processors,
            'loaders': loaders,
            'string_if_invalid': '<< MISSING VARIABLE "%s" >>' if DEBUG else ''
        },
    },
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django_babel.middleware.LocaleMiddleware',
    'saleor.core.middleware.discounts',
    'saleor.core.middleware.google_analytics',
    'saleor.core.middleware.country',
    'saleor.core.middleware.currency',
    'saleor.core.middleware.site',
    'saleor.core.middleware.taxes',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'impersonate.middleware.ImpersonateMiddleware',
    'saleor.graphql.middleware.jwt_middleware'
]

if DEBUG:
    MIDDLEWARE.append(
        'debug_toolbar.middleware.DebugToolbarMiddleware')
    INSTALLED_ADDONS.append('debug_toolbar')
    DEBUG_TOOLBAR_PANELS = [
        # adds a request history to the debug toolbar
        'ddt_request_history.panels.request_history.RequestHistoryPanel',

        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
        'debug_toolbar.panels.profiling.ProfilingPanel',
    ]
    DEBUG_TOOLBAR_CONFIG = {
        'RESULTS_CACHE_SIZE': 100}

ENABLE_SILK = os.environ.get('ENABLE_SILK', False)
if ENABLE_SILK:
    MIDDLEWARE.insert(0, 'silk.middleware.SilkyMiddleware')
    INSTALLED_ADDONS.append('silk')

AUTH_USER_MODEL = 'account.User'

LOGIN_URL = '/account/login/'

DEFAULT_COUNTRY = os.environ.get('DEFAULT_COUNTRY', 'US')
DEFAULT_CURRENCY = os.environ.get('DEFAULT_CURRENCY', 'USD')
DEFAULT_DECIMAL_PLACES = get_currency_fraction(DEFAULT_CURRENCY)
DEFAULT_MAX_DIGITS = 12
AVAILABLE_CURRENCIES = [DEFAULT_CURRENCY]
COUNTRIES_OVERRIDE = {
    'EU': pgettext_lazy(
        'Name of political and economical union of european countries',
        'European Union')}

OPENEXCHANGERATES_API_KEY = os.environ.get('OPENEXCHANGERATES_API_KEY')

# VAT configuration
# Enabling vat requires valid vatlayer access key.
# If you are subscribed to a paid vatlayer plan, you can enable HTTPS.
VATLAYER_ACCESS_KEY = os.environ.get('VATLAYER_ACCESS_KEY')
VATLAYER_USE_HTTPS = os.environ.get('VATLAYER_USE_HTTPS', False)

ACCOUNT_ACTIVATION_DAYS = 3

LOGIN_REDIRECT_URL = 'home'

GOOGLE_ANALYTICS_TRACKING_ID = os.environ.get('GOOGLE_ANALYTICS_TRACKING_ID')


def get_host():
    from django.contrib.sites.models import Site
    return Site.objects.get_current().domain

PAYMENT_HOST = get_host

PAYMENT_MODEL = 'saleor.order.Payment'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# # Do not use cached session if locmem cache backend is used but fallback to use
# # default django.contrib.sessions.backends.db instead
# if not CACHES['default']['BACKEND'].endswith('LocMemCache'):
#     SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
#
MESSAGE_TAGS = {
    messages.ERROR: 'danger'}

LOW_STOCK_THRESHOLD = 10
MAX_CART_LINE_QUANTITY = int(os.environ.get('MAX_CART_LINE_QUANTITY', 50))

PAGINATE_BY = 16
DASHBOARD_PAGINATE_BY = 30
DASHBOARD_SEARCH_LIMIT = 5

bootstrap4 = {
    'set_placeholder': False,
    'set_required': False,
    'success_css_class': '',
    'form_renderers': {
        'default': 'saleor.core.utils.form_renderer.FormRenderer'}}

# ALLOWED_HOSTS = get_list(
#     os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1'))
# ALLOWED_GRAPHQL_ORIGINS = os.environ.get('ALLOWED_GRAPHQL_ORIGINS', '*')
#
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
    'products': [
        ('product_gallery', 'thumbnail__540x540'),
        ('product_gallery_2x', 'thumbnail__1080x1080'),
        ('product_small', 'thumbnail__60x60'),
        ('product_small_2x', 'thumbnail__120x120'),
        ('product_list', 'thumbnail__255x255'),
        ('product_list_2x', 'thumbnail__510x510')],
    'background_images': [
        ('header_image', 'thumbnail__1080x440')]}

VERSATILEIMAGEFIELD_SETTINGS = {
    # Images should be pre-generated on Production environment
    'create_images_on_demand': DEBUG,
}

PLACEHOLDER_IMAGES = {
    60: 'images/placeholder60x60.png',
    120: 'images/placeholder120x120.png',
    255: 'images/placeholder255x255.png',
    540: 'images/placeholder540x540.png',
    1080: 'images/placeholder1080x1080.png'}

DEFAULT_PLACEHOLDER = 'images/placeholder255x255.png'

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'assets/',
        'STATS_FILE': '/app/webpack/webpack-bundle.json',
        'POLL_INTERVAL': 0.1,
        'IGNORE': [
            r'.+\.hot-update\.js',
            r'.+\.map']}}

LOGOUT_ON_PASSWORD_CHANGE = False

# SEARCH CONFIGURATION
DB_SEARCH_ENABLED = True

# support deployment-dependant elastic enviroment variable
ES_URL = (
    os.environ.get('ELASTICSEARCH_URL')
    or os.environ.get('SEARCHBOX_URL')
    or os.environ.get('BONSAI_URL'))

ENABLE_SEARCH = bool(ES_URL) or DB_SEARCH_ENABLED  # global search disabling

SEARCH_BACKEND = 'saleor.search.backends.postgresql'

if ES_URL:
    SEARCH_BACKEND = 'saleor.search.backends.elasticsearch'
    INSTALLED_ADDONS.append('django_elasticsearch_dsl')
    ELASTICSEARCH_DSL = {
        'default': {
            'hosts': ES_URL}}

AUTHENTICATION_BACKENDS = [
    'saleor.account.backends.facebook.CustomFacebookOAuth2',
    'saleor.account.backends.google.CustomGoogleOAuth2',
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend']

SOCIAL_AUTH_PIPELINE = [
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details']

SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_USER_MODEL = AUTH_USER_MODEL
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, email'}
# As per March 2018, Facebook requires all traffic to go through HTTPS only
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

# CELERY SETTINGS
CELERY_BROKER_URL = os.environ.get(
    'CELERY_BROKER_URL', os.environ.get('CLOUDAMQP_URL')) or ''
CELERY_TASK_ALWAYS_EAGER = not CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'django-db'

# Impersonate module settings
IMPERSONATE = {
    'URI_EXCLUSIONS': [r'^dashboard/'],
    'CUSTOM_USER_QUERYSET': 'saleor.account.impersonate.get_impersonatable_users',  # noqa
    'USE_HTTP_REFERER': True,
    'CUSTOM_ALLOW': 'saleor.account.impersonate.can_impersonate'}


# Rich-text editor
ALLOWED_TAGS = [
    'a',
    'b',
    'blockquote',
    'br',
    'em',
    'h2',
    'h3',
    'i',
    'img',
    'li',
    'ol',
    'p',
    'strong',
    'ul']
ALLOWED_ATTRIBUTES = {
    '*': ['align', 'style'],
    'a': ['href', 'title'],
    'img': ['src']}
ALLOWED_STYLES = ['text-align']


# Slugs for menus precreated in Django migrations
DEFAULT_MENUS = {
    'top_menu_name': 'navbar',
    'bottom_menu_name': 'footer'}

# This enable the new 'No Captcha reCaptcha' version (the simple checkbox)
# instead of the old (deprecated) one. For more information see:
#   https://github.com/praekelt/django-recaptcha/blob/34af16ba1e/README.rst
NOCAPTCHA = True

# Set Google's reCaptcha keys
RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')

SERIALIZATION_MODULES = {
    'json': 'saleor.core.utils.json_serializer'}


DUMMY = 'dummy'
BRAINTREE = 'braintree'
RAZORPAY = 'razorpay'
STRIPE = 'stripe'

CHECKOUT_PAYMENT_GATEWAYS = {
    DUMMY: pgettext_lazy('Payment method name', 'Dummy gateway')}

PAYMENT_GATEWAYS = {
    DUMMY: {
        'module': 'saleor.payment.gateways.dummy',
        'connection_params': {}},
    BRAINTREE: {
        'module': 'saleor.payment.gateways.braintree',
        'connection_params': {
            'sandbox_mode': os.environ.get('BRAINTREE_SANDBOX_MODE', True),
            'merchant_id': os.environ.get('BRAINTREE_MERCHANT_ID'),
            'public_key': os.environ.get('BRAINTREE_PUBLIC_KEY'),
            'private_key': os.environ.get('BRAINTREE_PRIVATE_KEY')
        }
    },
    RAZORPAY: {
        'module': 'saleor.payment.gateways.razorpay',
        'connection_params': {
            'public_key': os.environ.get('RAZORPAY_PUBLIC_KEY'),
            'secret_key': os.environ.get('RAZORPAY_SECRET_KEY'),
            'prefill': os.environ.get('RAZORPAY_PREFILL', True),
            'store_name': os.environ.get('RAZORPAY_STORE_NAME'),
            'store_image': os.environ.get('RAZORPAY_STORE_IMAGE')
        }
    },
    STRIPE: {
        'module': 'saleor.payment.gateways.stripe',
        'connection_params': {
            'public_key': os.environ.get('STRIPE_PUBLIC_KEY'),
            'secret_key': os.environ.get('STRIPE_SECRET_KEY'),
            'store_name': os.environ.get(
                'STRIPE_STORE_NAME', 'Saleor'),
            'store_image': os.environ.get('STRIPE_STORE_IMAGE', None),
            'prefill': os.environ.get('STRIPE_PREFILL', True),
            'remember_me': os.environ.get('STRIPE_REMEMBER_ME', True),
            'locale': os.environ.get('STRIPE_LOCALE', 'auto'),
            'enable_billing_address': os.environ.get(
                'STRIPE_ENABLE_BILLING_ADDRESS', False),
            'enable_shipping_address': os.environ.get(
                'STRIPE_ENABLE_SHIPPING_ADDRESS', False)
        }
    }
}

GRAPHENE = {
    'RELAY_CONNECTION_ENFORCE_FIRST_OR_LAST': True,
    'RELAY_CONNECTION_MAX_LIMIT': 100
}
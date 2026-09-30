"""
Django settings for Tuproqqal'a Tuman Maktabgacha va Maktab Ta'limi Bo'limi
(Render uchun moslashtirilgan)
"""
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# Render o'zi RENDER=true muhit o'zgaruvchisini qo'yadi
ON_RENDER = 'RENDER' in os.environ

# Render'da SECRET_KEY ni Environment bo'limida belgilang.
# Lokal ishlashda pastdagi zaxira kalit ishlatiladi.
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-tuproqqala-talim-bolimi-secret-key-2024',
)

# Render'da avtomatik DEBUG=False, lokal kompyuterda DEBUG=True.
# Xohlasangiz Environment'da DEBUG=True/False deb majburlash mumkin.
DEBUG = False

ALLOWED_HOSTS = ['tuproqqalatumanmmtb.uz', 'www.tuproqqalatumanmmtb.uz', '192.168.1.39']
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

CSRF_TRUSTED_ORIGINS = [
    'https://tuproqqalatumanmmtb.uz',
    'https://www.tuproqqalatumanmmtb.uz',
    'https://mmtb.onrender.com',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third party
    'ckeditor',
    'ckeditor_uploader',
    # Local apps
    'main',
    'news',
    'schools',
    'gallery',
    'staff_app',
    'contacts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # statik fayllar uchun
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Doimiy disk ulasangiz (masalan /var/data), Render Environment'ga
# DATA_DIR=/var/data qo'shing. Aks holda loyiha papkasi ishlatiladi
# (Render'da bunday holda ma'lumotlar har deploy'da o'chib ketadi).
DATA_DIR = Path(os.environ.get('DATA_DIR', BASE_DIR))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATA_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'uz'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

# Statik fayllar
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
# static/ papkasi bo'lmasa ogohlantirish chiqmasligi uchun shart qo'yildi
STATICFILES_DIRS = [BASE_DIR / 'static'] if (BASE_DIR / 'static').exists() else []

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage',
    },
}

# Media fayllar (yuklangan rasmlar)
MEDIA_URL = '/media/'
MEDIA_ROOT = DATA_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Render HTTPS'ni proxy orqali beradi
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# CKEditor
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
}
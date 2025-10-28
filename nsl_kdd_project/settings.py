"""
Django settings for nsl_kdd_project project.
"""

import os
from pathlib import Path

# Construir rutas dentro del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# ===========================
# CONFIGURACIÓN BÁSICA
# ===========================
SECRET_KEY = 'tu-secret-key-aqui'
DEBUG = True
ALLOWED_HOSTS = []

# ===========================
# APPS INSTALADAS
# ===========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',  
]

# ===========================
# MIDDLEWARE
# ===========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nsl_kdd_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # <- tu carpeta templates
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

WSGI_APPLICATION = 'nsl_kdd_project.wsgi.application'

# ===========================
# BASE DE DATOS
# ===========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ===========================
# VALIDACIÓN DE CONTRASEÑAS
# ===========================
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ===========================
# CONFIGURACIÓN DE IDIOMA Y ZONA HORARIA
# ===========================
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

# ===========================
# ARCHIVOS ESTÁTICOS
# ===========================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# ===========================
# RUTA PARA ARCHIVOS ARFF
# ===========================
ARFF_FILES_DIR = '/home/janeth/DataSet/datasets/datasets/NSL-KDD'

# ===========================
# CONFIGURACIÓN DE MEDIA (si se necesita)
# ===========================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

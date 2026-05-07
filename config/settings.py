import os
import dj_database_url
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('SECRET_KEY')

# --- 開発・本番の切り替え設定 ---
DEBUG = os.getenv('DEBUG', 'True') == 'True'

# --- 独自ドメインの設定 ---
ALLOWED_HOSTS = [
    'shinotech78.com',
    'www.shinotech78.com',
    'my-photo-portfolio.onrender.com',
    'localhost',
    '127.0.0.1',
]

# Renderのプロキシ設定
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# CSRF対策の信頼済みドメイン
CSRF_TRUSTED_ORIGINS = [
    'https://shinotech78.com',
    'https://www.shinotech78.com',
    'https://my-photo-portfolio.onrender.com'
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'photos',
    'tinymce'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
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
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
if os.getenv('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(
            default=os.getenv('DATABASE_URL'),
            conn_max_age=600,
            ssl_require=True,
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# --- ストレージ設定（ハイブリッド版：修正箇所） ---

# 1. ライブラリ（django-cloudinary-storage）が内部で参照する古い形式の変数名
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# 👇 WhiteNoiseの圧縮エラーを防ぐため、Django標準に変更
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# 2. Django 5.0以降で実際にメディア・静的ファイルを管理する最新の設定
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# Cloudinary接続設定
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
}

# パスの設定
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 共通設定
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
X_FRAME_OPTIONS = 'SAMEORIGIN'

# --- TinyMCE設定（改良部分） ---
TINYMCE_DEFAULT_CONFIG = {
    'width': '100%',
    'height': 500,
    # pluginsに 'code' と 'codesample' を追加
    'plugins': 'image link lists code codesample',
    # toolbarに 'code' と 'codesample' のボタンを追加
    'toolbar': 'undo redo | formatselect | bold italic | alignleft aligncenter alignright | bullist numlist | link image | code codesample',
    # メニューバーを表示させ、その中の「表示(view)」等からアクセスできるように設定
    'menubar': 'file edit view insert format tools table help',
}

# アップロード制限
DATA_UPLOAD_MAX_MEMORY_SIZE = 15728640
FILE_UPLOAD_MAX_MEMORY_SIZE = 15728640
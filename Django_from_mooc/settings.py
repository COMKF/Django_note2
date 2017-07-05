"""
Django settings for Django_from_mooc project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 这行代码的意思是，告诉django，把apps也加入到项目搜索目录中。
# 默认情况下，Django的搜索目录，只有根目录。也就是说，Django总是从根目录下开始搜索的。
# 同时，添加了参数0，它告诉服务器，在搜索资源时，先从apps目录中搜索，再从根目录中搜索。

# 命令行运行服务器与pycharm运行服务器的原理不同。
# 命令行运行服务器严格按照setting文件执行，因此需要加上这行代码。
#   (在此，如果每次都通过命令行启动服务器，无疑是很麻烦都。有一个简单都方法：
#       通过 Tools -- Run manage.py Task 直接打开 manage.py 环境。如果没有报错，则命令行启动服务器也不会报错。)
# 而pycharm运行服务器只需要进行标记就行了。
# 如果想要在这两种情况下都能正常运行，加上各自都方法就行了。
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_7#pj1hnmkqx&7&rze=414tq-hrqem%@=n3==c2v&v^bb(4@u2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # 注册自己的APP
    'message',
    'users',
    'courses',
    'organization',
    'operation',
    # 接下来使用 xadmin 替换 Django 自带的 admin，安装方法见笔记
    'xadmin',
    'crispy_forms',
    # 需要导入两个包
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 这行代码，可以让自定义的user类覆盖Django内部的user类，格式为 APP名+类名。效果是auth_user表不会被生成类，被UserProfile表代替。
AUTH_USER_MODEL = "users.UserProfile"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Django_from_mooc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # DIRS，该参数配置模版的目录，配置完成后，即会在该目录下寻找HTML文件。
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'Django_from_mooc.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 如何配置其他数据库，如mysql。
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'djangotest',
        # 'USER':'root',
        # 'PASSWORD':'root',
        # 'HOST':'localhost',
        # 只配置这些是不够的，还需要配置mysql的驱动。方法：(在虚拟环境下，pip install pymysql)
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# LANGUAGE_CODE = 'en-us'
# 改变语言为中文
LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
# 改变时区为上海，使用本地时间
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
# 改变USE_TZ，若不改的话，django在数据库存储时间时，会填入国际时间。改为False后，就会填入当前设置时区的时间，即本地时间。
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
# 如果找不到静态文件，就这样配置。如同TEMPLATES的配置。
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

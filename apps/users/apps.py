from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    # 为APP定义名称，方便管理员或用户查看。
    # （1）设置 verbose_name
    # （2）在所在的 __init__.py 文件中写入 default_app_config = 'users.apps.UsersConfig'
    verbose_name = '用户信息'

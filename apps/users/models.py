from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# 在django内部，已经有一个自带的User表，表名是auth_user，对应的类就是AbstractUser。
# 其中有一些字段我们可以用到，那么我们可以依据这个表，创建自己的User表，方法就是继承这个AbstractUser类，然后写自己的结构。
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='昵称', default='')
    birday = models.DateField(null=True, blank=True, verbose_name='生日')
    gender = models.CharField(choices=(('male', '男'), ('female', '女')), default='female', max_length=10)
    address = models.CharField(max_length=100, default='')
    mobile = models.CharField(max_length=11, null=True, blank=True)

    image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


# 接下来定义一些与User相关的类。
# 验证码
class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(choices=(('register', '注册'), ('forget', '找回密码')), max_length=10, verbose_name='验证码类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = "邮箱验证码CESHI"  # 后面加个CESH，看看有什么效果
        verbose_name_plural = verbose_name  # 把这行代码注释掉，看看有什么效果

    def __str__(self):
        return '%s(%s)' % (self.code, self.email)  # 用格式化显示EmailVerifyRecord


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(upload_to='image/%Y/%m', verbose_name='轮播图', max_length=100)
    url = models.URLField(max_length=200, verbose_name='访问地址')
    index = models.IntegerField(default=100, verbose_name='顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

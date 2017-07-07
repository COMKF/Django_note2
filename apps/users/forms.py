__author__ = 'YMH'
from django import forms
from captcha.fields import CaptchaField


# 用于表单验证，需要继承django的forms.Form。
class LoginForm(forms.Form):
    # 字段与model字段类似。
    username = forms.CharField(required=True)
    # required属性为True，则表明该字段不能为空，否则报错。
    password = forms.CharField(required=True, min_length=4)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=4)
    captcha = CaptchaField()  # 图片验证码字段

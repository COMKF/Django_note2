__author__ = 'YMH'
import re

from django import forms
from operation.models import UserAsk


# 使用ModelForm进行表单验证
class UserAskForm(forms.ModelForm):
    class Meta:  # Meta类，指定ModelForm的属性。它可以指model类型，也可以指定检查model类的哪些字段。（如果表单中有其他字段需要验证，也可以像Form一样验证）
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']  # 添加字段验证，可以通过model中的属性进行验证。

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
        if not mobile_re.match(mobile):
            raise forms.ValidationError('手机号码格式错误')
        return mobile

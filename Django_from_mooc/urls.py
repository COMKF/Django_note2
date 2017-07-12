"""Django_from_mooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve

# 将admin替换为xadmin
import xadmin
from message import views
from users.views import user_login, LoginView, RegisterView, ActiveUserView
from organization.views import OrgView
from Django_from_mooc.settings import MEDIA_ROOT

urlpatterns = [
    # url的正则表达式必须以/结尾，即 /$ 这种形式
    url(r'^admin/', xadmin.site.urls),
    url(r'^form/$', views.getform, name='go_form'),
    url(r'^index/$', TemplateView.as_view(template_name='index.html'), name='index'),
    # url(r'^login/$', TemplateView.as_view(template_name='login.html'), name='login'),
    # url(r'^login/$', user_login, name='login'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view, name='user_active'),

    # 课程机构url配置
    url(r'^org/', include('organization.urls', namespace='org', app_name='organization')),

    # 课程url配置
    url(r'^courses/', include('courses.urls', namespace='courses', app_name='courses')),

    # 因为显示图片使用了data-url属性，所以要为显示图片专门配置一个url。
    url(r'^media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT}),
]

__author__ = 'YMH'

from django.conf.urls import url
from .views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, AddFavView

# app_name = 'org'
urlpatterns = [
    # url的正则表达式必须以/结尾，即 /$ 这种形式
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home'),
    url(r'^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name='org_course'),

    # 收藏功能
    url(r'^add_fav/$', AddFavView.as_view(), name='add_fav'),
]

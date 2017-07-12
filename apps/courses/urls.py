__author__ = 'YMH'

from django.conf.urls import url
from .views import CourseDetailView,CourseCommentView,AddCommentView

# app_name = 'org'
urlpatterns = [
    # url的正则表达式必须以/结尾，即 /$ 这种形式
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),

    url(r'^comment/(?P<course_id>\d+)/$', CourseCommentView.as_view(), name='course_comment'),
    url(r'^add_comment/$', AddCommentView.as_view(), name='add_comment'),
]

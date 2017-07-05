import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['city', 'name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'add_time']
    search_fields = ['city', 'name', 'desc', 'click_nums', 'fav_nums', 'image', 'address']
    list_filter = ['city__name', 'name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'add_time']
    # 注意，course是Lesson的外键，直接写course是没有效果的。我们需要指定course的属性才行，比如：course__name。


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',
                    'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums']
    list_filter = ['org__name', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums',
                   'fav_nums','add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)

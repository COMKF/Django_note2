import xadmin
from .models import CityDict, CourseOrg, Teacher


class CourseOrgInline(object):
    model = CourseOrg
    extra = 0


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']

    inlines = [CourseOrgInline]  # 进行页面组装，新增城市的同时，可以新增外键为该城市的机构
    # 进行页面组装时，不能级联组装，即新增城市时，可新增机构，但不能新增外键为机构的课程
    # 但是可以组装外键同为城市的其他model

    list_editable = ['desc']  # 设置可以直接在页面上编辑的字段

    refresh_times = [3, 5, 10]  # 设置刷新间隔


class CourseOrgAdmin(object):
    list_display = ['name', 'city', 'category', 'click_nums', 'fav_nums', 'address', 'add_time']
    search_fields = ['city', 'name', 'desc', 'click_nums', 'fav_nums', 'image', 'address']
    list_filter = ['city__name', 'name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',
                    'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums']
    list_filter = ['org__name', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums',
                   'fav_nums', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)

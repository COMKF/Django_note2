from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from operation.models import UserFavorite
from .models import CourseOrg, CityDict
from .forms import UserAskForm
from courses.models import Course
from organization.models import Teacher


class OrgView(View):
    def get(self, request):
        all_orgs = CourseOrg.objects.all()  # 所有机构
        # org_nums = all_orgs.count()  # 机构总数

        # 热门机构排序及筛选
        hot_orgs = all_orgs.order_by('-click_nums')[:3]  # Django自带的排序功能

        # 筛选功能，筛选城市
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 筛选功能，筛选类别
        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)

        # 排序功能
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('-students')
            elif sort == 'courses':
                all_orgs = all_orgs.order_by('-course_nums')

        org_nums = all_orgs.count()  # 筛选后的机构总数

        # 对机构分页功能
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, 3, request=request)  # 三个参数，第一个是需要分页的集合，第二个参数是每页显示数量

        orgs = p.page(page)
        # 分页功能结束，但是网页上还需要一些改动

        cll_citys = CityDict.objects.all()  # 所有城市
        context = {'all_orgs': orgs, 'cll_citys': cll_citys, 'org_nums': org_nums, 'city_id': city_id,
                   'category': category, 'hot_orgs': hot_orgs, 'sort': sort}
        return render(request, 'org-list.html', context)


class AddUserAskView(View):
    '''用户添加咨询'''

    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            # ModelForm可以使用save方法，若方法中添加commit=True，可以直接把save提交到数据库中并进行保存。否则提交之后不会保存。
            # 这样的话，就不需要取出Form中的一个个数据，简化了代码。
            userask_form.save(commit=True)

            # 因为页面采用AJAX技术，因此返回的时候，返回的是json数据，而不是一个页面。
            # 返回json数据要用到JsonResponse。且参数是一个dict，用法如下。
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'fail', 'msg': '添加出错'})


class OrgHomeView(View):
    def get(self, request, org_id):
        # 根据id取出机构
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 再取出该机构下所有的课程
        all_courses = course_org.course_set.all()
        all_teachers = course_org.teacher_set.all()
        # all_teachers = Teacher.objects.filter(course_org=course_org)
        context = {'course_org': course_org, 'all_courses': all_courses, 'all_teachers': all_teachers}
        return render(request, 'org-detail-homepage.html', context)


class OrgCourseView(View):
    def get(self, request, org_id):
        # 根据id取出机构
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 再取出该机构下所有的课程
        all_courses = course_org.course_set.all()
        context = {'course_org': course_org, 'all_courses': all_courses}
        return render(request, 'org-detail-course.html', context)


class AddFavView(View):
    '''用户收藏及取消收藏'''
    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)
        # 判断用户是否登录
        if not request.user.is_authenticated:
            return JsonResponse({'status': 'fail', 'msg': '用户未登录'})

        exist_records = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        if exist_records:
            # 若记录已经存在，则表示用户取消收藏
            exist_records.delete()
            return JsonResponse({'status': 'fail', 'msg': '收藏'})
        else:
            user_fav = UserFavorite()
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()
                return JsonResponse({'status': 'success', 'msg': '已收藏'})
            else:
                return JsonResponse({'status': 'fail', 'msg': '收藏出错'})

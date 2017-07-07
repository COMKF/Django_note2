from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import CourseOrg, CityDict


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

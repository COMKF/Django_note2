from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from .models import Course, CourseResource
from operation.models import CourseComments


class CourseDetailView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        # 增加课程点击数
        course.click_nums += 1
        course.save()

        courseresources = CourseResource.objects.filter(course=course)

        context = {'course': course, "courseresources": courseresources}
        return render(request, 'course-detail.html', context)


class CourseCommentView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        all_comment = CourseComments.objects.filter(course=course)
        context = {'course': course, 'course': course}
        # 不再往下写了
        return render(request, 'course-comment.html', context)


class AddCommentView(View):
    def post(self, request):
        '''用户评论'''
        if not request.user.is_authenticated:
            return JsonResponse({'status': 'fail', 'msg': '用户未登录'})

        course_id = request.POST.get('course_id',0)
        comment = request.POST.get('comment','')
        if course_id>0 and comment:
            course_comment = CourseComments()
            course = Course.objects.get(id=course_id)
            course_comment.course = course
            course_comment.comments = comment
            course_comment.user = request.user
            course_comment.save()
            return JsonResponse({'status': 'success', 'msg': '添加成功'})
        else:
            return JsonResponse({'status': 'fail', 'msg': '添加失败'})


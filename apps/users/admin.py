# 这个类专门来注册后台管理系统。
# 当使用UserProfile替换django自带的User后，需要在原admin上专门进行注册。
# 而xadmin则不需要。
# 因此在这里只演示admin的注册机制。

# from django.contrib import admin
# from .models import UserProfile
# 为UserProfile制定一个管理器，管理器类名的通用写法是 原类名+Admin
# class UserProfileAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(UserProfile, UserProfileAdmin)  # 将管理器注册


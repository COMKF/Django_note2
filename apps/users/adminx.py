# xadmin的注册机制和admin的机制一样。
# xadmin会搜索各个app下的adminx.py，读取其中的内容进行注册。

# 演示注册EmailVerifyRecord。
import xadmin
from .models import EmailVerifyRecord, Banner


# 为EmailVerifyRecord制定一个管理器，管理器类名的通用写法是 原类名+Admin
class EmailVerifyRecordAdmin(object):  # 注意，它继承的是object
    list_display = ['code', 'email', 'send_type', 'send_time']  # 自定义显示都内容，如果不写这行代码，会显示默认内容

    search_fields = ['code', 'email', 'send_type']  # 添加搜索功能，并添加需要搜索都字段。
    # 该搜索功能建议只添加Char类型的字段，而不要添加Date、Time等类型的字段。当然，这不是强制规定，懒的话可以不管这么多。

    list_filter = ['code', 'email', 'send_type', 'send_time']  # 添加过滤器功能


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)  # 将管理器注册


# 按照这种方法，注册其他model
class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(Banner, BannerAdmin)

# xadmin的其他设置，比如页面的主题，页面的页眉、页脚等也可以在这个py文件中进行设置。这些设置也需要注册，方法和model一样。
# 设置主题
from xadmin import views


class BaseSetting(object):  # 基本设置
    enable_themes = True  # 启用主题设置
    use_bootswatch = True  # 使用bootswatch主题


xadmin.site.register(views.BaseAdminView, BaseSetting)  # 将BaseSetting中的设置注册到BaseAdminView中


class GlobalSetting(object):    # 全局设置
    site_title = 'YMH个人网站'  # 设置页眉和 HTML 标题。
    site_footer = 'YMH版权所有'     # 设置页脚
    menu_style = 'accordion'    # 设置左侧侧边栏显示方式。


xadmin.site.register(views.CommAdminView, GlobalSetting)  # 将GlobalSetting中的设置注册到CommAdminView中

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.views.generic.base import View

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm
from  utils.email_send import send_register_email


# def login(request):  # 该方法名是login，与该方法内部的login方法重名懒，造成了循环调用，因此需要改方法名。
# 这也说明，我们写代码时，要避免方法名重名，否则很可能会造成BUG。
def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        # 使用Django自带的验证方法，对登录用户进行用户名密码的验证。注意：该方法使用的是关键字参数，即使用的参数名必须是username和password。
        user = authenticate(username=user_name, password=pass_word)  # 若验证成功则返回user，不成功则返回 None。
        if user is not None:
            # 验证成功后，使用Django自带的登录方法进行登录。如何使用呢？见index.html中。
            login(request, user)
            return render(request, "index.html", {})
        else:
            return render(request, "login.html", {'msg': '用户名或密码错误！'})
    else:
        return render(request, "login.html", {})


# Django默认使用 用户名密码 登录模式，如何更改，使其成为 邮箱密码 登录模式呢？
# 需要重写CustomBackend类，继承ModelBackend类，并重写authenticate方法。
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # 重写了authenticate方法后，就替换了上面user_login类调用的authenticate方法。这样我们就可以自定义自己的代码了。
        try:
            # 现在我们做一些修改，扩展登录功能，使其支持 邮箱密码 登录模式。在这里，需要引入Q（非常强大）。
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            # 这里要注意的是，我们不能直接用get(username=username,password=pass_word)验证。
            # 因为，从网页上传过来的数据是明文，而数据库中的password是密文，直接比对肯定是false。需要用check方法。
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 类写完了，方法也写完了，但是这样是不够的，还需要在setting文件中配置AUTHENTICATION_BACKENDS字段。


# 上面的功能都是基于方法来完成的，现在开始学习 基于类 来完成这些功能，基于类更方便。
# 首先要继承Django的View类。写完之后，如果要使用这个类，就需要修改urls中第二个变量为LoginView.as_view()。
class LoginView(View):
    # 重写get方法，如果页面传的方法是get的话，会调用该方法。
    def get(self, request):
        return render(request, "login.html", {})

    # 重写post方法，如果页面传的方法是post的话，会调用该方法。
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html", {})
                else:
                    return render(request, "login.html", {'msg': '用户未激活！'})
            else:
                return render(request, "login.html", {'msg': '用户名或密码错误！'})
        else:
            return render(request, "login.html", {'login_form': login_form})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get('email', '')
            if UserProfile.objects.filter(email=email):  # 对邮箱是否已注册进行判断
                return render(request, "register.html", {'register_form': register_form,'msg': '该邮箱已注册'})
            password = request.POST.get('password', '')
            user = UserProfile()
            user.username = email
            user.email = email
            user.is_active = False  # 设置用户为未激活状态，只有点击激活链接后才激活
            # 对密码进行加密，使其保存在数据库中是一个密文
            user.password = make_password(password)
            user.save()

            # 注册时需要验证邮箱，调用utils内的方法
            send_register_email(email, "register")
            return render(request, "login.html")
        else:
            return render(request, "register.html", {'register_form': register_form})


# 激活流程
class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:  # 如果没有该验证码，则需要返回验证失败的页面（这里不写了）
            return render(request, "active_fail.html")
        return render(request, "login.html")

# 忘记密码--略

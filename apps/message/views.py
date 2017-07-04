from django.shortcuts import render

from .models import UserMessage


def getform(request):
    # if request.method == 'POST': # 这个判断最好加上
    #     name = request.POST.get('name','')  # 获取从页面传来的数据。第二个参数是默认值，这里默认为空。

    # 取出所有数据
    # all_messages = UserMessage.objects.all()

    # 取出特定条件的数据，需要用filter方法，同时满足两个条件，只需要加 , 即可。
    # all_messages = UserMessage.objects.filter(name="YMH",address="河南")
    # for message in all_messages:
    #     print(message.name)

    # 删除数据
    # all_messages.delete()


    # 演示表单回显
    message = None  # 先把 message 定义为None，保证程序健壮性
    all_messages = UserMessage.objects.filter(name="YMH", address="河南")  # 过滤取数据
    if all_messages:  # 判定是否存在
        message = all_messages[0]
    return render(request, 'message.html', {'my_message': message})

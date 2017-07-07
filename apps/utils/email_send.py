__author__ = 'YMH'

from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from Django_from_mooc.settings import EMAIL_FROM


# 向邮箱发送验证码
def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()
    # 先把邮箱验证码保存到数据库中

    # 再写邮件内容，需要通过Django内部函数支持
    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = 'XX网激活链接'
        email_body = '请点击下面的链接进行激活：http://127.0.0.1/active/%s' % (code)
        # 因此我们需要一个处理激活链接的url，以后解决。
        # send_mail函数需要四个参数，第一个是标题，第二个是内容，第三个是发件人，第四个是邮件列表（必须是一个list）
        # 暂时略过吧，有问题
        # send_mail(email_title,email_body,EMAIL_FROM,[email])


# 验证邮箱需要邮箱验证码，这个验证码是一个随机字符串，可以自己写这个方法。
def random_str(randomlength=8):
    str = ''
    chars = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
    length = len(chars) - 1
    for i in range(randomlength):
        str += chars[Random().randint(0, length)]
    return str

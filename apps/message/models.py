from django.db import models


class UserMessage(models.Model):
    # Django提供了多种数据类型，不仅对应数据库中的类型，也有更多的高级类型。
    # 若不指定主键，Django会自动生成一个id字段，充当主键，当然，我们也可以自己定义主键，只需要在字段中加primary_key参数即可。
    object_id = models.CharField(max_length=50,default='',primary_key=True,verbose_name=u'主键')
    # CharField，文本类型，对应数据库中的char或varchar类型。它必须要指明max_length参数。
    name = models.CharField(max_length=20,verbose_name=u'用户名')
    # EmailField，高级类型。
    email = models.EmailField(verbose_name='邮箱')
    address = models.CharField(max_length=100,verbose_name=u'联系地址')
    message = models.CharField(max_length=500,verbose_name=u'留言信息')
    '''
    除此之外，还有 
    IntegerField，对应数据库的int类型。
    ForeignKey，对应数据库的外健。
    DateTimeField，对应数据库的日期时间。
    IPAddressField，高级类型，对应IP地址。
    FileField，高级类型，对应文件。
    ImageField，高级类型，对应图片。
    等类型，当然还有其他一些类型。
    
    在Django下，默认所有的字段是不为空的。添加null=True,blank=True,就可以设置该字段可以为空。
    同时加上default参数，可以设置默认值。
    '''

    # 该类定义表的属性
    class Meta:
        verbose_name = u'用户留言信息'  # 单数名称
        verbose_name_plural = verbose_name  # 复数名称

        # db_table，指定table名，如果不指定的话，会自动生成message_usermessage（即，APP_类名）
        # db_table = 'usermessage'
        # ordering，指定排序规则，'-object_id'为倒序排列。
        # ordering = '-object_id'
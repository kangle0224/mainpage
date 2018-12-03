from django.db import models

class UserInfo(models.Model):
    name = models.CharField(u'用户名', max_length=50)
    age = models.IntegerField(u'年龄')
    email = models.EmailField(u'邮箱')
    user_type_choice = (
        ('0', '校长'),
        ('1', '教师'),
        ('2', '学生'),
    )
    user_type = models.CharField(choices=user_type_choice, max_length=10, default=2) # 此处是字符字段，user_type_choice也必须是字符

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'userinfo'   # 自定义表名
        # verbose_name_plural = ""   # 复数名称

class Course(models.Model):
    name = models.CharField(u'课程名', max_length=50)
    price = models.CharField(u'价格', max_length=50)
    teacher = models.ForeignKey(UserInfo, on_delete=False)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'course_name'
        # verbose_name_plural = ""





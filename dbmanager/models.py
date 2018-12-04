from django.db import models

# -----school and student
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
        verbose_name_plural = ""   # 复数名称

class Course(models.Model):
    name = models.CharField(u'课程名', max_length=50)
    price = models.CharField(u'价格', max_length=50)
    teacher = models.ForeignKey(UserInfo, on_delete=False)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'course_name'
        # verbose_name_plural = ""

# -----school and student

# -----blog
class Author(models.Model):
    name = models.CharField(u'姓名', max_length=50)
    name_en = models.CharField(u"英文名", max_length=50)
    age = models.IntegerField(u'年龄')
    addr = models.CharField(u'地址', max_length=50)
    email = models.EmailField(u'邮箱')
    brief = models.TextField(u'简介', null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "作者信息"
        verbose_name_plural = "作者信息"

class Article(models.Model):
    title = models.CharField(u'标题', max_length=100, null=False, blank=False)
    content = models.TextField(u'内容', null=True, blank=True)
    index_page = models.ImageField(u'首页图片', upload_to='static/images', null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=True)
    price = models.IntegerField(u'价格')
    publish_date = models.DateTimeField('发布时间',auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = '博客文章'
        verbose_name_plural = "博客文章"


class Publisher(models.Model):
    name = models.CharField(u'出版商', max_length=50)
    addr = models.CharField(u'地址', max_length=50, null=False, blank=False, unique=True)
    article = models.ManyToManyField(Article, related_name='pa')
    brief = models.TextField(u'朝代简介')

    def __str__(self):
        return self.name

    class Meta:
        db_table = '出版商'
        verbose_name_plural = "出版商"

# -----blog



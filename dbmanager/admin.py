from django.contrib import admin
from dbmanager.models import UserInfo, Course, Article, Author, Publisher

admin.site.register(UserInfo)
admin.site.register(Course)
admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Publisher)
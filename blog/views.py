from django.shortcuts import render, HttpResponse
from dbmanager import models
def index(request):
    author_list = models.Author.objects.all().order_by('id')
    article_list = models.Article.objects.all().order_by('id')

    return render(request, 'blog/blog.html', {"author_list": author_list, "article_list": article_list})

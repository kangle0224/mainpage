from django.shortcuts import render, HttpResponse

def index(request):
    # return HttpResponse("welcome to blog index...")
    return render(request, 'blog.html')

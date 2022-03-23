from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    title = "Это главная страница проекта Yatube"
    context = { 'title': title }
    return render(request, template, context) 


# Страница со списком мороженого
def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = "Здесь будет информация о группах проекта Yatube"
    context = { 'title': title }
    return render(request, template, context)
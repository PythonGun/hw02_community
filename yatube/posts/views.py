from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    NUMBER_POSTS = 10
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:NUMBER_POSTS]
    context = {
        'title': 'Главная страница Ятаб',
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    NUMBER_POSTS = 10
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:NUMBER_POSTS]
    context = {
        'title': 'Посты группы',
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)

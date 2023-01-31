from django.shortcuts import render, get_object_or_404
from posts.models import Post, Group


def index(request):
    POSTS_ON_PAGE = 10

    posts = Post.objects.all()[:POSTS_ON_PAGE]
    context = {
        'posts': posts,
    }

    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    POSTS_ON_PAGE = 10

    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:POSTS_ON_PAGE]
    title = group.title
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }

    return render(request, 'posts/group_list.html', context)

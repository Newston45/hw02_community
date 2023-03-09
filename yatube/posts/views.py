from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from posts.models import Post, Group


def index(request):
    POSTS_ON_PAGE = 10

    posts = Post.objects.all()
    paginator = Paginator(posts, POSTS_ON_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }

    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    POSTS_ON_PAGE = 10

    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)
    title = group.title
    paginator = Paginator(posts, POSTS_ON_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
        'title': title,
    }

    return render(request, 'posts/group_list.html', context)

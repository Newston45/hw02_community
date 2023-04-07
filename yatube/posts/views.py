from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from posts.models import Post, Group, User


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


def profile(request, username):
    POSTS_ON_PAGE = 10

    author = get_object_or_404(User, username=username)
    post_list = Post.objects.filter(author=author)
    post_count = Post.objects.filter(author=author).count()
    paginator = Paginator(post_list, POSTS_ON_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'author': author,
        'post_list': post_list,
        'post_count': post_count,
        'page_number': page_number,
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    author = post.author
    post_count = Post.objects.filter(author=author).count()
    context = {
        'post': post,
        'post_count': post_count,
    }
    return render(request, 'posts/post_detail.html', context)

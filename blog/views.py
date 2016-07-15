from django.shortcuts import render, get_object_or_404
from .models import Post


def post_new(request):
	context = {}
	return render(request, 'blog/post_new.html', context)


def post_edit(request):
	context = {}
	return render(request, 'blog/post_edit.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)


def post_list(request):
    post_list = Post.objects.all()
    context = {
        'post_list': post_list,
    }
    return render(request, 'blog/post_list.html', context)

from django.shortcuts import render
from blog.models import Post

def main(request):

    post_list = Post.objects.all()
    context = {
        'post_list': post_list
    }
    return render(request, "main/home.html", context)
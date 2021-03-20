from django.views import generic
from django.shortcuts import render
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/posts.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

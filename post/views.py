from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'post/home.html', context)


class PostListView(ListView):

    model = Post
    template_name = 'post/home.html'
    content_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_context_data(self, *args, object_list=None, **kwargs):
        data = super(PostListView, self).get_context_data(*args, **kwargs)
        data['title'] = 'Home Page'
        return data


class PostDetailView(DetailView):

    model = Post


def about(request):

    return render(request, 'post/about.html')

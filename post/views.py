from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')


class PostListView(ListView):

    model = Post
    template_name = 'post/home.html'
    content_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 9

    def get_context_data(self, *args, object_list=None, **kwargs):
        data = super(PostListView, self).get_context_data(*args, **kwargs)
        data['title'] = 'Home Page'
        return data


class PostDetailView(DetailView):

    model = Post


def about(request):

    return render(request, 'post/about.html')

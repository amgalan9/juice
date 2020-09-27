from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='home-page'),
    path('about/', views.about, name='about-home'),
]
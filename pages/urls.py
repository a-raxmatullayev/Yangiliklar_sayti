from unicodedata import name
from django.urls import path
from .views import (
    HomePageView, 
    PostDetailView, 
    PostCreateView,
    PostDeleteView,
    PostUpdateView,
)

urlpatterns = [
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name = 'post_delete'),
    path('post/<int:pk>/edit', PostUpdateView.as_view(), name = 'post_edit'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
    path('post/new', PostCreateView.as_view(), name = 'post_new'),
    path('', HomePageView.as_view(), name = 'home',),
   ]

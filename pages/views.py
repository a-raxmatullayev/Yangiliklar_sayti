from dataclasses import fields
from pyexpat import model
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post-create.html'
    fields = ['Sarlavha', 'Muallif', 'Matn']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['Sarlavha', 'Matn']

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Post, Categoria
from .forms import PostForm

from django.contrib.auth.mixins import LoginRequiredMixin

#####################CREACION DE LOS POSTS###############################

class PostCreateView(LoginRequiredMixin, CreateView): #entra heredando el createView y carga el formulario de forms.py y lo manda a post_Create.html
    model = Post
    form_class = PostForm
    template_name = 'posts/post_create.html'
    success_url = reverse_lazy('home')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

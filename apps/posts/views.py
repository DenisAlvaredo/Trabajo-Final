from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views.generic.dates import MonthArchiveView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import PostForm, CommentForm



#####################CREACION DE LOS POSTS###############################

class PostCreateView(LoginRequiredMixin, CreateView): #entra heredando el createView y carga el formulario de forms.py y lo manda a post_Create.html
	model = Post
	form_class = PostForm
	template_name = 'posts/post_create.html'
	success_url = reverse_lazy('home')
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)


def CategoryView(request, cats):
	category_posts = Post.objects.filter(categoria=cats.replace('-', ' ')).order_by('-fecha_publicacion')
	return render(request, 'posts/categorias.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'posts/post_detail.html', {'post': post})


class PostUpdateView(UpdateView):
	form_class = PostForm
	model = Post
	template_name = 'posts/post_create.html'
	success_url = reverse_lazy('home')

class PostDeleteView(DeleteView):
	model = Post
	template_name = 'posts/post_confirm_delete.html'
	success_url = reverse_lazy('home')

class AddCommentView(CreateView):
	model = Comentarios
	form_class = CommentForm
	template_name = 'posts/add_comment.html'
	success_url = reverse_lazy('home')

	def form_valid(self,form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)

#------------------------------------------

class PostMonthArchiveView(MonthArchiveView):
	queryset = Post.objects.all()
	date_field = "pub_date"
	allow_future = True

#---------------------

class UpDateCommentView(UpdateView):
	form_class = CommentForm
	model = Comentarios
	template_name = 'posts/add_comment.html'
	success_url = reverse_lazy('home')

	def form_valid(self,form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)

#---------------------

class DelCommentView(DeleteView):
	model = Comentarios
	template_name = 'posts/comment_delete.html'
	success_url = reverse_lazy('home')

	def form_valid(self,form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)



from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render, redirect
from django.utils import timezone
from apps.posts.models import Post, Categoria

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	cats = Categoria.objects.all()
	ordering = ['-fecha_publicacion']
	#ordering2 = ['fecha_publicacion']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Categoria.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

#def Home(request):
#	posts = Post.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
#	return render(request, 'home.html', {'posts': posts})



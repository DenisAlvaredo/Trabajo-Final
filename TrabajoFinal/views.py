from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
from django.utils import timezone
from apps.posts.models import Post

#class Home(ListView):
#    model = Post
#    template_name = 'home.html'

def Home(request):
	posts = Post.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
	return render(request, 'home.html', {'posts': posts})

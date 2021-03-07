from apps.posts.models import Post
from django.views.generic import TemplateView, ListView

class Home(ListView):
    model = Post
    template_name = 'home.html'

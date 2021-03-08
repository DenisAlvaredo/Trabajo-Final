from django.urls import path
from . import views
from .views import *

app_name = 'posts'

urlpatterns = [
	path('subir_post/', PostCreateView.as_view(), name = 'post_create'),
	path('<int:pk>/', views.post_detail, name='post_detail'),
	path('<int:pk>/edit/', PostCreateView.as_view(), name='post_create'),
]

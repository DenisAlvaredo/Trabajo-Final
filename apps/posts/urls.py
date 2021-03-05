from django.urls import path
from . import views
from .views import *

app_name= "posts"

urlpatterns = [
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
]
from django.urls import path
from . import views
from .views import *

app_name = 'posts'

urlpatterns = [
	path('subir_post/', PostCreateView.as_view(), name = 'post_create'),
	path('<int:pk>/', views.post_detail, name='post_detail'),
	path('category/<str:cats>', views.CategoryView, name = 'category'),
	#path('<int:pk>/edit/', PostCreateView.as_view(), name='post_create'),
	path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
	path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
	path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
	path('article/<int:pk>/del_comment/', DelCommentView.as_view(), name='del_comment'),

	path('<int:year>/<str:month>/',
   PostMonthArchiveView.as_view(),
   name="archive_month"),
]

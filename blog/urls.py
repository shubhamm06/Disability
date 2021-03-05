from django.urls import path
from .views import PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, search
from .models import Post
from . import views

urlpatterns = [
    path('blogs/<int:pg>/', 		            views.home, 				name='blog-home'),
    path('blogs/<int:pg>/search', 		        views.search, 				name='search'),
    path('blogs/<int:pk>/detail/',              PostDetailView, 	        name='post-detail'),
    path('blogs/write/' , 			            PostCreateView, 			name='post-create'),
    path('blogs/<int:pk>/update/', 	            PostUpdateView, 			name='post-update'),
    path('blogs/<int:pk>/delete/', 	            PostDeleteView.as_view(), 	name='post-delete'),
    path('blogs/bizfanatics/',                  views.magazine,	            name='magazine'),
]
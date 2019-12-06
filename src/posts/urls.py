from django.urls import path
from users import views as user_views
from posts.views import (
    index,
    PostsListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView )

urlpatterns = [
   path('', user_views.ProfileView.as_view(), name='index'),
   path('profile/<int:pk>/update/', user_views.ProfileUpdateView.as_view(), name='profile-update'),
   path('post/new/', PostCreateView.as_view(), name='post-create'),
   path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
   path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
   path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
   path('posts/<category>/', PostsListView.as_view(), name='posts-list'),
]


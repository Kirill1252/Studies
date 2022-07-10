from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import *

app_name = 'blog'

urlpatterns = [
    path('', HomePost.as_view(), name='index'),
    path('create_post/', CreatePost.as_view(), name='create_post'),
    # path('create_post/', create_post, name='create_post'),
    path('create_user/', RegisterUser.as_view(), name='create_user'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('blog:login')), name='logout'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post'),
    path('user_details/<int:pk>/', UserDetailView.as_view(), name='user_details'),
    path('post_delete/<int:pk>/', DeletePost.as_view(), name='post_delete'),
    path('update_post/<int:pk>/', UpdatePost.as_view(), name='update_post'),

]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('videoplayer', views.videoplayer, name='videoplayer'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('channel', views.channel, name='channel'),
    path('favoritecreators', views.favoritecreators, name='favoritecreators'),
    path('recentvideos', views.recentvideos, name='recentvideos'),
]
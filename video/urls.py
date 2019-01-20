from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('frame/', views.frame, name='frame'),
    path('video_player', views.videoplayer, name='video_player'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('channel', views.channel, name='channel'),
    path('favoritecreators', views.favoritecreators, name='favoritecreators'),
    path('recentvideos', views.recentvideos, name='recentvideos'),
]
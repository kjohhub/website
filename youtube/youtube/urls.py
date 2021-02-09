from django.urls import path
from youtube import views
from django.contrib.auth import views as auth_views
from . import views

app_name = 'youtube'
urlpatterns = [
    path('', views.index, name='index'),      				# /youtube/
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('results', views.results, name='results'),
    path('playlist', views.playlist, name='playlist'),
    path('playlist/add', views.playlist_add, name='playlist_add'),
    path('history', views.history, name='history'),
    path('signup/', views.signup, name='signup'),
    path('profile/delete/', views.profile_delete_view, name='profile_delete'),
    path('manage_video/', views.manage_video, name='manage_video'),
]

from django.urls import path
from youtube import views
from django.contrib.auth import views as auth_views
from . import views

app_name = 'youtube'
urlpatterns = [
    path('', views.index, name='index'),      				# /youtube/
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('results/', views.results, name='results'),
    path('playlist/<int:id>/', views.playlist, name='playlist'),
    path('playlist/insert/', views.playlist_insert, name='playlist_insert'),
    path('playlist/rename/', views.playlist_rename, name='playlist_rename'),
    path('playlist/delete/', views.playlist_delete, name='playlist_delete'),
    path('playlist/insert_video/', views.playlist_insert_video, name='playlist_insert_video'),
    path('playlist/delete_video/', views.playlist_delete_video, name='playlist_delete_video'),
    path('history/', views.history, name='history'),
    path('history/insert_video/', views.history_insert_video, name='history_insert_video'),
    path('history/delete_video/', views.history_delete_video, name='history_delete_video'),
    path('signup/', views.signup, name='signup'),
    path('profile/delete/', views.profile_delete_view, name='profile_delete'),
    path('manage_video/', views.manage_video, name='manage_video'),
]

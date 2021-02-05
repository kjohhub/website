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
    path('signup/', views.signup, name='signup'),
]

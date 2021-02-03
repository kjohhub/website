from django.urls import path
from youtube import views


app_name = 'youtube'
urlpatterns = [
    path('', views.index, name='index'),      				# /youtube/
   
    
   
]

from django.shortcuts import render
from youtube.models import memberTbl, videoTbl, playlistTbl, historyTbl


# index
def index(request):
    video_list = videoTbl.objects.all()
    context = {'video_list' : video_list }
    return render(request, 'youtube/index.html', context)

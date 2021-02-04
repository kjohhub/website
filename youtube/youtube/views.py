from django.shortcuts import render
from youtube.models import memberTbl, videoTbl, playlistTbl, historyTbl


# index
def index(request):
    return render(request, 'youtube/index.html', {})

def results(request):
    search_key = request.GET.get('search_key')
    if search_key:
        video_list = videoTbl.objects.all()
        video_list = video_list.filter(title__icontains=search_key)
    return render(request, 'youtube/index.html', {'video_list':video_list})

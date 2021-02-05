from django.shortcuts import render, redirect 		#210205 redirect부분 추가
from youtube.models import memberTbl, videoTbl, playlistTbl, historyTbl
from django.contrib.auth import authenticate, login		#210205추가
from youtube.forms import UserForm		#210205추가

# index
def index(request):
    return render(request, 'youtube/index.html', {})

def results(request):
    search_key = request.GET.get('search_key')
    if search_key:
        video_list = videoTbl.objects.all()
        video_list = video_list.filter(title__icontains=search_key)
    return render(request, 'youtube/index.html', {'video_list':video_list})

#210205추가 회원가입페이지
def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user) #자동로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'youtube/signup.html', {'form': form})
from django.shortcuts import render, redirect, get_object_or_404 		#210205 redirect부분 추가
from youtube.models import videoTbl, playlistTbl, playlistItemTbl, historyTbl
from django.contrib.auth import authenticate, login		#210205추가
from youtube.forms import UserForm		#210205추가
from .forms import CheckPasswordForm	#210208추가
from youtube.decorators import *	#210208추가
from django.db.models import Subquery

# index
def index(request):
    context = {}
    if request.user.is_authenticated:
        play_list = playlistTbl.objects.filter(userid=request.user.id)
        context['play_list'] = play_list
    return render(request, 'youtube/index.html', context)

def results(request):
    context = {}
    if request.user.is_authenticated:
        context['play_list'] = playlistTbl.objects.filter(userid=request.user.id)
    search_key = request.GET.get('search_key')
    if search_key:
        context['video_list'] = videoTbl.objects.filter(title__icontains=search_key)
    return render(request, 'youtube/index.html', context)

def playlist(request):
    context = {}
    if request.user.is_authenticated:
        context['play_list'] = playlistTbl.objects.filter(userid=request.user.id)
        video_list = videoTbl.objects.all()
        context['video_list'] = video_list
    return render(request, 'youtube/index.html', context)

def history(request):
    context = {}
    if request.user.is_authenticated:
        
        context['play_list'] = playlistTbl.objects.filter(userid=request.user.id)
        histo_list = historyTbl.objects.filter(userid=request.user.id)
        video_list = videoTbl.objects.filter(id__in=Subquery(histo_list.values('videoid')))
        context['video_list'] = video_list
    return render(request, 'youtube/index.html', context)


def playlist_add(request):
    context = {}
    if request.method == "POST":
        if request.user.is_authenticated:
            list_name = request.POST.get('name')        
            plist = playlistTbl(list_name=list_name, userid = request.user)
            plist.save()
            context['play_list'] = playlistTbl.objects.filter(userid=request.user.id)

    return render(request, 'youtube/index.html', context)


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

#210208 회원탈퇴
@login_message_required
def profile_delete_view(request):
    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)
        
        if password_form.is_valid():
            request.user.delete()
            return redirect('/youtube/login/')
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'youtube/profile_delete.html', {'password_form':password_form})
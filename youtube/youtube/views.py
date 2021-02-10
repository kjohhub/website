from django.shortcuts import render, redirect, get_object_or_404 		#210205 redirect부분 추가
from youtube.models import videoTbl, playlistTbl, playlistItemTbl, historyTbl
from django.contrib.auth import authenticate, login		#210205추가
from youtube.forms import UserForm		#210205추가
from .forms import CheckPasswordForm	#210208추가
from youtube.decorators import *	#210208추가
from django.db.models import Subquery
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# index
def empty():
    return

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
    if request.method == "POST":
        list_id = request.POST.get('listid')
        print(list_id)
        context['play_list'] = playlistTbl.objects.filter(userid=request.user.id)
        play_item = playlistItemTbl.objects.filter(listid=list_id)
        video_list = videoTbl.objects.filter(videoid__in=Subquery(play_item.values('videoid')))
        context['video_list'] = video_list
    return render(request, 'youtube/index.html', context)

def playlist_insert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        user = request.user
        playlist = playlistTbl(userid=user, list_name=name)
        playlist.save()
    return redirect('/')

def playlist_rename(request):
    pass

def playlist_delete(request):
    pass

@csrf_exempt
def playlist_insert_video(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            listid = request.POST.get('listid')
            videoid = request.POST.get('videoid')
            item = playlistItemTbl(listid_id=listid, videoid_id=videoid)
            item.save()
            return HttpResponse(status=200)
    return HttpResponse(status=201)

def playlist_delete_video(request):
    pass

def history(request):
    context = {}
    if request.user.is_authenticated:
        context['play_list'] = playlistTbl.objects.filter(userid=request.user.id)
        histo_list = historyTbl.objects.filter(userid=request.user.id)
        video_list = videoTbl.objects.filter(videoid__in=Subquery(histo_list.values('videoid')))
        context['video_list'] = video_list
    return render(request, 'youtube/index.html', context)

@csrf_exempt
def history_insert_video(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = request.user
            videoid = request.POST.get('videoid')
            history = historyTbl(userid=user, videoid_id=videoid)
            history.save()
            return HttpResponse(status=200)
    return HttpResponse(status=201)

def history_delete_video(request):
    pass

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

#210209 동영상 관리자창으로 이동
def manage_video(request):
    context = {}
    if request.user.is_authenticated:
        video_list = videoTbl.objects.all()
    return render(request, 'youtube/manage_video.html', context)

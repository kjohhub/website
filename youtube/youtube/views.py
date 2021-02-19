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
def index(request):
    context = {}
    if request.user.is_authenticated:
        play_list = playlistTbl.objects.filter(userid=request.user.id)
        context['play_list'] = play_list
    return render(request, 'youtube/index.html', context)

def results(request):
    context = {}
    search_key = request.GET.get('search_key')
    if request.user.is_authenticated:
        context['play_list'] = playlistTbl.objects.filter(userid=request.user.id)
    if search_key:
        context['list_type'] = 'search'
        context['video_list'] = videoTbl.objects.filter(title__icontains=search_key)
    return render(request, 'youtube/index.html', context)

def playlist(request, id):
    context = {}
    if request.user.is_authenticated:
        curr_list = playlistTbl.objects.get(pk=id)
        play_item = playlistItemTbl.objects.filter(listid=id)
        video_list = videoTbl.objects.filter(videoid__in=Subquery(play_item.values('videoid')))
        context['list_type'] = 'playlist'
        context['play_list'] = playlistTbl.objects.filter(userid=request.user.id)
        context['curr_list'] = curr_list
        context['video_list'] = video_list
    return render(request, 'youtube/index.html', context)

def playlist_insert(request):
    if request.user.is_authenticated:
        name = request.POST.get('name')
        playlist = playlistTbl(userid=request.user, list_name=name)
        playlist.save()
    return redirect('/')

def playlist_rename(request):
    if request.user.is_authenticated:
        id = request.POST.get('listid')
        name = request.POST.get('name')
        playlist = playlistTbl.objects.get(pk=id)
        playlist.list_name = name
        playlist.save()
    return redirect('/')

def playlist_delete(request):
    if request.user.is_authenticated:
        id = request.POST.get('listid')
        playlist = playlistTbl(pk=id)
        playlist.delete()
    return redirect('/')

@csrf_exempt
def playlist_insert_video(request):
    if request.user.is_authenticated:
        listid = request.POST.get('listid')
        videoid = request.POST.get('videoid')
        item = playlistItemTbl(listid_id=listid, videoid_id=videoid)
        item.save()
        return HttpResponse(status=200)
    return HttpResponse(status=400)

@csrf_exempt
def playlist_delete_video(request):
    if request.user.is_authenticated:
        listid = request.POST.get('listid')
        videoid = request.POST.get('videoid')
        item = playlistItemTbl.objects.get(listid_id=listid, videoid_id=videoid)
        item.delete()
        return HttpResponse(status=200)
    return HttpResponse(status=400)

def history(request):
    context = {}
    if request.user.is_authenticated:
        context['play_list'] = playlistTbl.objects.filter(userid=request.user.id)
        context['list_type'] = 'history'
        histo_list = historyTbl.objects.filter(userid=request.user.id)
        video_list = videoTbl.objects.filter(videoid__in=Subquery(histo_list.values('videoid')))
        context['video_list'] = video_list
    return render(request, 'youtube/index.html', context)

@csrf_exempt
def history_insert_video(request):
    if request.user.is_authenticated:
        videoid = request.POST.get('videoid')
        history = historyTbl(userid=request.user, videoid_id=videoid)
        history.save()
        return HttpResponse(status=200)
    return HttpResponse(status=400)

@csrf_exempt
def history_delete_video(request):
    if request.user.is_authenticated:
        videoid = request.POST.get('videoid')
        history = historyTbl.objects.get(userid=request.user, videoid_id=videoid)
        history.delete()
        return HttpResponse(status=200)
    return HttpResponse(status=400)

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
            return redirect('login')
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
    if request.user.is_superuser:
        video_list = videoTbl.objects.all()
        return render(request, 'youtube/manage_video.html', context)
    return redirect('/admin/')

@csrf_exempt
def video_form(request):
    context = {}
    if request.method == "POST":
        form = videoTblForm(request.POST)
        if form.is_valid():
            obj = videoTbl(title = form.data['title'], videoid = form.data['videoid'],  video_url = "https://www.youtube.com/watch?v=" + form.data['videoid'], image_url =  "https://i.ytimg.com/vi/" + form.data['videoid'] + "/hqdefault.jpg")
            obj.save()
            return render(request, 'youtube/manage_video.html', context)
        return HttpResponse('fail')
    elif request.method == 'GET':
        form = PersonForm()
        return render(request, 'dj/form.html', {'form': form})
    else:
        pass

@csrf_exempt
def manage_video_insert(request):
    if request.method == "POST":
        videoid = request.POST.get('videoid')
        title = request.POST.get('title')
        video_url = "https://www.youtube.com/watch?v=" + videoid
        image_url =  "https://i.ytimg.com/vi/" + videoid + "/hqdefault.jpg"
        video = videoTbl(videoid = videoid, title = title, video_url = video_url, image_url=image_url)
        video.save()
        return HttpResponse(status=200)
    return HttpResponse(status=400)



from django.shortcuts import render



# index
def index(request):
    context = {}
    return render(request, 'youtube/index.html', context)
    
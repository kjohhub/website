from django.contrib import admin
from youtube.models import memberTbl, videoTbl, playlistTbl, historyTbl

admin.site.register(memberTbl)
admin.site.register(videoTbl)
admin.site.register(playlistTbl)
admin.site.register(historyTbl)
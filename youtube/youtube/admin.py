from django.contrib import admin
from youtube.models import videoTbl, playlistTbl, playlistItemTbl, historyTbl

admin.site.register(videoTbl)
admin.site.register(playlistTbl)
admin.site.register(playlistItemTbl)
admin.site.register(historyTbl)
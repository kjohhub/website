from django.contrib import admin
from youtube.models import videoTbl, listlistTbl, playlistTbl, historyTbl

admin.site.register(videoTbl)
admin.site.register(listlistTbl)
admin.site.register(playlistTbl)
admin.site.register(historyTbl)
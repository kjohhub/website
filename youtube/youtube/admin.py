from django.contrib import admin
from youtube.models import videoTbl, playlistTbl, playlistItemTbl, historyTbl

@admin.register(videoTbl)
class videoTblAdmin(admin.ModelAdmin):
    list_display = ['videoid','title']

admin.site.register(playlistTbl)
admin.site.register(playlistItemTbl)
admin.site.register(historyTbl)
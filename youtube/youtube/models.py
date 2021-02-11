from django.db import models
from django.contrib.auth.models import User  


# 동영상 테이블
class videoTbl(models.Model):
    videoid = models.CharField(max_length=16, primary_key=True)
    title = models.CharField(max_length=64)
    video_url = models.CharField(max_length=64)
    image_url = models.CharField(max_length=64)
    upload_time = models.CharField(max_length=13)

    def __str__(self):
        return self.videoid

# 재생 목록 테이블
class playlistTbl(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    list_name = models.CharField(max_length=16, default='재생목록')

    def __str__(self):
        return str(self.id)
   

# 재생 목록 아이템 테이블
class playlistItemTbl(models.Model):
    class Meta:
        unique_together = (('listid', 'videoid'),)

    listid = models.ForeignKey(playlistTbl, on_delete=models.CASCADE)
    videoid = models.ForeignKey(videoTbl, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


# 시청 기록 테이블
class historyTbl(models.Model):
    class Meta:
        unique_together = (('userid', 'videoid'),)

    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    videoid = models.ForeignKey(videoTbl, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
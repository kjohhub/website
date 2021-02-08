from django.db import models
from django.contrib.auth.models import User  


# 동영상 테이블
class videoTbl(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    title = models.CharField(max_length=64)
    video_url = models.CharField(max_length=64)
    image_url = models.CharField(max_length=64)
    upload_time = models.CharField(max_length=13)

    def __str__(self):
        return self.id

# 재생 목록의 리스트 테이블
class listlistTbl(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    listName = models.CharField(max_length=16)

    def __str__(self):
        return self.listName
   

# 재생 목록 테이블
class playlistTbl(models.Model):
    listid = models.ForeignKey(listlistTbl, on_delete=models.CASCADE)
    videoid = models.ForeignKey(videoTbl, on_delete=models.CASCADE)

    def __str__(self):
        return ""


# 시청 기록 테이블
class historyTbl(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    videoid = models.ForeignKey(videoTbl, on_delete=models.CASCADE)

    def __str__(self):
        return ""
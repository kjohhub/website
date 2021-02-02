from django.db import models



# 회원 테이블
class memberTbl(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    password = models.CharField(max_length=16)
    name = models.CharField(max_length=16)
    birthdate = models.DateTimeField('date published')
    mobile = models.CharField(max_length=13)
    address = models.CharField(max_length=32)

    def __str__(self):
        return self.id


# 동영상 테이블
class videoTbl(models.Model):
    ID = models.CharField(max_length=16, primary_key=True)
    title = models.CharField(max_length=64)
    video_url = models.CharField(max_length=64)
    image_url = models.CharField(max_length=64)
    upload_time = models.CharField(max_length=13)

    def __str__(self):
        return self.ID

   

# 재생 목록 테이블
class playlistTbl(models.Model):
    userid = models.ForeignKey(memberTbl, on_delete=models.CASCADE)
    videoid = models.ForeignKey(videoTbl, on_delete=models.CASCADE)

    def __str__(self):
        return ""


# 시청 기록 테이블
class historyTbl(models.Model):
    userid = models.ForeignKey(memberTbl, on_delete=models.CASCADE)
    videoid = models.ForeignKey(videoTbl, on_delete=models.CASCADE)

    def __str__(self):
        return ""
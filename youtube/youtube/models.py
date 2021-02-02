from django.db import models



# 회원 테이블
class memberTbl(models.Model):
    pass


# 동영상 테이블
class videoTbl(models.Model):
    pass


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
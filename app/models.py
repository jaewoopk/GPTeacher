from django.db import models

# Create your models here.

class User(models.Model) :
    id = models.CharField(primary_key=True, max_length=50)  # 유저 ID
    password = models.CharField(max_length=20)              # 유저 비밀번호

class SentenceData(models.Model) :
    sentenceNum = models.IntegerField(primary_key=True)     # 문장 번호
    contents = models.CharField(max_length=200)             # 문장 내용
    level = models.IntegerField()                           # 문장 레벨
    hint = models.CharField(max_length=100)                 # 문장 힌트
    blankWord = models.CharField(max_length=50)             # 빈칸 단어
    blankPos = models.IntegerField()                        # 빈칸 위치
    ansKor = models.CharField(max_length=400)               # 정답 한글 문장
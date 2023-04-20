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

class UserStudyInfo(models.Model) :
    id = models.CharField(foreign_key=True, max_length=50)  # 유저 ID
    sentenceNum = models.IntegerField(foreign_key = True)   # 문장 번호
    wrongNum = models.IntegerField()                        # 틀린 횟수
    check = models.IntegerField()                           # 오답 횟수

class UserGameInfo(models.Model) :
    id = models.CharField(foreign_key=True, max_length=50)  # 유저 ID
    sentenceNum = models.IntegerField(foreign_key = True)   # 문장 번호
    score = models.IntegerField()                           # 게임 점수

class Ranking(models.Model) :
    id = models.CharField(foreign_key=True, max_length=50)  # 유저 ID
    userList = models.CharField(max_length=200)             # 유저 리스트
    maxScore = models.IntegerField()                        # 게임 최고 점수
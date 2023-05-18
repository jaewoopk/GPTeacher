from django.db import models

# Create your models here.

# class User(models.Model) :
#     id = models.CharField(primary_key=True, max_length=50)  # 유저 ID
#     password = models.CharField(max_length=20)              # 유저 비밀번호

# class SentenceData(models.Model) :
#     sentenceNum = models.IntegerField(primary_key=True)     # 문장 번호
#     contents = models.CharField(max_length=200)             # 문장 내용
#     level = models.IntegerField()                           # 문장 레벨
#     hint = models.CharField(max_length=100)                 # 문장 힌트
#     blankWord = models.CharField(max_length=50)             # 빈칸 단어
#     blankPos = models.IntegerField()                        # 빈칸 위치
#     ansKor = models.CharField(max_length=400)               # 정답 한글 문장

# class UserStudyInfo(models.Model) :
#     id = models.CharField(foreign_key=True, max_length=50)  # 유저 ID
#     sentenceNum = models.IntegerField(foreign_key = True)   # 문장 번호
#     wrongNum = models.IntegerField()                        # 틀린 횟수
#     check = models.IntegerField()                           # 오답 횟수

# class UserGameInfo(models.Model) :
#     id = models.CharField(foreign_key=True, max_length=50)  # 유저 ID
#     sentenceNum = models.IntegerField(foreign_key = True)   # 문장 번호
#     score = models.IntegerField()                           # 게임 점수

# class Ranking(models.Model) :
#     id = models.CharField(foreign_key=True, max_length=50)  # 유저 ID
#     userList = models.CharField(max_length=200)             # 유저 리스트
#     maxScore = models.IntegerField()                        # 게임 최고 점수

#-------------------------------- test -----------------------------------
class User(models.Model) :
    userid = models.CharField(max_length=50, verbose_name='유저ID', unique=True)                # 유저 ID
    password = models.CharField(max_length=100, verbose_name='비밀번호')        # 유저 비밀번호
    user_idx = models.IntegerField(default=1, verbose_name='유저학습문장번호')
    class Meta:
        db_table = 'test_user'

# -------------------------> mysql에서 뽑아온 문장 DB-----------------------------

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Sentencedata(models.Model):
    idsentencedata = models.IntegerField(db_column='idsentenceData', primary_key=True)  # Field name made lowercase.
    sentencedata_contents = models.CharField(db_column='sentenceData_contents', max_length=200)  # Field name made lowercase.
    sentencedata_word1 = models.CharField(db_column='sentenceData_word1', max_length=45)  # Field name made lowercase.
    sentencedata_word2 = models.CharField(db_column='sentenceData_word2', max_length=45)  # Field name made lowercase.
    sentencedata_word3 = models.CharField(db_column='sentenceData_word3', max_length=45)  # Field name made lowercase.
    sentencedata_word4 = models.CharField(db_column='sentenceData_word4', max_length=45)  # Field name made lowercase.
    sentencedata_answerword = models.CharField(db_column='sentenceData_answerword', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sentenceData'
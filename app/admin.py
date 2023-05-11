from django.contrib import admin

# Register your models here.

### admin id : admin
### admin password : 세종대학교


from .models import User
from .models import Sentencedata

class userAdmin(admin.ModelAdmin) :
    list_display = ('userid', 'password')

class sentenceAdmin(admin.ModelAdmin) :
    list_display = ('idsentencedata', 'sentencedata_contents', 'sentencedata_word1', 'sentencedata_word2', 'sentencedata_word3', 'sentencedata_word4', 'sentencedata_answerword')

admin.site.register(User, userAdmin)
admin.site.register(Sentencedata)
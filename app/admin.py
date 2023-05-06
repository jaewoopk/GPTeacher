from django.contrib import admin

# Register your models here.


### admin id : admin
### admin password : 세종대학교


from .models import User

class userAdmin(admin.ModelAdmin) :
    list_display = ('userid', 'password')

admin.site.register(User, userAdmin)
from django.urls import path
from django.shortcuts import redirect
from .views import RegisterView, LoginView, index, join, login, mypage, rank, study

from . import views

app_name = 'apps'

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('index/', index.as_view()),

    path('english/', lambda r: redirect('apps:join')),
    path('english/join/', join.as_view(), name= 'join'),
    path('english/login/', login.as_view(), name= 'login'),
    path('english/mypage/', mypage.as_view(), name= 'mypage'),
    path('english/rank/', rank.as_view(), name= 'rank'),
    path('english/study/', study.as_view(), name= 'study'),
]
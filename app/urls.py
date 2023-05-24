from django.urls import path
from django.shortcuts import redirect
from .views import RegisterView, LoginView, index, join, login, mypage, rank, study, jointest, main, logout

from . import views

app_name = 'apps'

urlpatterns = [
    #path('register/', RegisterView.as_view()),
    #path('login/', LoginView.as_view()),
    #path('index/', index.as_view()),

    path('english/', lambda r: redirect('apps:login')),
    #path('english/join/', join.as_view(), name= 'join'),
    #path('english/login/', login.as_view(), name= 'login'),
    #path('english/mypage/', mypage.as_view(), name= 'mypage'),
    #path('english/rank/', rank.as_view(), name= 'rank'),
    #path('english/study/', study.as_view(), name= 'study'),
    path('english/jointtest/', jointest.as_view(), name= 'test'),

    path('english/join/', views.join),
    path('english/login/', views.login, name= 'login'),

    path('english/main/', views.main, name= 'main'),
    path('english/study/', views.study, name= 'study'),
    path('english/rank/', views.rank, name= 'rank'),
    path('english/mypage/', views.mypage, name= 'mypage'),

    path('english/logout/', views.logout, name= 'out'),
    path('english/exam/', views.exam, name= 'exam'),
    #path('english/book/', views.logout, mark = 'book'),
]
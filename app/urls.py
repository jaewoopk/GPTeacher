from django.urls import path
from .views import RegisterView, LoginView, menu_index

from . import views

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    #path('index/', views.index, name='index'),
    path('index/', menu_index.as_view()),
]
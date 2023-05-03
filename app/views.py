from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegisterSerializer, LoginSerializer

from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import View
from django.shortcuts import render

class RegisterView(generics.CreateAPIView) : # CreateAPIView(generics) 사용 구현
    queryset = User.objects.all()
    serializer_class = RegisterSerializer # 회원가입 기능

class LoginView(generics.GenericAPIView) : # 특별한 제너릭을 사용하지 않고 기본 GenericAPIView를 사용하여 구현
    serializer_class = LoginSerializer
    
    def post(self, request) :
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        token = serializer.validated_data # validate()의 리턴 값인 Token을 받아온다.
        return Response({"token" : token.key}, status=status.HTTP_200_OK)

'''
def index(request):
    return HttpResponse("Hello World!!!")
'''
class index(TemplateView):
    template_name = 'index.html'

class join(TemplateView):
    template_name = 'app\english\join.html'

class login(TemplateView):
    template_name = 'app\english\login.html'
    
class mypage(TemplateView):
    template_name = 'app\english\mypage.html'

class rank(TemplateView):
    template_name = 'app\english\\rank.html'

class study(TemplateView):
    template_name = 'app\english\study.html'

class jointest(View):
    template_name = 'app\english\jointtest.html'
    
    def post(self, request, *args, **kwargs):
        result = {
            'insertid' : request.POST['email'],
            'insertpassword' : request.POST['password'],
        }
        print(request.POST['email'])
        print(request.POST['password'])
        return render(request, self.template_name, context=result)
        



# # --> FBV : Function Based View = 함수 기반 뷰
# @api_view(['GET']) # Decorator -> 함수를 꾸미는 역할(함수에 대한 성격을 표시해주는 표기법)
# def HelloAPI(request) :
#     return Response("hello world!")

# # --> CBV : Class Based View = 클래스 기반 뷰
# # class HelloAPI(APIView) :
# #     def get(self, request) :
# #         return Response("hello wolrd")
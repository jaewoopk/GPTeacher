from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegisterSerializer, LoginSerializer

from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User as appUser
from .models import Sentencedata

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
    template_name = 'app/english/join.html'
'''
class login(TemplateView):
    template_name = 'app\english\login.html'
'''
'''
class mypage(TemplateView):
    template_name = 'app\english\mypage.html'
'''
'''
class rank(TemplateView):
    template_name = 'app\english\\rank.html'
'''
'''
class study(TemplateView):
    template_name = 'app\english\study.html'
'''
class jointest(View):
    template_name = 'app/english/jointtest.html'
    
    def post(self, request, *args, **kwargs):
        result = {
            'insertid' : request.POST['email'],
            'insertpassword' : request.POST['password'],
        }
        print(request.POST['email'])
        print(request.POST['password'])
        return render(request, self.template_name, context=result)
        
def register(request):
    if request.method == 'GET' :
        return render(request, 'app/english/jointtest.html')

    elif request.method == 'POST' :
        username = request.POST.get('email', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('password', None)
        print(request.POST['email'])
        print(request.POST['password'])

        res_data = {}
        
        if not (username and password and re_password) :
            res_data['error'] = '전부 입력해야 합니다'
            print("error1")
        elif password != re_password :
            res_data['error'] = '비밀번호가 다릅니다'
            print("error2")
        else :
            print("error999")
            entry = appUser.objects.filter(userid=username)
            if entry.exists():
                res_data['error'] = '아이디 중복'
                print("errorwndqhr")
                return render(request, 'app/english/join.html', res_data)
            else :
                user = appUser(userid=username, password=make_password(password))
                user.save()
        return render(request, 'app/english/join.html', res_data)

        
def login(request) :
    response_data = {}

    if request.method == 'GET' :
        return render(request, 'app/english/login.html')

    elif request.method == 'POST' :
        log_username = request.POST.get('email', None)
        log_password = request.POST.get('password', None)

        if not (log_username and log_password) :
            response_data['error'] = '전부 입력해야 합니다'
            print("error1")
        else :
            entry = appUser.objects.filter(userid=log_username)
            if entry.exists() :
                dbuser = appUser.objects.get(userid=log_username)
                if check_password(log_password, dbuser.password):
                    request.session['user'] = dbuser.id
                    request.session.get_expire_at_browser_close()
                    return redirect('apps:study')
                else :
                    response_data['error'] = '비밀번호 오류'
                

        return render(request, 'app/english/login.html', response_data)

def logout(request) :
    request.session.pop('user')
    return redirect('apps:login')

def home(request) :
    user_id = request.session.get('user')
    if user_id :
        dbuser = appUser.objects.get(pk=user_id)
        return HttpResponse(dbuser.userid)
    return HttpResponse('로그인 필요')


def study(request) :
    if request.method == 'GET' :
        if 'user' in request.session:
            print("aaaa")
            return render(request, 'app/english/study.html')
        else :
            datas11 = Sentencedata.objects.all().order_by('idsentencedata')[:1]
            context = {'Sentencedata': datas11}
            return render(request, 'app/english/study.html', context)
            return redirect('apps:login')

def rank(request) :
    if request.method == 'GET' :
        if 'user' in request.session:
            print("ank")
            return render(request, 'app/english/rank.html')
        else :
            return redirect('apps:login')

def mypage(request) :
    if request.method == 'GET' :
        if request.session.get('user') != None :
            print("page", request.session.get('user'))
            return render(request, 'app/english/mypage.html')
        else :
            print("page2", request.session.get('user'))
            return redirect('apps:login')

# # --> FBV : Function Based View = 함수 기반 뷰
# @api_view(['GET']) # Decorator -> 함수를 꾸미는 역할(함수에 대한 성격을 표시해주는 표기법)
# def HelloAPI(request) :
#     return Response("hello world!")

# # --> CBV : Class Based View = 클래스 기반 뷰
# # class HelloAPI(APIView) :
# #     def get(self, request) :
# #         return Response("hello wolrd")
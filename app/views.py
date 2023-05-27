from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
import openai
from .serializers import RegisterSerializer, LoginSerializer

from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import TemplateView
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User as appUser
from .models import Sentencedata
from django.views.decorators.csrf import csrf_exempt
import json
import random

OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY

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
class join(TemplateView):
    template_name = 'app/english/join.html'
'''
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
        
def join(request):
    if request.method == 'GET' :
        return render(request, 'app/english/join.html')

    elif request.method == 'POST' :
        username = request.POST.get('email', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('password', None)
        print(request.POST['email'])
        print(request.POST['password'])

        res_data = {}

        if not (username and password and re_password) :
            res_data['error'] = '전부 입력해야 합니다'
        elif password != re_password :
            res_data['error'] = '비밀번호가 다릅니다'
        else :
            entry = appUser.objects.filter(userid=username)
            if entry.exists():
                res_data['error'] = '아이디 중복'
                return render(request, 'app/english/join.html', res_data)
            else :
                user = appUser(userid=username, password=make_password(password))
                user.save()
                return redirect('apps:login')
        return render(request, 'app/english/join.html', res_data)


def register(request):
    if request.method == 'GET':
        return render(request, 'app/english/jointtest.html')

    elif request.method == 'POST':
        username = request.POST.get('email', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('repassword', None)
        res_data = {}

        if not (username and password and re_password):
            res_data['error'] = '전부 입력해야 합니다'
            print("error1")
            return redirect('apps:login')
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다'
            print("error2")
            return redirect('apps:login')
        else:
            print("error999")
            entry = appUser.objects.filter(userid=username)
            if entry.exists():
                res_data['error'] = '아이디 중복'
                return redirect('apps:login')
            else:
                user = appUser(userid=username, password=make_password(password))
                user.save()
                return redirect('apps:login')
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
        else :
            entry = appUser.objects.filter(userid=log_username)
            if entry.exists() :
                dbuser = appUser.objects.get(userid=log_username)
                print(log_username)
                print(dbuser.userid)
                if check_password(log_password, dbuser.password):
                    request.session['user'] = dbuser.userid
                    request.session.get_expire_at_browser_close()
                    return redirect('apps:main')
                else :
                    response_data['error'] = '비밀번호 오류'
                

        return render(request, 'app/english/login.html', response_data)

def logout(request) :
    request.session.pop('user')
    return redirect('apps:login')

def main(request) :
    if request.method == 'GET' :
        if 'user' in request.session:

            return render(request, 'app/english/main.html')
        else :
            return redirect('apps:login')

@csrf_exempt

def study(request) :
    if request.method == 'GET' :
        if 'user' in request.session:
            user_id = request.session.get('user')
            current_user = appUser.objects.get(userid=user_id)
            msg = current_user.user_idx

            print(request.GET.get('user_gpt_id_hidden'))
            if request.GET.get('user_gpt_id_hidden') == 'user_gpt_id_ok':

                GPT_respond = GPTeacher_answer(request.GET.get('user_answer_to_view'),request.GET.get('gpt_answer_to_view'),request.GET.get('user_gpt'))   # 정답 질문 / GPT 해설 / 유저 질문
                print(GPT_respond)
                GPT_respond = str(GPT_respond)
                GPT_respond = GPT_respond.replace("\n", "")
                return render(request, 'app/english/study.html', {'message':msg,'GPT_respond':GPT_respond} )
            else:
                GPT_respond = ""
                return render(request, 'app/english/study.html', {'message':msg,'GPT_respond':GPT_respond} )
        else :
            return redirect('apps:login')
    elif request.method =='POST':
        if request.POST.get('forwhat') == "book":
            if 'user' in request.session:
                user_id = request.session.get('user')
                current_user = appUser.objects.get(userid=user_id)
                print(request.POST.get('idx_update2'))
                page = request.POST.get('idx_update2')
                book = current_user.bookmark

                mark = book.split(',')
                if not(str(page) in mark) :
                    mark.append(page)
                result = ' '.join(map(str, mark))

                current_user.bookmark = result
                #current_user.bookmark = ""
    
            current_user.save()
            return render(request, 'app/english/main.html')

        elif request.POST.get('forwhat') == "exit":
            if 'user' in request.session:
                user_id = request.session.get('user')
                current_user = appUser.objects.get(userid=user_id)
                current_user.user_idx = request.POST.get('idx_update')

            
            current_user.save()
            user_id = request.session.get('user')

            current_user = appUser.objects.get(userid=user_id)

            return render(request, 'app/english/main.html')
        else:
            body = json.loads(request.body.decode('utf-8'))
            print(body)
            print("ajax성공")
            text1 = body.get('sentence_answer')
            print(text1)
            text2 = body.get('explanation')
            print(text2)
            text3 = body.get('user_ask')
            print(text3)
            GPT_respond = GPTeacher_answer(text1, text2, text3)
            print(GPT_respond)
            GPT_respond = str(GPT_respond)
            GPT_respond = GPT_respond.replace("\n", "")
            return JsonResponse({"GPT_respond_ajax":GPT_respond})

def rank(request) :
    if request.method == 'GET' :
        if 'user' in request.session:
            return render(request, 'app/english/rank.html')
        else :
            return redirect('apps:login')

def mypage(request) :
    if request.method == 'GET' :
        if request.session.get('user') != None :
            user_id = request.session.get('user')
            current_user = appUser.objects.get(userid=user_id)
            book = current_user.bookmark
            booklist = {}
            mark = book.split(',')

            
            return render(request, 'app/english/mypage.html',{'user':current_user.userid})
        else :
            return redirect('apps:login')

def get_quiz_data(request):
    if request.method == 'GET':
        datas = Sentencedata.objects.values(
            'idsentencedata',
            'sentencedata_contents',
            'sentencedata_word1',
            'sentencedata_word2',
            'sentencedata_word3',
            'sentencedata_word4',
            'sentencedata_answerword'
        ).order_by('idsentencedata')
        data_list = list(datas)
        return JsonResponse(data_list, safe=False)
def GPTeacher_answer(text1,text2,text3):
    message = []
    message.append({"role": "user", "content": text1})
    message.append({"role": "assistant", "content": text2})
    message.append({"role": "user", "content": text3})


    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= message
    )
    chat_response = completion.choices[0].message.content

    return chat_response

def bookmark(request, page) :
    if request.method == 'GET' :
        if request.session.get('user') != None :
            msg = page
            return render(request, 'app/english/study.html', {'message':msg} )
        else :
            return redirect('apps:login')


def exam(request) :
    if request.method == 'GET' :
        if 'user' in request.session:
            user_id = request.session.get('user')
            current_user = appUser.objects.get(userid=user_id)
            msg = random.sample(range(1,100), 10)
            list = json.dumps(msg)
            return render(request, 'app/english/study2.html', {'message':list} )
        else :
            return redirect('apps:login')
    
    else :
        if 'user' in request.session:
            user_id = request.session.get('user')
            current_user = appUser.objects.get(userid=user_id)
            updatescore = request.POST.get('updatescore', None)

            current_user.score = updatescore
            current_user.save()
            return redirect('apps:main')
        else :
            return redirect('apps:login')

        return redirect('apps:main')

# # --> FBV : Function Based View = 함수 기반 뷰
# @api_view(['GET']) # Decorator -> 함수를 꾸미는 역할(함수에 대한 성격을 표시해주는 표기법)
# def HelloAPI(request) :
#     return Response("hello world!")

# # --> CBV : Class Based View = 클래스 기반 뷰
# # class HelloAPI(APIView) :
# #     def get(self, request) :
# #         return Response("hello wolrd")